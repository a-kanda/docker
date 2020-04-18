#FROM jupyter/minimal-noteboo1
FROM jupyter/datascience-notebook


# ARGで変数を定義
# buildする時に変更可能
# コンテナ内のディレクトを決めておく
ARG root_directory=/app/
ARG home_directory=/home/jovyan/




#ARG seborn_fonts_directory=/opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/
ARG seborn_fonts_directory=/usr/share/fonts/truetype
ARG cache_file=/home/jovyan/.cache/matplotlib/fontlist-v310.json

#ファイルをappディレクトリに追加
COPY . ${root_directory}/

# jupyter notebookに日本語化対応させる
COPY ./fonts/ ${seborn_fonts_directory}
RUN echo "font.family : IPAexGothic" >>  /opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc
RUN sed -i "s/font=\"sans-serif\"/font=\"IPAexGothic\"/" /opt/conda/lib/python3.7/site-packages/seaborn/rcmod.py
RUN rm ${cache_file}


# pythonのライブラリをインストール
#WORKDIR ${root_directory}/pip/
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

#ソースファイルの取得
#WORKDIR ${root_directory}/src
#WORKDIR /home/jovyan/work

#CMD [ "git", "clone", "git@" ]

WORKDIR ${home_directory}/
