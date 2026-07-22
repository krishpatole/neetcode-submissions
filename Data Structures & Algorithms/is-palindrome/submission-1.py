class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        copy_s=s
        reverse_s=s[::-1]#Ite reverse sathu slicing use kela ahe 
        if(copy_s==reverse_s):
             return True
        else:
            return False