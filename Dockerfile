FROM python:3.12.2-bullseye
LABEL mantainer="@luderibeiro"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH "/scripts:/venv/bin:$PATH"


COPY projekt/ /projekt
COPY scripts/ /scripts

WORKDIR /projekt

EXPOSE 8000

RUN apt update -y \
    && apt install -y \
    wget \
    build-essential \
    libc6-dev \
    freetds-dev \
    freetds-bin \
    unixodbc-dev \
    tdsodbc \
    python3-gdal \
&& sed -i 's,^\(MinProtocol[ ]*=\).*,\1'TLSv1.0',g' /etc/ssl/openssl.cnf \
&& sed -i 's,^\(CipherString[ ]*=\).*,\1'DEFAULT@SECLEVEL=1',g' /etc/ssl/openssl.cnf \
&& curl -O http://acraiz.icpbrasil.gov.br/credenciadas/CertificadosAC-ICP-Brasil/ACcompactado.zip \
&& unzip ACcompactado.zip -d /usr/local/share/ca-certificates/ \
&& update-ca-certificates \
&& apt-get autoremove -yqq --purge \
&& apt-get clean \
&& rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base \
&& sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
&& sed -i 's/^# pt_BR.UTF-8 UTF-8$/pt_BR.UTF-8 UTF-8/g' /etc/locale.gen \
&& locale-gen en_US.UTF-8 pt_BR.UTF-8 \
&& update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8

RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \
    tar xvJf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \
    cp wkhtmltox/bin/wkhtmlto* /usr/bin/
RUN wget ftp://ftp.freetds.org/pub/freetds/stable/freetds-1.1.20.tar.gz -T 360 && \
    tar -xvf freetds-1.1.20.tar.gz && \
    cd freetds-1.1.20/ && \
    ./configure --prefix=/usr/local --with-tdsver=7.4 && \
    make && \
    make install \
    && echo "\n\
[FreeTDS] \n\
Description=TDS driver (Sybase/MS SQL) \n\
Driver=libtdsodbc.so \n\
Setup=libtdsS.so \n\
CPTimeout= \n\
CPReuse= \n\
UsageCount=1 \n\
" >> /etc/odbcinst.ini

RUN python -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install -r /projekt/requirements.txt \
    && adduser --disabled-password --no-create-home appuser \
    && mkdir -p /data/web/static \
    && mkdir -p /data/web/media \
    && chown -R appuser:appuser /venv \
    && chown -R appuser:appuser /data/ \
    && chmod -R 755 /data/web/static \
    && chmod -R 755 /data/web/media \
    && chmod -R +x /scripts \
    && chmod +rx /scripts/run.sh

USER appuser

ENTRYPOINT [ "run.sh" ]
