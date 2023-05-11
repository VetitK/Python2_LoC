import os
import math
from math import sqrt, floor, ceil, pow
from math import *  # ไม่แนะนำ
import math as m

import time

t_start = time.time()
result = 0
for i in range(100001):
    result += i ** 2
print(result)
t_end = time.time()
print(t_end - t_start)

# Operating System

# PATHING
'test.txt'
'jedi/JediDaipaiSpain.py'

# check ว่าไฟล์มีอยู่จริง
print(os.path.exists('jedi/JediDaipaiSpain2.py'))
# check ว่าโฟลเดอร์นี้มีอยู่จริงมั้ย
os.path.isdir('jedi')
os.path.exists('jedi')
# list ว่าในโฟลเดอร์นี้มีไฟล์ชื่ออะไรบ้าง
print(os.listdir('jedi'))
# สร้างโฟลเดอร์
# os.mkdir('tiew')
# ลบโฟลเดอร์/ไฟล์
os.rmdir('jedi')
