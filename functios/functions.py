## basic funcitons.
print()                                                                 # print in console.
dir()                                                                   # get more info abaout data.
type()                                                                  # get type info about data.

## def functions.
def example(anyText):
    print(f"example {anyText}")

example("text")                                                         # return "example text"

## Lambda functions.
exampleL = lambda example_one, example_two: example_one + example_two
print(exampleL(1, 2))                                                   # return 3