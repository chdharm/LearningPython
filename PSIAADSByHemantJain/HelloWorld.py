class HelloWorld(object):
    @classmethod
    def main(cls,args):
        print "Hello World!"

if __name__=='__main__':
    import sys
    HelloWorld.main(sys.argv)