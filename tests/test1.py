def myfunction(first, *others):
    for num in others:
        print(num)
    print("first: ", first)


others_1 = "other1"
others_2 = "other2"
myfunction(first=3, 2, 1)
