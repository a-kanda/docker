FROM ubuntu:18.04

# ARGで変数を定義
# buildする時に変更可能
# コンテナ内のディレクトを決めておく
ARG root_directory=/app/

#apt-getを最新化
RUN apt-get update

#ファイルをappディレクトリに追加
#COPY . ${root_directory}/

# pythonの実行環境をインストール
WORKDIR ${root_directory}/pip/
RUN apt install python3 -y
#RUN apt install python-pip -y
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

#pythonプログラムの実行
#WORKDIR ${root_directory}/src
#CMD [ "python", "./exec.py" ]
