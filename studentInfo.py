#import os
#os.chdir('G:/PYTHON/demo')
#print(os.listdir())
#os.mkdir('demo')
#print(os.listdir())
#os.chdir('G:/PYTHON/demo/')
#f = open('begin.txt', 'w')
#s = input('enter story')
#f.write(s)
#f.close()
#f = open('begin.txt', 'r')
#print(f.read())

#f=open('end.txt', 'w')
#f.write('go to hell')

#print(os.listdir())
#f = open('customerData.txt', 'w')
#s = input('enter customer info:')
#f.write(s)

#f = open('begin.txt', 'r')
#print(f.read())

#f = open('dates.txt', 'w')  

#Task --
# Create a text file that contains name, age, city, course, mobile
# define a funciton and iterate to store multiple users.
# load the inputs into the file.
# save file.


def student_info():
    file = open('studentData.txt', 'a')
    print("*** Student Form ***")
    name=input('enter student name: ')
    age= int(input('enter age: '))
    course = input('enter course: ')
    city = input('enter city: ')
    mobile = input('enter mobile number: ')

    file.write(f"Name:{name}\n Age:{age}\n Course:{course}\n City:{city}\n Mobile:{mobile}\n")
    file.close()

while True:
    student_info()
    choice = input("Do you want to continue?(Y/N)").upper()
    if choice == 'Y':
        print("Enter Student Details: ")
    else:
        #print("Program Terminated")
        break


