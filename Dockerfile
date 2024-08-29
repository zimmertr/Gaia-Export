FROM python
RUN python3 -m pip install git+https://github.com/kk7ds/gaiagpsclient
WORKDIR /app
COPY bulk_export.py /app/bulk_export.py
ENTRYPOINT ["python3", "/app/bulk_export.py"]
