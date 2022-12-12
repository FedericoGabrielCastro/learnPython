myStr = "Example String"

print(dir(myStr))   ## show all string methods.

## Some Methods.
print(myStr.upper())                                # return "EXAMPLE STRING"
print(myStr.lower())                                # return "example string"
print(myStr.swapcase())                             # return "eXAMPLE sTRINNG"
print(myStr.capitalize())                           # return "Example string"
print(myStr.replace("Example", "Text"))             # return "Text string"
print(myStr.count("t"))                             # return 1
print(myStr.startswith("Example"))                  # return True
print(myStr.endswith("text"))                       # return False
print(myStr.split())                                # return ["Example", "String"]
print(myStr.find("a"))                              # return 3
print(len(myStr))                                   # return 13
print(myStr.index("E"))                             # return 0
print(myStr.isnumeric())                            # return False
print(myStr.isalpha())                              # return False
print(myStr[0])                                     # return "E"


## Concat.
print("show " + myStr)                              # return "show Example String"
print(f"show {myStr}")                              # return "show Example String"
print("show {0}".format(myStr))                     # return "show Example String"