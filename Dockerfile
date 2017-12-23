FROM python:3.6

RUN mkdir /backend
WORKDIR /backend
COPY . .
RUN pip install PyMySQL hug

CMD ["hug", "-f", "hack.py"]