import os

def extract_info_from_files(directory, character, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('SiiNunit\n')
        outfile.write('{\n')
        outfile.write('localization_db : .localization\n')
        
        outfile.write('{\n\n##Ferries\n')

        # 遍历指定文件夹中的所有文件
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            # 确保是文件而不是文件夹
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        # 如果行中包含特定字符
                        if character in line:
                            # 提取特定字符后的信息,replace('"', '')是为了去掉"
                            info = line.split(character, 1)[1].strip().replace('"', '')
                            # 将提取的信息按照SiiNunit格式写入到输出文件
                            outfile.write(f'  key[]: "{info}"\n')
                            outfile.write(f'  val[]: "{info}"\n\n')

        outfile.write('}\n}')

# 示例调用
directory_path = r'F:\map_ferry_names_location\def\ferry'  # 替换为你的文件夹路径
character = 'ferry_name: "'  # 设置为要查找的字符
output_file_path = r'F:\map_ferry_names_location\ferry_name_output2.sii'  # 替换为你想保存输出的文件路径,支持.txt和.sii格式
extract_info_from_files(directory_path, character, output_file_path)
