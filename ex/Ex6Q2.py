class Student:
    def __init__(self):
        pass
    def SetRollNo(self):
        self.roll = input("Enter your roll number: ")
        
    def SetMarks(self, n1, n2, n3, n4):
        self.marks1 = n1
        self.marks2 = n2
        self.marks3 = n3
        self.marks4 = n4
    
    def GetInfo(self):
        print(self.roll)
        print(self.marks1)
        print(self.marks2)
        print(self.marks3)
        print(self.marks4)

        
    def CalculateResult(self):
        self.result = (self.marks1 + self.marks2 + self.marks3 + self.marks4)
        self.percentage = (self.result/4)
        print(self.result)
        print(self.percentage)
        
Student1 = Student()
Student1.SetRollNo()
Student1.SetMarks(50, 50, 50, 50)
Student1.GetInfo()
Student1.CalculateResult()
