import mysql.connector as c
from mysql.connector import Error

con  = c.connect(host='db4free.net',
                database='car_wash',
                user='jeevan_reddy',
                passwd='Jeevan@123')
if not(con.is_connected()):
    print('Unknown error occured. Please try again later. ')

cursor = con.cursor()
def homepage():
  choice = int(input('1. New User Registration\n2. LOGIN as USER\n3. LOGIN as ADMIN\nChoose Your Action:'))
  return choice
  
print("*"*110)
print(" "*25,'MOBILE CAR WASH')
print("*"*110)


while True :
  choice = int(input('1. New User Registration\n2. LOGIN as USER\n3. LOGIN as ADMIN\n4. Exit\nChoose Your Action:'))
  if choice ==  1 :
    name = input('\nEnter Your Name: ')
    mail = input("Enter Your Email: ")
    password = 1
    pass2 = 0
    while password != pass2:
      password = input("Enter a password: ")
      pass2 = input('Re-enter your password: ')
      if password != pass2 :
        print('\nBoth passwords should match !!\n')
    query = f"insert into login(name,Email,password) values('{name}','{mail}','{password}')"
    cursor.execute(query)
    con.commit()
    print("\nYour Account is Successfully Created.\n")
    print("*"*110)
    
    
  elif choice == 4 :
    print("\nYou chose to exit. Thank You.\n️")
    print('*'*110)
    break
  

  elif choice == 2 :
    check = 0
    carwashcentres = 0
    while not(check):
      mail = input('Enter your Email: ')
      password = input("Enter Your Password: ")
      query = f"select ld.userid from login as ld where ld.Email = '{mail}' and ld.Password = '{password}'  and ld.role='user' "
      cursor.execute(query)
      check = cursor.fetchone()
      if check : 
        print('Welcome! You are loggged in now.\n')
        break
      else :
        print("\nPlease enter valid Email and Password !!\n")
        continue
      
      
  elif choice == 3 :
    check = 0
    carwashcentres = 0
    while not(check):
      mail = input('Enter your Email: ')
      password = input("Enter Your Password: ")
      query = f"select ld.userid from login as ld where ld.Email = '{mail}' and ld.Password = '{password}'  and ld.role='admin' "
      cursor.execute(query)
      check = cursor.fetchone()
      if check : 
        print('Welcome Admin! You are logged in now.\n')
        break
      else :
        print("\nPlease enter valid Email and Password !!\n")
        continue