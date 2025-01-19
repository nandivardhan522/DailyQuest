class Solution:
    def compress(self, chars):
        write = 0  # Pointer to write the compressed string
        i = 0  # Pointer to traverse the input list
        while i < len(chars):
            char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1

            # Write the character to the array
            chars[write] = char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write
sol=Solution()
chars = ["a","a","b","b","c","c","c"]
print(chars[:sol.compress(chars)])
'''
Time Complexity:
    The overall time complexity is O(n).
Space Complexity
The solution operates in place, so the space complexity is O(1).
'''