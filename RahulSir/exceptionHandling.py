# a = 0
# b = 100
# c = b/a
# print(c) #ZeroDivisionError: division by zero

# print('This is my code')

#due to error in line no 4,line6 will not run exceution 
# stop to overcome it we use try.... except....

try:
    a = 0
    b = 100
    c = b/a
    print(c)
except:
    print('please enter correct value of a')


print("My code have to run")


'''

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- EncodingWarning
           +-- ResourceWarning
'''


# f = open(r'C:\Users\Nikhita\Desktop\pythonProgr\RahulSir\amit.txt')

# print(f.read())

#FileNotFoundError: [Errno 2] No such file or directory:
try:
    f = open(r'C:\Users\Nikhita\Desktop\pythonProgr\RahulSir\amit.txt')

    print(f.read())

    print(10/100)

    list_odd = [1,3,5,7,9]
    print(list_odd[2])
    #print(list_odd[20])#IndexError: list index out of range

except FileNotFoundError as e:
    print("some error are occured ",e)

except IndexError as n:    
    print("Element not found",n)
else:
    print("all code excuted sucessfully")       


finally:
     ("I will run every time")
