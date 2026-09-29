class Hospital:
    def __init__(self):
        self.name=input("name:")
        self.location=input("location:")
        self.phone=int(input("phone no:"))

    def display_hospital(self):
        print(self.name,self.location,self.phone)
class Department:
    def __init__(self):
        self.dept_name=input("dept name=")
        self.doctorname=input("doctor name=")

    def dislpay_department(self):
        print(self.dept_name,self.doctorname)
class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patientname=input("patient name=")
        self.age=int(input("age="))
        self.gender=input("gender=")
        self.admission_date=input("admission date=")
        self.bedno=int(input("bed no="))
        self.discharge_date=" "

    def set_discharge(self):
        self.discharge_date=input("updated discharge date=")

    def full_summary(self):
        Hospital.display_hospital(self)
        Department.dislpay_department(self)
        print("name=",self.patientname,"age=",self.age,"gender=",self.gender)
        print("bedno=",self.bedno,"admission_date=",self.admission_date)
        if self.discharge_date=="":
            print("not yet discharged")
        else:
            print("discharge date=",self.discharge_date)
p=Patient()
p.set_discharge()
p.full_summary()
  
