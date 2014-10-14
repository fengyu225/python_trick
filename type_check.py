import inspect
from functools import wraps

def type_check(*type_args,**type_kwargs):
    def dec(func):
        types_args = inspect.getcallargs(type_check,*type_args,**type_kwargs)
        print types_args

        @wraps(func)
        def new_func(*args,**kwargs):
            val_args = inspect.getcallargs(new_func,*args,**kwargs)
            for i,x in enumerate(val_args['args']):
                if not isinstance(x, types_args['type_args'][i]):
                    raise Exception("Type not match: {0} is not type {1}".format(x,types_args['type_args'][i]))
            for k in val_args['kwargs']:
                if not isinstance(val_args['kwargs'][k], types_args['type_kwargs'][k]):
                    raise Exception("Type not match: {0} is not type {1}".format(val_args['kwargs'][k], types_args['type_kwargs'][k]))
            func(*args,**kwargs)
        return new_func
    return dec

@type_check(int,float,x=list,y=tuple)
def f(a,b,x=[1,2],y=(3,)):
    pass

f(1,2.0,x=3,y=(4,))
