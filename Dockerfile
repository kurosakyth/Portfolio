FROM selenium/standalone-chrome:latest

WORKDIR /app

COPY . /app
USER root
RUN apt-get update && apt-get install -y wget gnupg unzip

# Install Python and pipenv
RUN apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip pipenv
RUN pipenv install selenium
RUN pipenv install pytest
RUN pipenv install pytest-xdist
RUN pipenv install pytest-html

# Install dependencies
COPY Pipfile* ./
RUN pipenv install --system --deploy --dev

# Download and install chromedriver
RUN wget https://chromedriver.storage.googleapis.com/111.0.5563.64/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm chromedriver_linux64.zip

# Set the command to execute when the container starts
CMD ["pipenv", "run", "python", "-m", "pytest", "--html=reports/report.html", "./tests/runner/test_all.py", "-n", "3"]
