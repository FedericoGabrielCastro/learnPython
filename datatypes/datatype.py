## Strings.
print(type('text'))             # return string 
print(type("text"))             # return string
print(type('''text'''))         # return string
print(type("""text"""))         # return string

## Numbers.
print(type(30))                 # return int
print(type(30.5))               # return float

## Booleans.
print(type(True))               # return boolean
print(type(False))              # return boolean

## List (mutable)
print(type([10, "text", True])) # return list

## Tuples (inmutable)
print(type("text", (), {}))     # return tuple

## Dictorionies (key, value)
print(type({
    "name": "text",
    "age": 29
}))                             # return dict

## None
print(type(None))               # return NoneType