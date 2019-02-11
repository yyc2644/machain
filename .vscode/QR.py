from PIL import Image
import qrcode
import yaml
import os

QRPath = "/Users/YiCheng/VSCode/machain/test/qrcode.yaml"
x = yaml.load(open(QRPath,'r',encoding = 'utf-8').read())

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=8,
    border= 1
)
#第一个参数是币种，第二个参数是助记词/私钥/地址
qr.add_data(x['btctest1']['Mnemonic'])
# qr.add_data(x['ethtest']['PrivateKey'])
qr.make(fit=True)  
img = qr.make_image()

img.show()
