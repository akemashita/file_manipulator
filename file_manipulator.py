import sys

def main():
    # 引数に過不足がある場合は処理を終了する
    if len(sys.argv) != 4:
        print('Invalid input, just 4 arguments are required. Please refer to the following statement.')
        print('file_manipulator.py COMMAND INPUT_FILEPATH OUTPUT_FILEPATH')
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
                print('duplicate-contents command was selected')

            elif command == 'replace-string':
                print('replace-string command was selected')

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


if __name__ == '__main__':
   main()




# with open(pathname) as f:
#     contents = f.read()

# with open(pathname, 'w') as f:
#     f.write(contents + '\nAppending more text to this file!')


# # reverse command

# python3 file_manipulator.py reverse ~/vagrant/workspace/practice_recursion/file_manipulator/test.txt ~/vagrant/workspace/practice_recursion/file_manipulator/output.txt