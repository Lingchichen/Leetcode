"""
Q5
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
dabab
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: "cbbd"
Output: "bb"
"""

"""
compare origin and reverse

babad
dabab

cbbd
dbbc
"""
def palindromic_sub(s):
    reverse_s=s[::-1]
    print(reverse_s)
    longest=""
    j=0
    validate=False
    if s == reverse_s:
        return s
    else:
        for j in range(len(s)-1):
            temp=""
            for i in range(j,len(s)):
                temp+=s[i]
                print("temp",temp)
                if len(temp)==1:
                    validate=True
                else:
                    for l in range(len(temp)//2):
                        if temp[l]==temp[-1-l]:
                            validate=True
                        else:
                            validate=False
                            break
                if temp in reverse_s and validate and len(temp) >=len(longest):
                    longest=temp
                    print("longest",longest)
    return longest


s="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
palindromic_sub(s)
