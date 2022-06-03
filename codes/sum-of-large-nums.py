
def AddNumbers(num1, num2):

    #length of str2 is larger.
    if len(num1) > len(num2):
        temp = num1
        num1 = num2
        num2 = temp
  
    # Final result will be stored in this variable
    total_sum = ""
  
    # the length of both numbers (strings)
    n1 = len(num1)
    n2 = len(num2)
    diff = n2 - n1
  
    #carry on
    carry = 0
  
    # Traverse from the units place to add the two numbers
    for i in range(n1 - 1, -1, -1):
       
        temp_sum = ((ord(num1[i]) - ord('0')) + int((ord(num2[i+diff]) - ord('0'))) + carry)
      
        total_sum += str(temp_sum % 10)
         
        
        carry = temp_sum // 10
  
    # Add remaining digits of larger number num2 with carry

    for i in range(n2-n1-1, -1, -1):
     
        temp_sum = ((ord(num2[i])-ord('0')) + carry)
        total_sum += str(temp_sum % 10)
        carry = temp_sum // 10
  
    # Add remaining carry
    if (carry):
        total_sum + str(carry+'0')
  
    # reverse the final sum
    total_sum = total_sum[::-1]
  
    return total_sum
  
# Driver code
if __name__ == "__main__":
    num1 = "11"
    num2 = "198111"
    print(AddNumbers(num1, num2))
