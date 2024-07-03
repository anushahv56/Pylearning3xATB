#Multilevel
class grandparent:
    gold="2kg"
    def grandparent_method(self):
        print("gp method")
class parent(grandparent):
    def parent_method(self):
        print("parent method")
class pramod(parent):


  def pramod_method(self):
      print("pramod method")
pramod_obj=pramod()
pramod_obj.pramod_method()
pramod_obj.grandparent_method()
pramod_obj.parent_method()
pramod_obj.gold

grandparent_obj=grandparent()
grandparent_obj.grandparent_method()
grandparent_obj.gold