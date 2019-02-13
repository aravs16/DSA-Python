class Solution:
    def longestValidParentheses(self, s):
        stck = [-1]
        result = 0
        for i in range(len(s)):
            
            if s[i] == '(':
                stck.append(i)
            else:
                stck.pop() # Matching one
                if len(stck) != 0:           
                    result = max(result, i-stck[-1])
                elif len(stck) == 0 :
                    stck.append(i)
            print(stck,result)
                
        if stck == [-1]:
            result = len(s)
        
        return result
        
s = Solution()
print(s.longestValidParentheses("(()))"))

#(()(()(()))

# (  (  )  (  (  )  (  (  )  ) ) )