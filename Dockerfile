# Dockerfile for learn_ci demo

# step 1: Use a base image
FROM python:3.10-slim

# step 2: 设置工作目录
WORKDIR /app

# step 3: 复制所需文件到工作目录下
COPY requirements.txt .

# step 4: 安装依赖
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# step 5: 复制应用代码到工作目录
COPY main.py .
COPY module/ ./module/

# step 6: 设置启动命令
CMD ["python", "./main.py"]