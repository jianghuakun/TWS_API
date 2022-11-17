#本方法是识别验证码

from PIL import Image
import pytesseract
import base64
import sys


def image(imagebase64):
    img_base64 = imagebase64
    img_base64 = img_base64[22:]
    # begin python3 base64_binascii.Error: Incorrect padding错误.原因是base64加密的数据是4的整数倍，如果不是就在后面加‘=’补齐
    missing_padding = 4 - len(img_base64) % 4
    #print(1, len(img_base64))
    if missing_padding:
        img_base64 += '=' * missing_padding
    # end
    #print(2, len(img_base64))
    imgdata = base64.b64decode(img_base64)
    file = open('1.jpg', 'wb')
    file.write(imgdata)
    file.close()

    pytesseract.pytesseract.tesseract_cmd = 'c:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    tessdata_dir_config = '--tessdata-dir "c:/Program Files (x86)/Tesseract-OCR/tessdata"'
    image = Image.open("1.jpg")
    code = pytesseract.image_to_string(image, config=tessdata_dir_config)
    #print(code)
    return code
