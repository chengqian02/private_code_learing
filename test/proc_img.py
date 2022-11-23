from operator import mod
import re
from PIL import Image
import pytesseract


def calc_diff(pixel):
    #     计算pixel与背景的离差平方和，作为当前像素点与背景相似程度的度量
    if pixel[0] == 200 and pixel[2] == 200 and pixel[2] == 200:
        return False
    # if pixel[0] == 175 or pixel[1] == 75 or pixel[2] == 125:
    #     return False
    if pixel[0] != pixel[2]   and pixel[1] != pixel[2]:
        if pixel[0] >  50   or pixel[1] > 50 or  pixel[2] > 50:
            return False
    return True

im  = Image.open('yzm.png').convert(mode='RGB')
delete_color = [237, 237, 237]
pixdata = im.load()
for y in range(im.size[1]):
    for x in range(im.size[0]):
        if not calc_diff(pixdata[x, y]):
            pixdata[x, y] = (255, 255, 255)

       
im.save("output1.png")
        # result = calc_diff(pixdata[y,x], delete_color)
        # if ( result == 4107):
        #     pass
        # else:
        # print(pixdata[x,y])
# im.show()


# im1 = Image.open('output1.png')
# im1.show()
config = r'--oem 3 --psm 6 outputbase digits'
result1 = pytesseract.image_to_string(Image.open('yzm.png'), config=config)
result2 = pytesseract.image_to_string(Image.open('output1.png'), config=config)

print(result1,result2)
