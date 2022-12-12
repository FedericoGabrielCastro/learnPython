exampleList = ["text_one", "text_two", "example_one", "example_two"]

# Bucle for
for item in exampleList:
    if item == "text_two":
        continue                        # if exampleLIste have "text_two", continue with the bucle.
    if item == "text_one":
        break                           # if exampleList have "text_one", ends the bucle for here.
    print(item)                         # return "text_one", "text_two", "example_one", "example_two".

# Bucle while
while exampleList[1] == "text_two":
    print("exampleList")                # while exampleList element 1 is equal "text_two", execute this line.
    # Infinite "while" example.