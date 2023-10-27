FROM python:3.11
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "80"]
