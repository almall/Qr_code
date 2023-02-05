FROM python:3.9.12

COPY ./qr_code.py /qr/
COPY ./docker.txt /qr/

WORKDIR /qr/

RUN pip3 install -r ./docker.txt

ENTRYPOINT ["python", "qr_code.py"]