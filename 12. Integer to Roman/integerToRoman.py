class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        if num>=1000:
            rem = num//1000
            roman += "M" * rem
            num = num%1000
        if num>=900:
                roman += "CM"
                num = num%900
        if num>=500:
            rem = num//500
            roman += "D" * rem
            num = num%500
        if num>=400:
                roman += "CD"
                num = num%400
        if num>=100:
            rem = num//100
            roman += "C" * rem
            num = num%100
        if num>=90:
                roman += "XC"
                num = num%90
        if num>=50:
            rem = num//50
            roman += "L" * rem
            num = num%50
        if num>=40:
                roman += "XL"
                num = num%40
        if num>=10:
            rem = num//10
            roman += "X" * rem
            num = num%10
        if num>=9:
                roman += "IX"
                num = num%9
        if num>=5:
            rem = num//5
            roman += "V" * rem
            num = num%5
        if num>=4:
                roman += "IV"
                num = num%4
        roman += "I" * num
        return roman
            
