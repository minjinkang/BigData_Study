import re

# 문자열에서 패턴 찾기
pattern = r'apple'
text = 'I like apple.'
result = re.search(pattern, text)
if result:
    print('찾은 패턴:', result.group())
else:
    print('일치하는 패턴이 없습니다.')

# 문자열에서 모든 패턴 찾기
pattern = r'apple'
text = 'I like apple. I have an apple.'
results = re.findall(pattern, text)
if results:
    print('찾은 패턴:', results)
else:
    print('일치하는 패턴이 없습니다.')

# 패턴으로 문자열 대체하기
pattern = r'apple'
replace = 'orange'
text = 'I like apple. I have an apple.'
result = re.sub(pattern, replace, text)
print('바뀐 문자열:', result)

# 패턴으로 문자열 분리하기
pattern = r'\s+'
text = 'I like apple. I have an apple.'
results = re.split(pattern, text)
print('분리된 문자열:', results)