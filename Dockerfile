FROM python:3.4
RUN pip install Flask
ADD . /code
WORKDIR /code
CMD python hello.py