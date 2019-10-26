FROM python

RUN python --version
RUN which python


WORKDIR /

#RUN pip3 install -r requirements.txt



EXPOSE 5432
COPY files/ /



#ENTRYPOINT [ "python" ]

CMD python server.py