class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        stck = []
        m = {'(':')','[':']','{':'}'}
        max_c = 0
        count = 0
        for i in s:
            print(i)
            if i == '(' or i == '[' or i == '{':
                stck.append(m[i])
            else:
                k = stck.pop()
                if k != i:
                    stck = []
                    if count > max_c:
                        max_c = count
                    else:
                        count = 0
                else:
                    count = count+1
            print(stck)
                
        if len(stck) == 0:
            return True
        return False
        
s = Solution()
print(s.isValid("()"))