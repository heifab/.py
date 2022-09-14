'''

def hannuota( n, str1, str2, str3) :
    if n==0 :
        return 0
    hannuota( n-1, str1, str3, str2)
    print(str1,'->',str2)
    hannuota( n-1, str3, str2, str1)
    return 0

hannuota(5,'a','b','c')

'''

'''
def printinfo( arg1, *vartuple ):
    #单星输入元组
    print ("输出: ")
    print (arg1)
    print (vartuple)

printinfo( 70, 60, 'ahub', 30 )
printinfo( 'qndiuf', 70, 40)
'''

'''
def printinfo( arg1, **vartuple ):
    #双星输入字典
    print ("输出: ")
    print (arg1)
    print (vartuple)

printinfo( 70, a = 60, b = 'ahub', c = 30 )
printinfo( 'qndiuf', d = 70, e = 40)
'''

'''
matha = lambda a, b: a*a + b

print(matha( 1, 3 ))
print(matha( 4, 2 ))
'''

def f(a, b, /, c, d, *, e, f):
    #形参 a 和 b 必须使用指定位置参数
    #c 或 d 可以是位置形参或关键字形参
    #而 e 和 f 要求为关键字形参
    print(a, b, c, d, e, f)

f(1, 2, 3, d = '4nj', e = 5, f = 6)