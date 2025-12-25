FROM python:3.8-slim


WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y ffmpeg \ 
    && pip install -r requirements.txt

COPY app/ .

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000", "--reload"]
# reloadで開発環境でもコードが変わったら即座に変わる。


# コマンド 使い方例
# python バージョン選び方 https://www.docker.com/ja-jp/blog/containerized-python-development-part-1/
# https://zenn.dev/kawauso_danu/articles/5f70d3b454da71 これに従ってます

