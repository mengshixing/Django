#base64编码原理
#A-Za-z0-9+/ 刚好64个字符对应编号0-63,生成索引表
#二进制每三个字节分割一下3*8分成4*6,最大的111111值63,对应表的/
#如果二进制串不是3字节倍数,Base64用\x00字节在末尾补足后，再在编码的末尾
#加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
#\x00即16进制0占一个字节8位

import base64

print(base64.b64encode(b'sadkadk[0qj[qffjq[fj3mm'))
#b'c2Fka2Fka1swcWpbcWZmanFbZmozbW0='
print(base64.b64decode(b'c2Fka2Fka1swcWpbcWZmanFbZmozbW0='))
#如果去掉=解码错误binascii.Error: Incorrect padding
#print(base64.b64decode(b'c2Fka2Fka1swcWpbcWZmanFbZmozbW0'))

#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
#所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

#b'' Byte类型字符串 \Xb7十六进制 占一个字节,5个16进制数字,加上i一共48位
# i 对应105位ascii码表 01101001   10110111  00011101 11111011 11101111 11111111
# 解析为011010 011011  011100  011101       111110 111110 111111 111111
# 26 27 28 29 62 62 63 63对应abcd++//
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))# b'abcd++//'
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))# b'abcd--__'


#练习:请写一个能处理去掉=的base64解码函数：

def decode_b64(str):
    if len(str)%4!=0:
        str=str+'===='[0:4-len(str)%4]
        #或者str=str+'='*(4-len(str)%4)
    print(base64.b64decode(str))

decode_b64('YWJjZA')
decode_b64('YWJjZA=')
print('===='[0:1])
print('='*5)