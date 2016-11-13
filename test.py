# -*- coding: utf-8 -*-

s = '''
http://www.wangpansou.cn/s.php?q=%E8%BE%B9%E7%BC%98%E6%80%A7%E4%BA%BA%E6%A0%BC%E9%9A%9C%E7%A2%8D%E6%B2%BB%E7%96%97%E6%89%8B%E5%86%8C+pdf&book_id=2188
'''

import re
book_id = re.findall(re.compile('.*?book_id=(.*?)$', re.S), str(s))[0]
print book_id
# pattern = re.compile('<div.*?href="(.*?)".*?>(.*?)</a>.*?<div.*?>(.*?)</div>', re.S)
# for i in re.findall(pattern, str(s))[0]:
#     print i

