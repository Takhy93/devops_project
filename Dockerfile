FROM ubuntu:16.04
MAINTAINER papa_john
RUN apt-get update -y && \
apt-get install -y python3-pip python-dev
RUN mkdir -p projet/app
RUN ls
COPY . projet/
WORKDIR projet
RUN ls
COPY ./app/ projet/app/
RUN pip3 install -r requirements.txt
WORKDIR app
RUN ls
RUN ls templates
ENTRYPOINT ["python3"]
CMD [ "main" ]
   