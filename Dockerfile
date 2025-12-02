FROM python:3.8-slim


WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

EXPOSE 8000

ENTRYPOINT [ "python3", "app.py" ]

# コマンド 使い方例
# python バージョン選び方 https://www.docker.com/ja-jp/blog/containerized-python-development-part-1/
# https://zenn.dev/kawauso_danu/articles/5f70d3b454da71 これに従ってます

