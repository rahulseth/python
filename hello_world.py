# install Package
import requests

# For reusability of status_code

if __name__ == '__main__':
    print("hello world")

    # Conditional statement
    num1 = 10
    num2 = 20
    if (num1 > num2):
        print("If clause block executed")
    else:
        print("Else clause block executed")

    # loop in Python
    while num1 < num2:
        print(num1)
        num1 = num1 + 10

# custom function
def mymatch():
   # input from user
   print("enter number between 10 to 50")
   mynum = input()
   mylist = [10, 20, 30, 40, 50]
   for x in mylist:
       if (x == mynum):
           print("number available")
           break;
       else:
           print("Looking")

mymatch()

# Request
res = requests.get('http://data.nasa.gov/resource/y77d-th95.json')
print(res.status_code)
#print(res.text)
print(res.json())
