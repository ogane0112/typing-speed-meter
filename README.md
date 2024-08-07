# typing-speed-meter
寝る前に作ったのでかなり雑です。
だれかなおしてください(他人任せ)
## 環境設定

### 1. 仮想環境の作成と有効化

まず、仮想環境を作成して有効化します。

#### Windows

```sh
python -m venv typing-speed-meter-env
typing-speed-meter-env\Scripts\activate
```

#### macOS/Linux

```sh
python -m venv typing-speed-meter-env
source typing-speed-meter-env/bin/activate
```

### 2. 依存関係のインストール

仮想環境が有効化された状態で、必要なライブラリをインストールします。

```sh
pip install -r requirements.txt
```

### 3. アプリケーションの実行

仮想環境が有効化され、依存関係がインストールされた状態で、以下のコマンドを実行してアプリケーションを起動します。

```sh
python typing-speed-meter.py
```

## 使用しているライブラリ

- `tkinter`：Python標準ライブラリ。GUIを作成するために使用。
- `keyboard`：キーボード入力をキャプチャするために使用。

## requirements.txtの生成方法

現在の仮想環境にインストールされているすべてのパッケージを`requirements.txt`に出力するには、以下のコマンドを実行します。

```sh
pip freeze > requirements.txt
```

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。
```

