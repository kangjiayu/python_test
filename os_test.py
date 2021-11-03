import os

# print("当前目录：", os.getcwd())
# print("当前目录里有什么：", os.listdir())
import numpy as np

# print("data file in directory:", os.listdir())
# with open("day_wise.csv", "r") as f:
#     print("\n", f.read())
#data = np.loadtxt("day_wise.csv", str, delimiter=",", skiprows=1, dtype=np.int)
p = r'day_wise.csv'
with open(p, encoding='utf-8') as f:
    data = np.loadtxt(f, str, delimiter=",", skiprows=1)
    print(data[:, 1:])
