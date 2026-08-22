Order_Amt=int(input("enter order amount : "))
Del_Dist=int(input("Enter delivery Distance : "))
Cust_Type=input("Enter Customer Type (frequent/normal): ")
Cust_Rating=int(input("Enter Customer Rating : "))
Rest_Rating=int(input("Enter Restaurant rating : "))
Prep_Time=int(input("Enter prepartion Time : "))
Pay_method=input("Enter Payment Method (prepaid/Cod): ")
Weather_Cond=input("Enter the Weather Condition (Rain or Normal) : ")
Demand_Lvl=input("Enter Demand Level (High/Low): ")
Peak_Hour_Status=input("Enter peak hour status : ")
Prev_Cancel=int(input("Enter PRevious Cancellation : "))

if(Order_Amt<50):
    Order_Status="Rejected"
elif(Del_Dist>30):
    Order_Status="Rejected"
elif(Cust_Rating<2 or Rest_Rating<2):
    Order_Status="Rejected"
elif(Prev_Cancel>=7):
    Order_Status="Rejected"
elif(Weather_Cond=="Rain" or Demand_Lvl=="High" or Peak_Hour_Status=="yes" or Prep_Time>50):
    Order_Status="Manual review"
else:
    Order_Status="Accepted"


if(Del_Dist<=5):
    Del_Charges=20
elif(Del_Dist<=10):
    Del_Charges=40
elif(Del_Dist<=20):
    Del_Charges=60
else:
    Del_Charges=100


if(Order_Amt>1000):
    Discount=150
elif(Order_Amt>500 and Cust_Type=="frequent" and Pay_method=="prepaid"):
    Discount=75
else:
    Discount=0


if(Cust_Type=="frequent" and Peak_Hour_Status=="yes"):
    Priority="High"
else:
    Priority="Normal"


if(Prev_Cancel>=5):
    Cancel_Risk="High"
elif(Prev_Cancel>=3 and Prev_Cancel<5):
    Cancel_Risk="Medium"
else:
    Cancel_Risk="Low"


if(Prep_Time>50 or Rest_Rating<=3):
    Rest_Status="Delayed"
elif(Demand_Lvl=="High" and Prep_Time>30):
    Rest_Status="Busy"
else:
    Rest_Status="Normal"


if(Order_Status=="Manual review"):
    Manual_Review="Yes"
else:
    Manual_Review="No"


if(Order_Status=="Rejected"):
    Final_Amount=0
elif(Order_Amt+Del_Charges-Discount<0):
    Final_Amount=0
else:
    Final_Amount=Order_Amt+Del_Charges-Discount


if(Order_Status=="Rejected"):
    Final_Category="Rejected"
elif(Order_Status=="Manual review"):
    Final_Category="Manual Review"
elif(Priority=="High"):
    Final_Category="Priority Delivery"
else:
    Final_Category="Normal Delivery"



print("Final Order Report")
print("Order Status : ",Order_Status)
print("Delivery Charges : ",Del_Charges)
print("Discount : ",Discount)
print("Priority Delivery Status : ",Priority)
print("Cancellation Risk : ",Cancel_Risk)
print("Restaurant Status : ",Rest_Status)
print("Manual Review Status : ",Manual_Review)
print("Final Order Category : ",Final_Category)
print("Final Payable Amount : ",Final_Amount)