count=0
while count < 5 :
    count +=1
    if count == 100:
        break
    print('LOOP',count)
else:
    print('循环正常执行完了')
#当循环正常执行完时  未被break打断 才会执行else



count=0
while count < 5 :
    count +=1
    if count == 3:
        break
    print('LOOP',count)
else:
    print('循环正常执行完了')

#当循环未正常执行完时 被break打断 不会执行else
