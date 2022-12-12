myDictio = {
    "text": "textValue",
    "example": 2,
    "dictio": 1.4
}

print(dir(myDictio)) ## show all dictionaries methods.

## Some methods.
print(type(myDictio))               # return dict
print(myDictio.keys())              # return myDictio = (["text", "example", "dictio"])
print(myDictio.items())             # return myDictio = ([("text": "textValue"), ("example": 2) , ("dictio": 1.4)])