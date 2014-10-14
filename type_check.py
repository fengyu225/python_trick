import inspect
from functools import wraps

def type_check(*type_args,**type_kwargs):
    def dec(func):
        types_args = inspect.getcallargs(type_check,*type_args,**type_kwargs)

        @wraps(func)
        def new_func(*args,**kwargs):
            val_args = inspect.getcallargs(new_func,*args,**kwargs)
            for i,x in enumerate(types_args['type_args']):
                if not isinstance(val_args['args'][i],x):
                    raise Exception("Type not match: {0} is not type {1}".format(val_args['args'][i],x))
            for k in types_args['type_kwargs']:
                if not isinstance(val_args['kwargs'][k], types_args['type_kwargs'][k]):
                    raise Exception("Type not match: {0} is not type {1}".format(val_args['kwargs'][k], types_args['type_kwargs'][k]))
            return func(*args,**kwargs)
        return new_func
    return dec

@type_check(float,x=list)
def f(a,b,x=[1,2],y=(3,)):
    return sum([a,b,x[0],y[0]])

print f(1,2.0,x=[3],y=(4,))
