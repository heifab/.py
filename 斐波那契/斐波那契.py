''' 
#1
a = 0
b = 1
i = 0
print(a,end=' ')
while ( i < 10 ):
    print(b,end=' ')
    a,b = b,a + b
    i += 1
'''

#2
import sys

i , j = 20 , 0
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(i) # f 是一个迭代器，由生成器返回生成

while (j < i):
    print(next(f), end=" ")
    j += 1

'''
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
'''