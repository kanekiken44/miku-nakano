FROM python:latest
 
WORKDIR /miku
COPY . /miku
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "miku"]
