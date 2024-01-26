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

#This function was written by Sahar Farzanehpour.
#IDE used : Xcode.
#This function converts a roman numeral to Integer value.
#It iterates through the input string, adding the values of each Roman numeral or subtracting when necessary, and returns the overall integer representation.
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans
