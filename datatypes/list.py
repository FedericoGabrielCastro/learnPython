myList = [1, "text", 1.34, True, [1, 2 ,3]]
myStrList = ["text", "example", "sort" ]

print(dir(myList)) ## show all list methods.

## Some methods.
print(type(myList))                                 # return list
print(len(myList))                                  # return 5
print(myList[1])                                    # return "text"
print("text" in myList)                             # return True
myList[0] = "text";             print(myList)       # return myList = ["text", "text", 1.34, True, [1, 2 ,3]]
myList.append("example");       print(myList)       # return myList = [1, "text", 1.34, True, [1, 2 ,3], "example"]
myList.extend([5, 6, 7]);       print(myList)       # return myList = [1, "text", 1.34, True, [1, 2 ,3], 5, 6, 7]
myList.insert(1, "example");    print(myList)       # return myList = [1, "example", "text", 1.34, True, [1, 2 ,3]]
myList.pop();                   print(myList)       # return myList = [1, "text", 1.34, True]
myList.remove("text");          print(myList)       # return myList = [1, 1.34, True, [1, 2 ,3]]
myStrList.sort();               print(myStrList)    # return myStrList = ["example", "sort", "text"]
myList.index("text");           print(myList)       # return 1


## Create list.
number_list = list((1,2,3,4))                       # return [1, 2, 3, 4]
print(range(1, 5))                                  # return [1, 2, 3, 4]d