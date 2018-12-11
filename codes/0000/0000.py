from PIL import Image,ImageDraw,ImageFont

def add_num(img):
    # 定义图片对象
    draw = ImageDraw.Draw(img)
    # 定义字体对象
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf',size = 100)
    # 填充颜色设置成红色
    fillcolor = '#ff0000'
    # 提取目标图片的尺寸
    width,height = img.size
    # 图片上添加文本
    draw.text((width-200,0),'100',font = myfont, fill = fillcolor)
    # 保存图片
    img.save('result.jpg','jpeg')
    return 0

if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)

