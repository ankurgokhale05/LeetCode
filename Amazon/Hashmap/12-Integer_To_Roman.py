'''
Method
Use a hashmap with values of roman letters as keys and their value as value in descending order of their value. After doing that we need to iterate over the keys and if value of num is greater than dict[key] then add corresponding character to empty string and remove the key from num. Keep doing that.

Time Complexity: It depends on number of digits within a number 
Space Complexity: Depends on how many different numbers as keys to be considered
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I' 
        }
        roman = ''
        for key in dict:
            while num >= key:
                roman += dict[key]
                num -= key
        return roman
    
    
                
        
    
        