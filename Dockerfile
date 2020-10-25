FROM python:latest

#グラフ描画用
RUN pip install networkx matplotlib

RUN pip install graphillion

ADD first.py /docker_dir/
ADD second.py /docker_dir/
WORKDIR /docker_dir

