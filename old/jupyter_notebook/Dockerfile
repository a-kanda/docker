FROM jupyter/minimal-notebook

# ARGで変数を定義
# buildする時に変更可能
# コンテナ内のディレクトを決めておく
ARG root_directory=/app/
ARG home_directory=/home/jovyan/

#ファイルをappディレクトリに追加
COPY . ${root_directory}/

# pythonのライブラリをインストール
WORKDIR ${root_directory}/pip/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#ソースファイルの取得
#WORKDIR ${root_directory}/src
#WORKDIR /home/jovyan/work

#CMD [ "git", "clone", "git@" ]

WORKDIR ${home_directory}/
