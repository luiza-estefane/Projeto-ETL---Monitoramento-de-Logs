FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    libgtk2.0-0 \
    libxtst6 \
    libxi6 \
    xvfb \
    x11vnc \
    novnc \
    websockify \
    supervisor \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

COPY pdi-ce-*.zip /opt/
RUN unzip pdi-ce-*.zip && rm pdi-ce-*.zip && mv data-integration pentaho

COPY drivers/ /opt/pentaho/lib/

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 6080

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
