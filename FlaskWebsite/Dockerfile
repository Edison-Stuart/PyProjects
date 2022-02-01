FROM python:3.8

ADD requirements.txt requirements.txt
RUN mkdir Flaskwebsite && \
    pip install -r requirements.txt && \
    cd Flaskwebsite

COPY . /Flaskwebsite/

CMD /usr/local/bin/python3 /Flaskwebsite/site.py