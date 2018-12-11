# 任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

def counter(file):
    with open(file,'r') as f:
        # text = f.readlines()
        sum = 0
        # f.readlines()返回一个由文本每行字符串为元素组成的列表
        for line in f.readlines():
            sum += len(re.findall(r'\w+',line))
    return sum
if __name__ == "__main__":
    file = './test.txt'
    print(counter(file))