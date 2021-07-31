lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_sum, odd_sum = 0, 0
even_lst, odd_lst = [], []
for i in lst:
    if i % 2 == 0:
        even_sum += i
        even_lst.append(i)
    else:
        odd_sum += i
        odd_lst.append(i)


# 第一題答案：
print(f"奇數總和減偶數總和為：{odd_sum - even_sum}")
# 第二題答案：
print(f"偶數陣列：{even_lst}\n" + f"奇數陣列：{odd_lst}")