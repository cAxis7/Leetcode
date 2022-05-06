# Remove Digit From Number to Maximize Result
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        prev = -1
        for i in range(len(number)):
            if number[i] == digit:
                if i + 1 == len(number) or digit < number[i + 1]:
                    return number[:i] + number[i+1:]
                prev = i
        
        return number[:prev] + number[prev+1:]
