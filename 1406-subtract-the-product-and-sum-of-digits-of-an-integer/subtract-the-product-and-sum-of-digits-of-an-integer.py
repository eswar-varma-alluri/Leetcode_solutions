class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_digits = 1
        sum_digits = 0
        
        while n > 0:
            digit = n % 10
            product_digits *= digit
            sum_digits += digit
            n //= 10
            
        return product_digits - sum_digits