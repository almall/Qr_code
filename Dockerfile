FROM python

WORKDIR /QR_CODE/

COPY ./main.py /QR_CODE/
COPY ./qrpython /QR_CODE/
#COPY docker.txt /QR_CODE/

#RUN pip install -r docker.txt

ENTRYPOINT ["python3", "main.py"]