"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==len(haystack):
            if needle == haystack:
                return 0
            else:
                return -1
        elif len(needle) > len(haystack):
            return -1
        else:
            if needle !="":
                if needle in haystack:
                    for i in range(len(haystack)):
                        print("new")
                        if needle[0]==haystack[i]:
                            for j in range(len(needle)):
                                print("hay",haystack[i+j],i+j)
                                print("needle",needle[j],j)
                                if haystack[i+j]==needle[j]:
                                    match=True
                                else:
                                    match=False
                                    break
                            if match==True:
                                return i
                    return -1
                else:
                    return -1
            else:
                return 0

            
