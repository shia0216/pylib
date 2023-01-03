# pylib
個人的にpython使う時の汎用的なコードをまとめる。

## 実行環境メモ

必要なパッケージを各ディレクトリの`requirements.txt`に記載する。

`venv`を使う。

```
python -m venv ./venv

# linux
source ./venv/bin/activate

# windows
Set-ExecutionPolicy RemoteSigned -Scope Process
./venv/Scripts/activate
```