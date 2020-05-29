# 링크 : https://www.acmicpc.net/problem/2671

#(100~1~|01)~

import re
text = input()
regex = re.fullmatch('(100+1+|01)+', text)

if regex:
    print("SUBMARINE")
else:
    print("NOISE")
