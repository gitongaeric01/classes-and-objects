class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
     self.name = name
     self.age = age
     self.tracks = tracks
     self.score = score

    def change_name(self):
      new_name = str (input("Please enter student name: "))
      Bob.name = new_name 
        #print(self.name)

    def change_age(self):
     while True:
       new_age = input("Please enter student age: ")
       if new_age.isdigit():
           new_age=int(new_age)
           Bob.age = new_age 
           break
       else:
          print("You have not entered an integer.Please repeat with an integer entry")
       
    def add_track(self):
     new_track = str (input("Please enter student track: "))
     Bob.tracks = new_track

    def get_score(self):
     new_score= float (input("Please enter student score: ") )      
     Bob.score = new_score
     return Bob.score
    
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

Bob.change_name()
Bob.change_age()
Bob.add_track()
Bob.get_score()

print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)


"""
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
"""

