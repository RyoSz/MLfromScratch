# Python Crash Course
## Strings
data = 'hello world'
print(data[0])
print(len(data))
print(data)

## Numbers
value = 123.1
print(value)
value = 10
print(value)

## Boolean
a = True
b = False
print(a,b)

## Multiple assignment
a, b, c = 1, 2, 3
print(a,b,c)

## No value
a = None
print(a)
print(a,b,c)
print(b+c)

## Flow control
value = 99
if value == 99:
    print('That is fast')
elif value > 200:
    print('That is fast')
else:
    print('That is safe')

## For loop
for i in range(10):
    print(i)

## While loop
i = 0
while i < 3.5:
    print (i)
    i += 1

## Typle: read-only collections of items.
a = (1,2,3)
print(a)

## List
mylist = [1,2,3]
print("Zeroth Value: %d" % mylist[0])
# 解説：””で文字列を印刷する指示。その中に関数からの指示値を入れたい。%dで符号付き10進整数に変換しますよという指示。その後に%で変換元を指定。
mylist.append(4)
print(mylist)
print("List Length: %d" % len(mylist))
for value in mylist:
    print(value)

## Dictionary
mydict = {'a':1, 'b':2, 'c':3}
print(mydict)
print(mydict.keys())
print(mydict.values())
print("A value: %d" % mydict['a'])
mydict['a'] = 11
print("A value: %d" % mydict['a'])
print("Keys: %s" % mydict.keys())
print("Values: %s" % mydict.values())
for key in mydict.keys():
    print(mydict[key])

## Functions
def mysum(x,y):
    return x+y
result = mysum(1,156)
print(result)
