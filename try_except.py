# exception handling

a = 10
b = 1
# else
# finally


try:
    print(a/b)
except ZeroDivisionError as temp:
    print("Incorrect values ",temp)
else:
    print("Else block")