FROM ubuntu:16.04

#更新软件源，必须要执行，否则可能会出错。-y就是要跳过提示直接安装。
RUN apt-get -y update
RUN apt-get install -y python-dev python-pip
RUN apt-get install -y python-setuptools
#MySQL-Python必须得先安装这个库
RUN apt-get install -y libmysqlclient-dev

RUN apt-get install -y wget
RUN mkdir /vts_test
#设置工作目录
WORKDIR /vts_test
#将当前目录加入到工作目录中
ADD . /vts_test
#install any needed pacakges in requirements.txt，你要把所有需要安装的Python模块加到这文件中。
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django-bootstrap-toolkit==2.15.0
#对外暴露端口
EXPOSE 80 8080 8000 5000
#设置环境变量
ENV SPIDER=/vts_test
