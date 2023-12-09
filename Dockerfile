# https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker
FROM python:3.12.0-slim

WORKDIR /app
WORKDIR /var/lib/sqlite3

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    wget \
    r-base-core \
    && rm -rf /var/lib/apt/lists/*

# Setup python
COPY ./requirements_app.txt .

RUN pip3 install -r requirements_app.txt

# Setup playwright
RUN playwright install
RUN playwright install-deps

# Setup R environment
RUN R --slave -e 'install.packages("renv")'
RUN R --slave -e 'renv::init(force = TRUE)'
RUN R --slave -e 'renv::restore(rebuild = TRUE, clean = TRUE)'
