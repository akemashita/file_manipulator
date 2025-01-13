import sys

def main():
    # 引数に不足がある場合は処理を終了する
    if len(sys.argv) < 4:
        print('Invalid input, 4 or 5 arguments are required. See below example.')
        print('[reverse] file_manipulator.py reverse input_filepath output_filepath')
        print('[copy] file_manipulator.py copy input_filepath output_filepath')
        print('[duplicate-contents] file_manipulator.py duplicate-contents input_filepath repeat_integer')
        print('[replace-string command] file_manipulator.py replace-string input_filepath find_string replace_string')
        sys.exit(1)

    script_name = sys.argv[0]
    command = sys.argv[1]
    input_filepath = sys.argv[2]
    output_filepath = sys.argv[3]

    print(f'Script_name: {script_name}')
    print(f'Command: {command}')
    print(f'Input Filepath: {input_filepath}')
    print(f'Output Filepath: {output_filepath}')

    # 入力ファイルが開けない場合はエラーを返す
    try :
        with open(input_filepath) as f:
            input_data = f.read()

            if command == 'reverse':
                reverse(input_data, output_filepath)

            elif command == 'copy':
                copy(input_data, output_filepath)

            elif command == 'duplicate-contents':
                # print('duplicate-contents command was selected')
                duplicate_contents(input_data, output_filepath, input_filepath)

            elif command == 'replace-string':
                # print('replace-string command was selected')

                if len(sys.argv) < 5:
                    print('Invalid input, replace-string command require 5 arguments. See example below.')
                    print('file_manipulator.py replace-string input_filepath find_word replace_word')

                else:
                    find_word = sys.argv[3]
                    replace_word = sys.argv[4]
                    replace_string(input_data, find_word, replace_word, input_filepath)

            else:
                print('Invalid command. Acceptable commands are following 4:')
                print('reverse, copy, duplicate-contents, replace-string')

    except FileNotFoundError:
        print(f'Invalid INPUT_FILEPATH. Your set input file does not exist there: {input_filepath}')



def reverse(input_data, output_filepath):
    rev = input_data[::-1]

    with open(output_filepath, 'w') as out_f:
        out_f.write(rev)
        print('Reversed command has been completed.')


# python3 file_manipulator.py copy test.txt output.txt
def copy(input_data, output_filepath):

    with open(output_filepath, 'w') as out_f:
        out_f.write(input_data)
        print(f'Copy command has been completed. Output file here: {output_filepath}')


# python3 file_manipulator.py duplicate-contents test.txt 3
def duplicate_contents(input_data, str_repeat_count, input_filepath):
    # 繰り返し回数が数字以外の場合はエラーを返す
    try :
        int_repeat_count = int(str_repeat_count)

        duplicated_contents = input_data * int_repeat_count

        with open(input_filepath, 'w') as input_f:
            input_f.write(duplicated_contents)

        print(f'Duplicate-contents command has been completed. Output file here: {input_filepath}')

    except ValueError:
        print('Invalid input, duplicate-contents command require an integer for the number of repeats as the third argument. See example below.')
        print('file_manipulator.py duplicate-contents input_filepath 2')


# python3 file_manipulator.py replace-string test.txt Appending Replaced
def replace_string(input_data, target_str, replace_str, input_filepath):
    replaced_data = input_data.replace(target_str, replace_str)

    with open(input_filepath, 'w') as f:
        f.write(replaced_data)


if __name__ == '__main__':
   main()




# with open(pathname) as f:
#     contents = f.read()

# with open(pathname, 'w') as f:
#     f.write(contents + '\nAppending more text to this file!')


# # reverse command

# python3 file_manipulator.py reverse ~/vagrant/workspace/practice_recursion/file_manipulator/test.txt ~/vagrant/workspace/practice_recursion/file_manipulator/output.txt