FROM python
RUN python3 -m pip install git+https://github.com/kk7ds/gaiagpsclient
WORKDIR /app
COPY bulk_export.sh /app/bulk_export.sh
RUN chmod +x /app/bulk_export.sh
ENTRYPOINT ["/app/bulk_export.sh"]
