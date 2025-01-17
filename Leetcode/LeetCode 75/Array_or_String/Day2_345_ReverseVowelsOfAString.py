class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert the input string to a character array.
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"
        while start < end:
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            while start < end and vowels.find(word[end]) == -1:
                end -= 1
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        return "".join(word)
sol=Solution()
s = "IceCreAm"
print(sol.reverseVowels(s))
'''
Complexity Analysis:
    Time Complexity:
        The algorithm iterates through the string once, checking and swapping vowels using two pointers.
        The membership check for vowels (O(1)) is performed using a set lookup.
        O(n)
    Space Complexity:
        The algorithm uses additional space for:
            The list conversion of the string (O(n)).
            A fixed set of vowels (O(1))
            O(n)
'''