# 1、99乘法表
# 解题思路：最里面的j在乘法表的前面，第二个循环中j的取值范围在1到i的值之间
# def multiplication_table():
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             print("{} * {} = {}\t".format(j, i, i * j), end="")
#         print()
#
#
# multiplication_table()

# 2、导入random模块，生成1-100的随机列表（列表数字不重复，长度为100）
import random


def random_num():
    # 先生成一个1-100的列表
    lis1 = list(range(1, 101))

    list2 = []

    # 当list1的列表有值时
    while len(lis1) > 0:
        # 则随机从list1中选择一个数字，将选择的数字插入到list2中，list1中则删除，这样可以让list2中的数字不再重复
        num = random.choice(lis1)
        lis1.remove(num)
        list2.append(num)

    print(list2)


random_num()
