class Solution:
    def closeStrings(self, word1, word2):
        if set(word1) != set(word2):
            return False
        freq1 = sorted([word1.count(char) for char in set(word1)])
        freq2 = sorted([word2.count(char) for char in set(word2)])

        return freq1 == freq2

sol=Solution()
word1 = "abc"
word2 = "bca"
print(sol.closeStrings(word1,word2))
'''
Time Complexity:
    Creating the sets: O(n+m), where n is the length of word1 and m is the length of word2.
    Counting character frequencies: O(nk1+mk2), where k1 and k2 are the number of unique characters in word1 and word2, respectively.
    
    Sorting the frequencies: O(k1logk1+k2logk2).
    Overall complexity: O(n+m+nk1+mk2+k1logk1+k2logk2), which is efficient for typical input sizes.
Space Complexity:
The set and sorted operations require space proportional to the number of unique characters, making the space complexity 
O(k1+k2).
'''