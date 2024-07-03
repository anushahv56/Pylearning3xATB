#Multiple inheriatnce
class father:
    def father_money(self):
        return "5"
    def home(self):
        return "father home"
class mother:
    def mother_money(self):
        return "2"
    def home(self):
        return "mother home"
class son(father,mother):

    def home(self):
        return "son home"
son_obj=son()
son_obj.mother_money()
son_obj.father_money()
print(son_obj.home())