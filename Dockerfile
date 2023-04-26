# especifica la imagen base
FROM python:3.10-slim-buster

# establece el directorio de trabajo
WORKDIR /app

# copia los archivos necesarios
COPY . /app

# instala las dependencias
RUN pip install pipenv
RUN pipenv install
RUN pipenv install selenium
RUN pipenv install pytest
RUN pipenv install pytest-xdist
RUN pipenv install pytest-html

# establece el comando a ejecutar al iniciar el contenedor
CMD ["python", "tests/runner/test_candidates.py"]