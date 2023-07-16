name=str(input("enter the name of  employee"))
salary=int(input ("enter the salary of  employee {unit} Rs"))
time= int(input("length of service of employee {unit} Yrs "))
if (time>10):
   bonus =(10/100*salary)
   print(f'your bonus is {bonus}rs')

elif (time>=6<10):
  bonus =(5/100*salary)
  print(f'your bonus is {bonus}rs')
  
elif (time<6):
  bonus =(3/100*salary)
  print(f'your bonus is {bonus}rs')
print(f'your total montly salary including bonus is {salary+ bonus}Rs')
print (f'your total annual salary including bonus {salary*12+bonus}Rs')



       
       




