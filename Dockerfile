# pull official base image
FROM python:3.10-slim

# set working directory
WORKDIR /usr/src/app

# install python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./requirements.txt .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]