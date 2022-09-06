

# function to sum Fib sequence
def calculateFib(n) :
    if (n <= 0) :
        return 0
  
    seq =[0] * (n+1)
    seq[1] = 1
  
    # Initialize result
    sum = seq[0] + seq[1]
  
    # Add remaining terms
    for i in range(2,n+1) :
        seq[i] = seq[i-1] + seq[i-2]
        sum = sum + seq[i]
         
    return sum
 
n =50
print("Sum of first 50 Fibonacci numbers is : " ,
      calculateFib(n))