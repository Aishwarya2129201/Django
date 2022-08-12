class Solution:

    def caseSort(self,s,n):
        ss = [i for i in s]
        str1 = []
        str2 = []
        
        for i in range(n):
            if ss[i]>='a' and ss[i]<='z':
                str1.append(ss[i])
            elif ss[i]>='A' and ss[i]<='Z':
                str2.append(ss[i])
                
        str1.sort()
        str2 = sorted(str2)
        
        i = 0
        j = 0
        for k in range(n):
            if ss[k]>='a' and ss[k]<='z':
                ss[k] = str1[i]
                i += 1
            elif ss[k]>='A' and ss[k]<='Z':
                ss[k] = str2[j]
                j += 1
        
        return "".join(ss)

if __name__ = __main__:
  t = int(input())
  for tt in range(t):
    n = int(input())
    s = str(input())
    print(Solution().caseSort(s,n))
