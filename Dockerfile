# python3.9のイメージをダウンロード
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# pipを使ってpoetryをインストール
RUN pip install poetry

# poertyの定義ファイルをコピー（存在する場合）
COPY pyproject.toml* poetry.lock* ./

# poetryでライブラリをインストール
RUN poetry config virtualenvs.in-project true
RUN if [-f pyproject.toml]; then poetry install --no-root; fi

# uvicornのサーバーを立ち上げる。
ENTRYPOINT ["poetry","run","uvicorn","app:main:app","--host","0.0.0.0","--reload"]