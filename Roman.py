# This function was written by Swetha Rajeev.
# IDE use: VS Code
# This function will convert an integer to a roman numeral
# version of it using a map too keep track of what each number represents.
# Then will loop through each digit of the given number and will convert 
# each digit to the roman version of it.
class Solution:
    def intToRoman(self, num: int) -> str:
    
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        
        r = ''
        
        
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:

            while n <= num:
                r += num_map[n]
                num-=n
        return r

