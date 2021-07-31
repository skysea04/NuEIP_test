import copy
lst_a = [77, 5, 5, 22, 13, 55, 97, 4, 796, 1, 0, 9]
lst_b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Set():

    def __init__(self, lst):
        self.lst = copy.deepcopy(lst)

    def has(self, value):
        return value in self.lst

    def add(self, value):
        self.lst.append(value)

    def remove(self, value):
        self.lst.remove(value)
    
# 交集    
def intersection(a, b):
    res = Set([])
    set_a = Set(a)  
    for i in b:
        if set_a.has(i):
            res.add(i)
    return res.lst

# 差集
def difference(a, b):
    res = Set(a)
    for i in b:
        while res.has(i):
            res.remove(i)
    return res.lst

# 聯集
def union(a, b):
    res = Set(a)
    for i in b:
        if not res.has(i):
            res.add(i)
    return res.lst

lst_c = intersection(lst_a, lst_b)
lst_d = difference(lst_a, lst_b)
lst_e = union(lst_a, lst_b)

print(f"陣列c(交集)：{lst_c}")
print(f"陣列d(差集)：{lst_d}")
print(f"陣列e(聯集)：{lst_e}")