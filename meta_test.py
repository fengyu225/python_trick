class meta(type):
#        def __new__(self,*args):
#                print args
#                super(meta,self).__new__(args)
        def __init__(self,*args):
                print "__init__"
                for i in args:
                    print i
                super(meta,self).__init__(args)
#        def __call__(self,*args):
#                raise Exception("error")

class Test(object):
    __metaclass__ = meta
    def func(self):
        print "func"
    @classmethod
    def class_func(cls):
        print cls
        print "class func"
    @staticmethod
    def static_method(*args):
        print args
        print "static func"

t = Test()
#Test.static_method()
#Test.class_func()
