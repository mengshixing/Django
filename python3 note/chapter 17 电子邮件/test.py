
s=b'DT:SPM 163 smtp4,DtGowADHfvmHn11Zd1XJAA--.11451S2 1499307911,\
please see http://mail.163.com/help/help_spam_16.htm?ip=111.160.189.62&hostid=smtp4&time=1499307911'
import struct

import base64

print(base64.b64decode(s))

#print(struct.unpack('>IH', s))