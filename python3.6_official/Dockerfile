FROM python:3.6

# ARGで変数を定義
# buildする時に変更可能
# コンテナ内のディレクトを決めておく
ARG root_directory=/app/

#ファイルをappディレクトリに追加
COPY . ${root_directory}/

# pythonの実行環境をインストール
#WORKDIR ${root_directory}/pip/
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

#ソースファイルの取得
#WORKDIR ${root_directory}/src
#CMD [ "git", "clone", "git@" ]
