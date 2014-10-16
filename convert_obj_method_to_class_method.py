import inspect
import functools

class convert_method_metaclass(type):
    def __new__(self,name,objs,dic):
        for e in dic:
            if inspect.isfunction(dic[e]) and not e.startswith("__"):
                dic[e] = functools.partial(dic[e],self=None)
        return type.__new__(self,name,objs,dic)

class Test(object):
    __metaclass__ = convert_method_metaclass
    def __init__(self):
        self.x = 1
    def func(*args,**kwargs):
        print "in func"
        #print self,a,b
        print args
        print kwargs

t = Test()
Test.func(2)
