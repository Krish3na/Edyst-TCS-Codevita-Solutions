'''

European Iteration
We know about number systems: The Roman numerals and the alternative place-value system with a given base.

For the purposes of this problem, we limit ourselves to

Roman numerals with values up to 3999 MMMCMXCIX
"Place value system" numbers having bases from 2 (with possible symbols 0, 1) through 36 (with possible symbols 0, 1, ..., 9, A, ... ,Z)
Consider the following procedure:

Accept a natural number N (in base 10).
If N lies in the closed interval [1,3999], i.e. between 1 and 3999 (both inclusive), convert N to R, its Roman numeral representation; else output N as the result and stop.
Identify the base in which the value of R, now considered to be in "place value system", is least and calculate its value in base 10, replacing N with this value.
Repeat from step 2.
Constraints
1 <= N <= 3999

Input Format
A single Integer N.
Output
Converted N
Test Case
Example Input
1
Output
45338950
Explanation
The procedure goes as follows in this case:

Accept N = 1.
Since 1 lies in [1,3999], covert it to Roman R = I
The least value of I (in bases 19 and above) is 18 in base 10. Hence N = 18.
Repeating step 2, since 18 lies in [1,3999], convert it to R = XVIII
The least value of XVIII (in base 34) is
33*34^4+31*34^3+18*34^2+18*34+18 or N = 45338950
Repeating step 2, since 45338950 lies outside [1,3999] output 45338950 and stop.
Here's how the conversions go:

Input = 1 => I => 18 => XVIII => 45338950 = Output
'''


def toRomanNum(num):
    val_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_num = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num_ret = ""
    i = 0
    while num > 0:
            for _ in range(num // val_num[i]):
                roman_num_ret = roman_num_ret + roman_num[i]
                num = num - val_num[i]
            i = i + 1
    return roman_num_ret

def roman_to_Base10_adjusted(num):
    
    if "X" in num :
        base = 34
    elif "V" in num :
        base = 32
    elif "M" in num :
        base = 23
    elif "L" in num :
        base = 22
    elif "I" in num :
        base = 19
    elif "D" in num :
        base = 14
    elif "C" in num :
        base = 13

    roman_to_base_dict = {"C":12, "D":13, "I":18, "L":21, "M":22, "V":31, "X":33}
    
    temp_num = num[::-1]
    #print(temp_num)
    sum = 0
    for i in range(len(num)):
        sum = sum + roman_to_base_dict[temp_num[i]]*(base**i)
        #print(sum)
    
    return sum


def toRNLoop(num):
    roman_num = toRomanNum(num)
    new_num = roman_to_Base10_adjusted(roman_num)
    #print(roman_num,new_num)
    while new_num < 3999 :
        roman_num = toRomanNum(new_num)
        new_num = roman_to_Base10_adjusted(roman_num)
        #print(roman_num,new_num)

    return new_num


try:
    num = int(input())
    if num < 4000 and num > 0 :
        print(str(toRNLoop(num)))
    elif num > 3999:
        print(num)
    else:
        raise "Non-Positive Number"
except Exception as ex:
    print(ex)
