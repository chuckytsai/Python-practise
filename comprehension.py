# python 才有的作法
# list, dict, set才可以用

nums = [1, 2, 3, 4]

squared_x = [item ** 2 for item in nums]
print("squared_x", squared_x)

squared_y = [item ** 2 for item in nums if item > 2]
print("squared_y", squared_y)

# 變成dict
squared_x_dict = {item: item ** 2 for item in nums}
print("squared_x_dict", squared_x_dict)

squared_x_generator = (item ** 2 for item in nums)
for i in squared_x_generator:
    print("squared_x_generator", i)
