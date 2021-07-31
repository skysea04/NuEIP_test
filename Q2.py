str = "人易科技:上 機 測 驗 - 演算法"

# 第一小題
str = str.replace(":", "：")

# 第二小題
str = str.replace(" ", "", 3)

# 第三小題
left = str.find("：")
right = str.find("-")
print(str[left+1:right])