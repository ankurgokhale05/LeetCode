'''
Given Tax brackets and percentage of tax calculate total tax on amount
45000
10000 * 0.1 = 1000
10000 * 0.2 = 2000
10000 * 0.3 = 3000
15000 * 0.4 = 6000
 = 12,000 


Time Complexity: O(1) or O(len(levels) = constant)
Space Complexity: O(1)

'''

def calculateTax(levels,salary):
    left = salary
    i = 0  # index on levels
    prev = 0
    tax = 0
    while left > 0:
        level = levels[i]
        percent = level[1]
        if level[0] == None:
            tax += left * percent
            return tax
        taxable_salary = min(left, level[0] - prev)
        tax += taxable_salary * percent
        left -= taxable_salary
        prev = level[0]
        i+= 1
    return tax
    
print(calculateTax([[10000, 0.1], [20000,0.2], [30000,0.3],[None, 0.4]], 45000))