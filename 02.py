
words = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''

array_of_words = words.split(' ')

for i in array_of_words:
    for j in i:
        num = ord(j)-ord('a')
        if num >=0 and num <=25:
            num = (num + 2) % 26
            print(chr(ord('a')+num),end='')
        else:
            print(j,end='')
    print(end=' ')
