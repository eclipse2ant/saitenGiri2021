#global x
x = 1


def f():
  global x
  x = 3
  return x

def g():
#  global x
#  x = 12
  return x


print(f())
print(g())
print(x)