FROM python:3.12.0a3-bullseye

RUN python -m pip install pip
RUN python -m pip install matplotlib
RUN python -m pip install numpy


COPY src/* .

CMD python main.py