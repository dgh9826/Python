myemail = 'sparta@naver.com'

result=myemail.split('@')
print(result)

result1=myemail.split('@')
print(result1[1])

result2=myemail.split('@')[1].split('.')[0]
print(result2)

myemaii='sparta@naver.com'

result3 = myemaii.replace('naver','gmail')

print(result3)