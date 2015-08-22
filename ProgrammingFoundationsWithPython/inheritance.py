

class Parent():
    def __init__(self,last_name,eye_color):
        print ("Parent class called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("last Name - "+self.last_name)
        print ("Eye color - "+self.eye_color)
        

class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print ("Child constructor called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print ("last Name - "+self.last_name)
        print ("Eye color - "+self.eye_color)
        print ("Number of toys - "+str(self.number_of_toys))

#ram = Parent("golla","brown")

gam = Child("golla","blue",5)

print gam.show_info()
