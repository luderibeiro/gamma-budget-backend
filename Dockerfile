FROM python:3.12.2-bullseye
LABEL mantainer="@luderibeiro & @paulogoncalveslima"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH "/scripts:$PATH"
ENV PYTHONPATH "${PYTHONPATH}:${PWD}"

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
    python3-gdal

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

WORKDIR /gamma_budget

COPY /gamma_budget/requirements.txt .

RUN pip3 install --upgrade pip \
    && pip3 install -r /gamma_budget/requirements.txt

COPY /gamma_budget/* .

RUN useradd -ms /bin/bash  appuser \
    && mkdir -p /data/web/static \
    && mkdir -p /data/web/media \
    && chown -R appuser:appuser /data/ \
    && chmod -R 755 /data/web/static \
    && chmod -R 755 /data/web/media 

WORKDIR /scripts

COPY /scripts/ /scripts/

RUN chmod -R +x /scripts

WORKDIR /gamma_budget

USER appuser

ENTRYPOINT ["/bin/bash", "run.sh" ]
