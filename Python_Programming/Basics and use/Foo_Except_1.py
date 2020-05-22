# Вариант со своей функцией foo и ее результатами в зависимости от данных

def foo(a, b):
  try:
#    assert(a == b)
#    return
    c = a / b
    return c
  except ZeroDivisionError:
    print("ZeroDivisionError")
    return
  except ArithmeticError:
    print("ArithmeticError")
  except AssertionError:
    print("AssertionError")
  except TypeError:
    print("TypeError")
    return
  return
#
A =10
B = 0
Result = foo(A, B)
print("Result =", Result)
# A =10 B = 5 ==>
# # Result = 2.0
#
# A =10 B = 0 ==>
# ZeroDivisionError
# Result = None
#
# A =10 B = "2" ==>
# TypeError
# Result = None
#
# assert (a == b)
# A =10 B = 5 ==>
# AssertionError
# Result = None