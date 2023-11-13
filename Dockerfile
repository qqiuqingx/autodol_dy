FROM python:3.10.9
# 安装 FFmpeg（具体命令可能因基础镜像而异）
RUN apt-get update && apt-get install -y ffmpeg
# 设置工作目录
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
