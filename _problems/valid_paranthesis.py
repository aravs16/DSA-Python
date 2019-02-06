class Solution:
    def isValid(self, s):
        stck = []
        m = {'(':')','[':']','{':'}'}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stck.append(m[i])
            else:
                if len(stck) == 0:
                    return False
                k = stck.pop()
                if k != i:
                    return False
                
        if len(stck) == 0:
            return True
        return False

s = Solution()
print(s.isValid("()"))