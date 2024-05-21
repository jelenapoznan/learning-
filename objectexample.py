class Human:
  def __init__(self, n, o):
    self.name = n
    self.occupation = o

  def do_work(self): # Method
    if self.occupation == "teniss player":
      print(self.name, "plays tenis")
    elif self.occupation == "actor":
      print(self.name, "shoots film")

  def speaks(self):
    print(self.name, "says how are you")

tom = Human("Tom Cruse", "actor") # Creating object. tom is object == tom is self
tom.do_work()
tom.speaks()

maria = Human("Maria", "teniss player") 
maria.do_work()
maria.speaks
