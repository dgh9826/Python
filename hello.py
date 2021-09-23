a_list =['사과','감','배']
b_list=['영희','철수',['사과','감']]

print(a_list[1])
print(b_list[2][0])

a_list.append('수박') # list 추가 함수
print(a_list)
print('===========')

a_dict = {'name':'bob','age':24}
print(a_dict['name'])
a_dict['height']=178
print(a_dict)

a_dict['fruits'] =a_list
print(a_dict)
print(a_dict['fruits'][0])

