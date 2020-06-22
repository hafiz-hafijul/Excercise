try:
    x = 'f'
    print(x*10, sep =' ')
    
except TypeError:
    print('concate wrong')

d = {'a':1,'b':2,'c':3}
for i in d:
    print(i ,'=>',d[i])