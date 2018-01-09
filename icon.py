import argparse
from PIL import Image

# parser = argparse.ArgumentParser()
# parser.add_argument('file')

# args = parser.parse_args()
# imgpath = args.filename

# 字符串列表
ascii_char = list(r"$@&%B#=-. ")

# 把RGB转为灰度值，并且返回该灰度值对应的字符标记
def select_ascii_char(r, g, b):
    gray = int((19595 * r + 38469 * g + 7472 * b) >> 16)  # ‘RGB－灰度值’转换公式
    unit = 256.0/len(ascii_char)  # ascii_char中的一个字符所能表示的灰度值区间
    return ascii_char[int(gray/unit)]


# 返回给定路径图片的字符表示，用户在此还可以指定输出字符画的宽度和高度
def output(imgpath, width=200, height=100):
    im = Image.open(imgpath)
    im = im.resize((width, height), Image.NEAREST)
    txt = ""

    for h in range(height):
        for w in range(width):
            txt += select_ascii_char(*im.getpixel((w, h))[:3])
        txt += '\n'
    return txt


def save_as_txtfile(txt):
    with open('/Users/shitakusei/Desktop/learning/icon.txt', 'wb') as f:
        f.write(txt)


if __name__ == '__main__':
    print (output('/Users/shitakusei/Desktop/test.jpg', 120, 90))
    save_as_txtfile(output('/Users/shitakusei/Desktop/test.jpg', 120, 90))
