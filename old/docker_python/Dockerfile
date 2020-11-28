FROM ubuntu:18.04

#SSHの設定を追加
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

#SSHの鍵認証とパスワード入力を不要にする
RUN passwd -d root
RUN sed -i 's/#PermitEmptyPasswords no/PermitEmptyPasswords yes/' /etc/ssh/sshd_config
RUN sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

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

#pythonコマンドで起動できるようにする
RUN echo alias python="python3"  >> ~/.bashrc
RUN alias pip="pip3"  >> ~/.bashrc

#pythonプログラムの実行
#WORKDIR ${root_directory}/src
#CMD [ "python", "./exec.py" ]
