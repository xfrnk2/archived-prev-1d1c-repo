#정규표현식 - Regular Expression(regex)
# 참고해서 본 곳 : https://blog.naver.com/PostView.nhn?blogId=dudwo567890&logNo=130162403749
# 주의깊게 본 곳 : https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/07/20/regex-usage-01-basic/
import re

text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber)