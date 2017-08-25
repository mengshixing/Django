
# copy文件脚本 运行环境ubuntu
# 用于多次复制同一份文件并改名

import shutil

for i in range(19):

    shutil.copy('/var/yp/super.md', ''.join(['/var/yp/super',str(i),'.md']))
	


	
# 一开始给脚本名字起的是copy.py,报错
# module 'shutil' has no attribute 'copy'
# 修改文件名解决