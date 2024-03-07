

# 变量类型的转换
i = 3
str(i)

i = '456'
int(i)
float(i)

i = 1.234
float(i)

def exo1():
    print("hello world");
    print("hello", end="");
    print("hello", end="--");

    y = 33
    nom = "jack"
    print("{} a {} ans".format(y, exo1()))
    print("{0} a {1} ans".format(y, exo1())) # 加入index
    print("{1} a {0} ans".format(y, exo1()))

    p = 3000 / 3452
    print("resulat egale {:.2f}".format(p)) # 输出时保留两位小数

def boucle1():
    # 冒号！！！
    if b == 1:
        b = 2
    elif b == 2:
        b = 3
    else: b = 4

def list1():
    list1 = [ 'runoob', 786 , 2.23, 'john', 70.2 ] # 列表
    tinylist1 = [123, 'john']

    print (list1)              # 输出完整列表
    print (list1[0])            # 输出列表的第一个元素
    print (list1[1:3])          # 输出第二个至第三个元素 
    print (list1[2:])           # 输出从第三个开始至列表末尾的所有元素
    print (tinylist1 * 2)       # 输出列表两次
    print (list1 + tinylist1)   # 打印组合的列表
    print (len(tinylist1))      #随即输出tinylist里的元素

    list_range1 = list(range(10)) #输出0 - 10
    print (list_range1)
    print (len(list_range1)) # 输出长度

    list_range2 = list(range(1,10)) #输出1 - 9
    print (list_range2)
    print (len(list_range2)) # 输出长度

    list_range3 = list(list_range1 + list_range2) # List de list
    print (list_range3)

    for x in range(5):
        print(x)



def dictionary1():
    dict = {}
    dict['one'] = "c'est 1"
    dict[2] = "c'est 2"

    tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}
    tinydict['name'] = 'Li' #更改键值为name对应的值
    print (dict['one'])          # 输出键为'one' 的值
    print (dict[2])              # 输出键为 2 的值
    print (tinydict)            # 输出完整的字典
    print (tinydict.keys())      # 输出所有键
    print (tinydict.values())    # 输出所有值

def fonction1(x):
    print("votre numbre: {}".format(x))
    return x ** 2, x ** 3 

print(fonction1(3))
    





