#1. square pattern
n=5
for i in range(1,n+1):
    star1 = ''
    for j in range(1,n+1):
        star1 = star1+ '* '
    print(star1)

#2.rectangle
n=5
for i in range(1,n+1):
    star1 = ''
    for j in range(1,(n*2)+1):
        star1 = star1+ '* '
    print(star1)

#3.	Right-Angled Triangle (Left-Aligned)
n = 5
for i in range(1,n+1):
    star = ''
    for j in range(1,i+1):
        star = star+'* '
    print(star)


#4.Right-Angled Triangle (Right-Aligned)
n = 5

for i in range(1,n+1):
    star = ''
    space = ''
    for j in range(n-i):
        space = space+'  '
    for k in range(i):
        star = star+'* '
    print(space+star)

#5.Inverted Triangle (Left-Aligned)
n = 5
for i in range(n,0,-1):
    star = ''
    for j in range(1,i+1):
        star = star+'* '
    print(star)

#6.Inverted Triangle (Right-Aligned)
n = 5
for i in range(n,0,-1):
    star = ''
    space = ''
    for k in range(i):
        star = star+'* '
    for j in range(n-i):
        space = space + '  '
    
    print(space+star)

# # 7.Centered Pyramid Pattern
n = 4
for i in range(1,n+1):
    star = ''
    space=''
    for j in range(n-i):
        space = space+ '  '
    for k in range(2*i-1):
        star = star+'* '
    print(space+star)


# 8.Diamond Pattern
n = 4
for i in range(1,n+1):
    space = ''
    star = ''
    for j in range(n-i):
        space = space+'  '
    for k in range(2*i-1):
        star = star + '* '
    print(space+star)
for i in range(n-1,0,-1):
    space = ''
    star = ''
    for j in range(n-i):
        space = space+'  '
    for k in range(2*i-1):
        star = star + '* '
    print(space+star)


# 9.Butterfly Pattern

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==n and j==n:
            print(' *',end=' ')
        else:
            print('*',end=' ')
    for j in range(1,(n-i)*2+1):
        print(' ',end=' ')
    for j in range(1,i+1):
        if i==n and j==1:
            print(' ',end= '')
        else:
            print('*',end = ' ')
    print()
    
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    for j in range(1,(n-i)*2+1):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end= ' ')
    print()


#10. Left-Aligned Half Diamond
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()


# 11. Right-Aligned Half Diamond 
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()



# 12. Sandglass Pattern
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end= ' ')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(2,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()



# 13. Increasing Width Triangle
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    

# 14. Decreasing Width Triangle
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

# 15 Right-Aligned Hill Pattern
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()

