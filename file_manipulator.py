import sys
import os

def main():
    """
    メイン処理：コマンドライン引数に基づいて各コマンドを実行します。
    """

    # 引数に不足がある場合は処理を終了する
    if len(sys.argv) < 4:
        print('Invalid input, 4 or 5 arguments are required. See below usage.')
        print_usage()
        sys.exit(1)

    script_name = sys.argv[0]
    command = sys.argv[1]
    input_filepath = sys.argv[2]
    output_filepath = sys.argv[3]

    # 入力ファイルが開けない場合はエラーを返す
    try :
        with open(input_filepath, 'r') as f:
            input_data = f.read()

            if command == 'reverse':
                output_filepath = check_output_file(sys.argv[3])
                reverse(input_data, output_filepath)

            elif command == 'copy':
                output_filepath = check_output_file(sys.argv[3])
                copy(input_data, output_filepath)

            elif command == 'duplicate-contents':
                repeat_count = sys.argv[3]
                duplicate_contents(input_data, repeat_count, input_filepath)

            elif command == 'replace-string':
                if len(sys.argv) < 5:
                    print('Invalid input, replace-string command require 5 arguments. See example below.')
                    print('file_manipulator.py replace-string input_filepath find_word replace_word')
                    sys.exit(1)

                find_word = sys.argv[3]
                replace_word = sys.argv[4]
                replace_string(input_data, find_word, replace_word, input_filepath)

            else:
                print('Invalid command. Acceptable commands are following 4:')
                print('reverse, copy, duplicate-contents, replace-string')

    except FileNotFoundError:
        print(f'Invalid INPUT_FILEPATH. Your set input file does not exist there: {input_filepath}')


def print_usage():
    print('Usage:')
    print('[reverse] file_manipulator.py reverse input_filepath output_filepath')
    print('[copy] file_manipulator.py copy input_filepath output_filepath')
    print('[duplicate-contents] file_manipulator.py duplicate-contents input_filepath repeat_integer')
    print('[replace-string command] file_manipulator.py replace-string input_filepath find_string replace_string')


def check_output_file(output_filepath):
    """
    指定されたパスにファイルが作成できるかの確認
    """
    try:
        with open(output_filepath, 'w') as f:
            f.write('check create file.')

        os.remove(output_filepath)
        return output_filepath

    except:
        return 'output.txt' # エラーが発生した場合は、同じフォルダにoutput.txtで出力


def write_to_file(data, filepath, success_message):
    """
    指定されたデータをファイルに書き込みます。
    """
    with open(filepath, 'w') as f:
        f.write(data)
    print(success_message)


# python3 file_manipulator.py reverse test.txt output.txt
def reverse(input_data, output_filepath):
    """
    inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
    """
    reversed_data = input_data[::-1]
    write_to_file(reversed_data, output_filepath, 'Reversed command has been completed.')


# python3 file_manipulator.py copy test.txt output.txt
def copy(input_data, output_filepath):
    """
    inputpath にあるファイルのコピーを作成し、outputpath として保存します。
    """
    write_to_file(input_data, output_filepath, 'Copy command has been completed.')


# python3 file_manipulator.py duplicate-contents test.txt 3
def duplicate_contents(input_data, str_repeat_count, input_filepath):
    """
    inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
    """
    # 繰り返し回数が数字以外の場合はエラーを返す
    try :
        int_repeat_count = int(str_repeat_count)
        duplicated_contents = input_data * int_repeat_count
        write_to_file(duplicated_contents, input_filepath, 'Duplicate-contents command has been completed.')

    except ValueError:
        print('Invalid input, duplicate-contents command require an integer for the number of repeats as the third argument. See example below.')
        print('file_manipulator.py duplicate-contents input_filepath 2')


# python3 file_manipulator.py replace-string test.txt Appending Replaced
def replace_string(input_data, target_str, replace_str, input_filepath):
    """
    inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
    """
    replaced_data = input_data.replace(target_str, replace_str)
    write_to_file(replaced_data, input_filepath, 'Replace-string command has been completed.')


if __name__ == '__main__':
   main()