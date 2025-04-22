# 用於迴圈, 強制下面一位的概念
nums = [1, 2, 3, 4, 5, 6]
for i in nums:
    if i == 5:
        continue
    print("Q1", i)


# continue後都不會執行
for i in "ABCDEFG":
    print("Q2", "Now the current i is " + i)
    continue
    print("Here is the line after continue")
