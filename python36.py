def plusOne(digits):
    n = len(digits)
    
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    return [1] + digits


digits1 = [1,2,3]
digits2 = [4,3,2,1]
digits3 = [9]

print(
    "Output:", plusOne(digits1),
    "\nOutput:", plusOne(digits2),
    "\nOutput:", plusOne(digits3)
)