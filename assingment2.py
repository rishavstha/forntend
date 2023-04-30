# write a funtion that take a string as a parameter and returns wheather it is pallindrome or not.

def is_palindrome(string):
   reversed_string=""
   for i in range(len(string),0,-1):
      reversed_string+=string[i-1]
      if string==reversed_string:
         print("Palindrome")
      else:
         print("Not a palindrome")

# write a function to take a string as a parameter and replace the A character with with @ and S with $ and return the string.

#write a function that input an array and print the positive and negative number count.