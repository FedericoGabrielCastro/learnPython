mySet = {"text", "example", "set"}

print(dir(mySet)) ## show all set methods.

## Some methods.
print("text" in mySet)                      # return True
mySet.add("new");           print(mySet)    # return mySet = {"new", text", "example", "set"}
mySet.remove("text");       print(mySet)    # return mySet = {"example", "set"}
mySet.clear();              print(mySet)    # return mySet()
