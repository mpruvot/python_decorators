import typing

class FunctionNotTypedError(Exception):
    pass
class BadTypeError(Exception):
    pass

def check_typed_func(func):
    def wrapper(*args, **kwargs):
        varnames = [var for var in func.__code__.co_varnames][:func.__code__.co_argcount]
        annotated_types = [i for i in func.__annotations__.values()]
        if len(annotated_types) != len(varnames):
            raise FunctionNotTypedError 
        for kwarg in kwargs.keys():
            expected_type = func.__annotations__[kwarg]
            if not isinstance(kwargs[kwarg], expected_type):
                raise BadTypeError
            if kwarg not in func.__annotations__:
                raise FunctionNotTypedError
        for arg, expected_type in zip(args, annotated_types):
            if not isinstance(arg, expected_type):
                raise BadTypeError
        
            
        res = func(*args, **kwargs)
        return res
    return wrapper

@check_typed_func
def print_names(name_a: str, name_b: str):
    print(name_a, name_b)
    
if __name__ == "__main__":
    print_names(name_a="pruvot", name_b="marius")
    

#https://docs.python.org/3/library/inspect.html#types-and-members