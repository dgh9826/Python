age =24
if age > 20:
    print('성인입니다.')
    print("성인입니다2")
else:
    print("청소년입니다.")

print('======반복문======')
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

for ff in fruits:
    print(ff)

count = 0
for fruit in fruits:
    if fruit=='사과':
        print(fruit)
        count +=1
print(count)