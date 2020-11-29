# dockerを使った開発環境
* deeplearning (ubuntu18.04上で機械学習実施用の環境)
  * tensorflow-gpu:1.15
  * jupyter-notebook
```
docker build -t deeplearning-env -f Dockerfile.gpu .
```
