FROM continuumio/miniconda3
MAINTAINER vickyboston20
RUN conda create -n env python=3.7
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt