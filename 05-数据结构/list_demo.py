# -*- encoding:utf-8 -*-
# !/usr/bin/python3

'''
Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。
以下是 Python 中列表的方法：
'''

# 1、list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list1 = [1, 2, 3, 4, 5];

list1.append(6)

print(list1);

# 2、list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list2 = [0, 1, 2, 3, 4]
list2.extend(list1);
print('2、list.extend(L)', list2);

# 3、list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，
# 例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list3 = ["a", "b", "c"]
list3.insert(0, "d");
print("3、list.insert(i, x)", list3);

# 4、list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
ls4 = [1, 2, 3, 4];
ls4.remove(1);
print("4、list.remove(x)", ls4);

# 5、list.pop([i])	从列表的指定位置删除元素，并将其返回。
# 如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被删除。
# （方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
ls5 = [0, 1, 2, 3, 4, 5]
ls5.pop(0);
print("5、list.pop([i])", ls5);

# 6、list.clear()	移除列表中的所有项，等于del a[:]。
ls6 = [1, 2, 3, 4, 5];
ls6.clear();
print("6、list.clear()", ls6);

# 7、list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
ls7 = [1, 2, 3, 4, 5, 6];
print("7、list.index(x)", ls7);
print("ls7.index(5)", ls7.index(5));

# 8、list.count(x)	返回 x 在列表中出现的次数。
ls8 = [0, 1, 1, 3, 4, 5];
print("8、list.count(x)", ls8.count(1));

# 9、list.sort()	对列表中的元素进行排序。
ls9 = [12, 11, 12, 113, 1234, 123];
ls9.sort()
print("9、list.sort()", ls9);

# 10、list.reverse()	倒排列表中的元素。
ls9.reverse();
print("10、list.reverse()", ls9);

# 11、list.copy()	返回列表的浅复制，等于a[:]。
ls11 = [1, 2, 3, 4];
ls12 = ls11.copy();
print("11、list.copy()", ls12);
