import sys

def main():
  # 引数に過不足がある場合は処理を終了する
  if len(sys.argv) != 4:
    print('Invalid input, just 4 arguments are required. Plese refer to the following statement.')
    print('file_manipulator.py COMMAND INPUT_FIELPATH OUTPUT_FILEPATH')
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
        contents = f.read()

        print(contents)

  except :
     print(f'Invalid INPUT_FILEPATH. Your set input file dose not exist there: {input_filepath}')




if __name__ == '__main__':
   main()




# with open(pathname) as f:
#     contents = f.read()

# with open(pathname, 'w') as f:
#     f.write(contents + '\nAppending more text to this file!')


# # reverse command

# python3 file_manipulator.py reverse ~/vagrant/workspace/practice_recursion/file_manipulator/test.txt ~/vagrant/workspace/practice_recursion/file_manipulator/output.txt