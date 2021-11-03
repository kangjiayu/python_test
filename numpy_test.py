import numpy as np

test1 = np.array([5, 10, 12, 6])

# for i in test1:
#     print(i)
print(np.expand_dims(test1, axis=0))

a = test1.shape
for i in range(a[0]):
    print(test1[i])

# test2 = np.array([5.1, 8.2, 11, 6.3])
#
# # 首先需要把它们都变成二维，下面这两种方法都可以加维度
# test1 = np.expand_dims(test1, 0)
# test2 = test2[np.newaxis, :]
#
# print("test1加维度后 ", test1)
# print("test1加维度后 ", test2)
#
# # 然后再在第一个维度上叠加
# all_tests = np.concatenate([test1, test2])
# print("括展后\n", all_tests)
# print(all_tests.itemsize)
# print(test1.itemsize)
# print(test1.dtype)
# print(all_tests.reshape(4, 2))
# c = np.array([[1, 2], [3, 4]], dtype=complex)
# print(c)
d = np.arange(24).reshape([2, 3, 4])
print(d.itemsize)
# print(d)
# print(d[1])
# print(d[1, 1])
print(d[1, 1, 1])
print(d[[1, 1, 1]])
# print(d[[1, 1, 1], [1, 1, 1]])

# d[0, 0, 0] = 32769
# print(d)
#c = np.loadtxt('day_wise.csv', delimiter=',', skiprows=1)
