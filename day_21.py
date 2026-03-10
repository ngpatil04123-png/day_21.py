print("Never Give up !!")
def sum_list(lst):                             # function that returns the sum of numbers in a list.
    sum=0
    for i in lst:
        sum+=i
    return sum
print(sum_list([1,2,3,4,5,6,6]))
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def largest():                           # function that takes two numbers and returns the largest number.
    a=int(input("Enter the a value : "))
    b=int(input("Enter the b vaiue : "))
    if a > b:
        return a
    else:
        return b

print(f"The largest number is :  {largest()}")


def smallest():                            # function that takes two numbers and returns the smallest number.
  p=int(input("Enter the p value : "))
  q=int(input("Enter the q value : "))
  if p<q:
    return p
  else:
    return q
print(f"The smallest number is :{smallest()}")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def vowel():                     #function that counts vowels in a given string.
   string=str(input("Enter the string : "))
   count=0
   vowels="aeiou"
   for i in string:
      if i.lower() in vowels:
         count+=1
         print(f" vowel is : {i}")
   return count
print(f"The vowel count is : {vowel()}")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def palindrome():                              # function that checks whether a string is a palindrome.                      
    string=str(input(" Enter the string to check palindrome or not : "))
    if string == string[::-1]:
        return "palindrome : Entered string is palindrome "
    else:
        return " not a palindrome :  Entered string is not palindrome" 
print(palindrome())
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def factorial():                       # Factorial Using Function
    n = int(input(" Enter the n value : "))
    fact=1
    for i in range(1,n+1):
      fact= fact * i
    print(f" The factorial is : {fact}")
factorial()
------------------------------------------------------------------------------------------------------------------------------------------------------------
def re():                       # Factorial Using Function
    n = str(input(" Enter the string value : "))
    rev=""
    for i in n:
      rev= i + rev
    print(f" The reversed is : {rev}")
re()

         

      
