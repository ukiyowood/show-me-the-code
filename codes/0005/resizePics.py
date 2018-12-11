import glob
from PIL import Image
# linux和windows下路径表示方法不一致,未完成

def reSize(dirPath,sizeX=100,sizeY=100):
    for dir in glob.glob(dirPath + '*.jpg'):
        print(dir)

if __name__ == '__main__':
    reSize('.\pics')