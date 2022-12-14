FROM python:3.10-slim-buster

RUN python -m pip install pip
RUN python -m pip install matplotlib
RUN python -m pip install numpy
RUN python -m pip install pandas



COPY src/* .

CMD python main.py