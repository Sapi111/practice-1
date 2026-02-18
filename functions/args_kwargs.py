# 1) *args пример
def sum_args(*args):
    return sum(args)
print(sum_args(1,2,3))

# 2) **kwargs пример
def print_kwargs(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
print_kwargs(name="Timur", age=16)

# 3) *args и **kwargs вместе
def combined(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
combined(1,2,3,name="Timur")

# 4) args как список
def list_args(*args):
    for i in args:
        print(i)
list_args(5,6,7)

# 5) kwargs как словарь
def dict_kwargs(**kwargs):
    return kwargs
print(dict_kwargs(a=1,b=2))