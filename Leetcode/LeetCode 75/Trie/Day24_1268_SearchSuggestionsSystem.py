class Solution:
    def suggestedProducts(self, products, searchWord: str):
        res=[]
        products.sort()
        temp=""
        for i in range(0,len(searchWord)):
            temp+=searchWord[i]
            temp_res=[]
            for j in range(len(products)):
                if products[j].startswith(temp):
                    temp_res.append(products[j])
                if(len(temp_res)==3):
                    break

            res.append(temp_res)

        return res

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

Solution = Solution()
print(Solution.suggestedProducts(products,searchWord))

'''
Time Complexity Analysis
Sorting Step:
products.sort() sorts the list lexicographically.
Sorting takes O(N log N), where N is the number of products.
Prefix Matching:
The function iterates through each character of searchWord (let's say M is its length).
For each prefix, it scans through the product list (at worst, all N products) to find at most three matches.
In the worst case (if no early stopping), this takes O(M * N).
Overall Complexity:
Sorting: O(N log N)
Prefix Matching: O(M * N)
Total Worst-Case Complexity: O(N log N + M * N)
Since M (length of searchWord) is generally small compared to N, the dominant term is usually O(N log N).
Space Complexity Analysis
Sorting is done in-place, so no extra space is used there.
res stores M lists, each containing at most 3 elements, leading to O(M * 3) = O(M).
Other temporary variables (like temp and temp_res) use negligible extra space.
Overall Space Complexity: O(M) (excluding input storage).
'''