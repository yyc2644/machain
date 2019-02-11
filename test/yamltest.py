#encoding utf-8
import yaml
<<<<<<< HEAD

f = open(r'/Users/yangyicheng/Documents/GitHub/machain/test/qrcode.yaml')
y = yaml.load(f)

print(type(y))
=======
import os
path = "/Users/YiCheng/VSCode/machain/test/qrcode.yaml"

f= open(path,'r',encoding = 'utf-8')
cont = f.read()

x = yaml.load(cont)

print(x['btctest1']['Mnemonic'])
>>>>>>> 472ebbbda128ed0a30a230c9e429a7226467ceaf
