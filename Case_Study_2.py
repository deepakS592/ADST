Pname=input("Enter your name : ")
n1=int(input("Enter number of requested department : "))
i=0
reqDepartment = []
while n1 != i:
    D = input(f"Enter the department {i+1} : ")
    reqDepartment.append(D)
    i += 1

n2=int(input("Enter number of available department : "))
i=0
availDepartment = []
while n2 != i:
    D = input(f"Enter the department {i+1} : ")
    availDepartment.append(D)
    i += 1
    
n3=int(input("Enter number of Previously visited department : "))
i=0
prevVisitedDep = []
while n3 != i:
    D = input(f"Enter the department {i+1} : ")
    prevVisitedDep.append(D)
    i += 1
    
n4=int(input("Enter number of Prefered Doctor : "))
i=0
PreferDoctor = []
while n4 != i:
    D = input(f"Enter the Doctor {i+1} : ")
    PreferDoctor.append(D)
    i += 1
    
n5=int(input("Enter number of Available Doctor : "))
i=0
AvailDoctor = []
while n5 != i:
    D = input(f"Enter the Doctor {i+1} : ")
    AvailDoctor.append(D)
    i += 1
    
n6=int(input("Enter number of Emergency Department : "))
i=0
EmerDepartment = []
while n6 != i:
    D = input(f"Enter the Department {i+1} : ")
    EmerDepartment.append(D)
    i += 1
    
reqDepartmentSet=set(reqDepartment)
availDepartmentSet=set(availDepartment)
prevVisitedDepSet=set(prevVisitedDep)
PreferDoctorSet=set(PreferDoctor)
AvailDoctorSet=set(AvailDoctor)
EmerDepartmentSet=set(EmerDepartment)

if len(reqDepartment)!=len(reqDepartmentSet):
    print("Duplicate department requested")
else:
    print("No duplicate department requested")
    
CommonDepartment=reqDepartmentSet.intersection(availDepartmentSet)
UnavailDepartment=reqDepartmentSet.difference(availDepartmentSet)
PreviouslyVisited=reqDepartmentSet.intersection(prevVisitedDepSet)
AvailablePreferredDoctor=PreferDoctorSet.intersection(AvailDoctorSet)
ReqImmediateAtten=reqDepartmentSet.intersection(EmerDepartmentSet)
AllDepartments=reqDepartmentSet.union(prevVisitedDepSet)

if len(ReqImmediateAtten)>0:
    RecommendedDepartment=list(ReqImmediateAtten)[0]
elif len(CommonDepartment)>0:
    RecommendedDepartment=list(CommonDepartment)[0]
else:
    RecommendedDepartment="No department Availavle"

if len(ReqImmediateAtten)>0:
    AppointmentStatus="Emergency appointment required"
elif len(CommonDepartment)>0:
    AppointmentStatus="Appointment can be scheduled"
else:
    AppointmentStatus="Appointment cannot be scheduled"
print("\n---------- FINAL APPOINTMENT REPORT -----------------")
print("Patient Name                   :",Pname)
print("Requested Departments          :",reqDepartment)
print("Available Departments          :",availDepartment)
print("Unavailable Departments        :",UnavailDepartment)
print("Common Departments             :",CommonDepartment)
print("Previously Visited Departments :",prevVisitedDep)
print("Emergency Departments          :",EmerDepartment)
print("Recommended Department         :",RecommendedDepartment)
print("Final Appointment Status       :",AppointmentStatus)