class Car:
    name=None
    make=None
    model=None
    def __init__(self,o_name,o_make,o_model):
        self.name=o_name
        self.make=o_make
        self.model=o_model
    def start_engine(self):
        print("starting car with",self.name)
        print("starting car with",self.make)
        print("starting car with",self.model)
lambo=Car("lambo","v2",287)
lambo.start_engine()
xuv=Car("xuv name","w2",123)
xuv.start_engine()
