# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x_list=str(x)
#         x_list=list(x_list)
#         x_list_backwards=[]
#         i=len(x_list)-1
#         while i>=0:
#             x_list_backwards.append(x_list[i])
#             i-=1
#         print(x_list_backwards)
#         if x_list==x_list_backwards:
#             palindrome=True
#         else:
#             palindrome=False
#         return palindrome

# solution1=Solution()

# print(solution1.isPalindrome(121))

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix_list=[]
        most_frequent_prefix=""
        frequency=1
        for word in strs:
            if len(word)>1:
                prefix_list.append(word[0]+word[1])
            else:
                prefix_list.append(word[0])
        print(prefix_list)

        for prefix in prefix_list:
            counter=prefix_list.count(prefix)
            if counter>frequency:
                frequency=counter
                most_frequent_prefix=prefix
        
        # return most_frequent_prefix

solution1=Solution()

print(solution1.longestCommonPrefix(["a"]))