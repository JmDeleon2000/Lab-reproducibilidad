FROM python:3.10-slim-buster

RUN python -m pip install pip
RUN python -m pip install matplotlib
RUN python -m pip install numpy


COPY src/* .

CMD python main.py