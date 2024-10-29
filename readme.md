# 用于从 ETS2 地图文件中提取 Mod 名称的脚本
此脚本用于从 ETS2 地图文件中提取 Mod 名称。它的工作原理是在地图文件中搜索字符串 “city/country/ferryname”，然后提取其后面的文本。该脚本将输出在地图文件中找到的所有 mod 名称的列表。

## 使用说明
1. 首先，请确保安装了python并将其添加到环境变量中
2. 然后，从地图mod中提取所需的文件
3. 使用VSCode或Notepad++打开脚本并进行自定义
   1. 修改需要提取的文件路径
   2. 修改需要提取的字段前面的字符（尽可能详细，方便定位），
   3. 修改需要保存输出的文件路径
4. 在脚本所在文件夹右键`在终端中打开`
5. 输入`python city_name_extract_info`并按回车
6. 打开输出的文件并检查其格式
7. 根据你的语言修改`val`字段即可
8. country和ferry按照此方法重复即可

### 脚本位置
脚本文件在源代码的`src`文件夹以及Release的`script.7z`中都含有



# script for extracting mod names from ETS2 map files
This script is used to extract the mod names from ETS2 map files. It works by searching for the string "city/country/ferryname" in the map file and then extracting the text that comes after it. The script will output a list of all the mod names found in the map file.




## Usage
1. Start by installing python and adding it to the environment variables 
2. Extract the files you need to extract from the map mod folder    
3. Use VSCode or Notepad++ to open the script and customize the script
   1. Modify the path of the file to be extracted
   2. the characters in front of the field to be extracted (as detailed as possible, easy to locate),   
   3. modify the path of the file to be saved as output     
4. Right click in the folder where the script is located`Open in a terminal`    
5. Type `python city_name_extract_info` and press enter    
6. Open the output file and check its formatting        
7. Just modify the `val` field according to your language
8. Country and ferry can be repeated according to this method   

### script position
The script files are contained in the `src` folder of the source code and in `script.7z` of the Release


