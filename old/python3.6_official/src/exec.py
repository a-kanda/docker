# coding:utf-8
import subprocess

print("HELLO python3.6_official")
print("./src/exec.pyに記述したプログラムが実行されます。")

exec_file = "/work/git/trade/exec.py"

subprocess.call(['python3.6',exec_file])

