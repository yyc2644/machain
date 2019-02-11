#encoding utf-8
import yaml
import os
path = "/Users/YiCheng/VSCode/machain/test/qrcode.yaml"

f= open(path,'r',encoding = 'utf-8')
cont = f.read()

x = yaml.load(cont)

print(x['btctest1']['Mnemonic'])
