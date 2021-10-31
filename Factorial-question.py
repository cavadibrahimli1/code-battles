def FirstFactorial(num):
  if num == 1:
        return num
  else:        
        factorial = num*FirstFactorial(num-1)    
        return factorial
  

  # code goes here
  return num

# keep this function call here 
print(FirstFactorial(input()))
