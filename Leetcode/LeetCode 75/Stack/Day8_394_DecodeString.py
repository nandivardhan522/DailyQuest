class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if(char=="]"):
                stri=""
                while(True):
                    dele=stack.pop()
                    if(dele == "["):
                        n=""
                        while(stack and stack[-1].isdigit()):
                            n=stack.pop()+n
                        stri=int(n)*stri
                        for i in stri:
                            stack.append(i)
                        break
                    stri=dele+stri
            else:
                stack.append(char)
        return ''.join(stack)

s = "3[a]2[bc]"
sol=Solution()
print(sol.decodeString(s))

'''
Time Complexity:
    Iteration over the string: Each character is processed once. This takes O(n).
    Stack Operations: Appending and popping from the stack are O(1) operations.
    In the worst case, the stack operations involve copying strings for nested encodings. 
    This results in a time complexity of O(n × max_k), where max_k is the maximum repeat count.
Space Complexity:
    The stack stores all characters and partially decoded strings. The space complexity is O(n).
'''