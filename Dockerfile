# 使用官方Python镜像作为基础镜像
FROM python:3.12.2-slim

RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  software-properties-common \
  git \
  && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的工作目录
COPY lib /app/lib
COPY models /app/models
COPY app.py /app/
COPY requirements.txt /app/

# 安装pip依赖
RUN pip install --no-cache-dir -r requirements.txt

# 对外暴露Streamlit默认使用的8501端口
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENV MODEL_PATH=/app/models/tokenizer

# 启动Streamlit应用
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]