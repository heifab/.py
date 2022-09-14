'''列表

list1 = [11, 34, 56]
list1.sort()
print(list1)


list.append(x)	    把一个元素添加到列表的结尾，
                    相当于 a[len(a):] = [x]。
list.extend(L)	    通过添加指定列表的所有元素来扩充列表，
                    相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。
                    i是准备插入到其前面的那个元素的索引
                    例如 a.insert(0, x) 会插入到整个列表之前
                    而 a.insert(len(a), x)相当于 a.append(x)
list.remove(x)	    删除列表中值为 x 的第一个元素。
                    如果没有这样的元素，就会返回一个错误。
list.pop([i])	    从列表的指定位置移除元素，并将其返回。
                    如果没有指定索引，a.pop()返回最后一个元素。
                    元素随即从列表中被移除。
list.clear()	    移除列表中的所有项，等于del a[:]。
list.index(x)	    返回列表中第一个值为 x 的元素的索引。
                    如果没有匹配的元素就会返回一个错误。
list.count(x)	    返回 x 在列表中出现的次数。
list.sort()	        对列表中的元素进行排序。
list.reverse()	    倒排列表中的元素。
list.copy()	        返回列表的浅复制，等于a[:]。


list2 = [x/2 for x in list1 if x > 30]
print(list2)

list3 = [x + y for x in list1 if x > 3 for y in list2 ]
print(list3)

del list3[3:5]
print(list3)

'''

'''元组

t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5)
print(t)
print(u)

'''

'''集合

a = {x for x in 'abrwveacadabra' if x not in 'abc'}
print(a)
a = set('owfnnne')
print(a)
a = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(a) 
'''

'''字典
a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(a)

a = {x: x**2 for x in (2, 4, 6)}
print(a)

a = dict(sape = 4139, guido = 4127, jack = 4098)
print(a)
'''
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)