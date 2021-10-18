l = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
print(l)
l1 = ''
for i in l:
    a = chr(ord(i)+1)
    l1 += a
print(l1) 
l2 = ''
for i in l:
    b = l.replace(("z"),("A"))
print(l2)
l3 = ''
for i in l:
    c = l3.replace('!','-')
    l3 = c
print(l3)