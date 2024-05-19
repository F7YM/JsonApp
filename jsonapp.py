import sys, json
from easygui import *

# 定义颜色，方便coloredPrint函数使用
class Colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

# 颜色打印函数
def coloredPrint(text, color):
    print(color + text + Colors.ENDC)        
 
if len(sys.argv) > 1:
    AppFile = sys.argv[1]
    # 尝试读取文件，若未找到文件就报错
    try:
        with open(AppFile, 'r', encoding='utf-8') as f:
            f.read()
    except FileNotFoundError:
        coloredPrint(f'[ERROR] 未找到文件{AppFile}', Colors.ERROR)
        exit()
else:
    coloredPrint('[ERROR] 未传入jsonapp文件', Colors.ERROR)
    exit()

with open(AppFile, 'r', encoding='utf-8') as f:
    lineNum = 1
    jsonCode = ''  # 用于存储找到的JSON代码块
    inJsonBlock = False  # 标记是否在JSON代码块中

    for line in f:
        lineNum += 1
        lineCode = line.strip()  # strip()用于去掉每行末尾的换行符

        # 检查是否是新的一段JsonUI开始
        if lineCode.startswith('$japp:main:'):
            inJsonBlock = True  # 标记进入JSON代码块
            jsonCode = ''  # 重置JSON代码块
            continue  # 跳过当前循环，继续下一次循环

        # 如果在JSON代码块中，则累加代码
        if inJsonBlock:
            # 检查是否遇到end标记
            if lineCode.startswith('end'):
                inJsonBlock = False  # 标记退出JSON代码块
            else:
                jsonCode += lineCode

    # 找到的JSON代码块储存在jsonCode变量中
    jsonCodeData = json.loads(jsonCode)
    msg = jsonCodeData['msg']
    msgbox(msg = msg)


""" # JSON_DATA = '$japp:main:'
# 使用json.loads()函数读取JSON字符串并转换为字典
data = json.loads(JSON_DATA)

# 访问字典中的'msg'键值
message = data['msg']
print(message)  # 输出: hello """