'''输出
s = 'Hello, Runoob\n'
str(s)
repr(s)
print(repr(s))

print(str(1/7))

hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)
print(repr((x, y, ('Google', 'Runoob'))))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    # ljust 左对齐  center 居中对齐  zfill 左填充0 
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    #0、1、2代表后续的第几个，2d、3d、4d代表几格宽的右对齐，.3f代表精确到小数点后三位

print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
#大括号内部可使用01或名字的自由组合，或者无参数按照顺序输出

print('常量 PI 的值近似为： {!r}。'.format('fwefe'))
#!a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

f = open("输入输出/date.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!" )
f.close()# 关闭打开的文件
'''


'''输入
str = input("请输入：")
print ("你输入的内容是: ", str)

f = open("输入输出/date.txt", "r")
str1 = f.read()
print(str1)
#print(str2)  str2 = f.readline() 诸如此类还有.readlines()  .write()  .tell()  .seek()
f.close()

'''



