from asyncio.windows_events import NULL


x =NULL
def f():
    x=1
    
f()
print(x)
 