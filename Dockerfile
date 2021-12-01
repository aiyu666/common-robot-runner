FROM linuxserver/docker-compose

COPY Pipfile* /home

WORKDIR /home

RUN apt-get update && \
    apt-get install -y \
    software-properties-common gcc
    
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get install -y \
    python3.9 \
    python3.9-distutils \
    python3-pip

RUN pip3 install pipenv && \
    pipenv lock && \
    pipenv install --system --deploy --dev

RUN curl -O https://download.docker.com/linux/static/stable/x86_64/docker-18.03.1-ce.tgz && \
    tar zxvf docker-18.03.1-ce.tgz && \
    cp docker/docker /usr/local/bin/ && \
    rm -rf docker docker-18.03.1-ce.tgz
