# file_manipulator

このファイル操作ツールでは、以下のコマンドをサポートしています：

1. **reverse**: ファイル内容を逆順にして、別のファイルとして保存する。
2. **copy**: ファイル内容を別のファイルにコピーする。
3. **duplicate-contents**: ファイル内容を指定回数繰り返して複製する。
4. **replace-string**: ファイル内の特定の文字列を別の文字列に置き換える。


## 必要条件
- Python 3.6 以上
- ファイルシステムの読み書き権限

## インストール
このリポジトリをクローンまたはダウンロードして、ローカルマシンに保存してください。

## 使用方法
コマンドラインから `file_manipulator.py` を実行してください。サポートされているコマンドは次のとおりです：

1. **reverse**:
```
python3 file_manipulator.py reverse <input_filepath> <output_filepath>
```

2. **copy**:
```
python3 file_manipulator.py copy <input_filepath> <output_filepath>
```

3. **duplicate-contents**:
```
python3 file_manipulator.py duplicate-contents <input_filepath> <repeat_integer>
```
`repeat_integer` は繰り返す回数を整数で指定してください。

4. **replace-string**:
```
python3 file_manipulator.py replace-string <input_filepath> <find_string> <replace_string>
```
検索文字列（`find_string`）と置換文字列（`replace_string`）の両方を必ず指定してください。

## 注意事項
- 指定した出力ファイルパス（`output_filepath`） が無効またはアクセス不可の場合、`output.txt` という名前で同じディレクトリに保存されます。
