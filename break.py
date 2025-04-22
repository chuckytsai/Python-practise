# 用於迴圈結束
for i in "123456789":
    if i == "5":
        break
    print("Q1", i)


# 只會打斷該迴圈底下
for i in "123456789":
    if i == "4":
        break
    for j in "abcdefg":
        if j == "c":
            break
        print("Q2", i, j)
