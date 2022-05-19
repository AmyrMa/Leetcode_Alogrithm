#Given a string s, find the length of the longest substring without repeating characters.
#Approach 1: Brute Force: check method enumerate all substring, and use check function to see if there is any duplicates
#run time is O(n^3)
Class Solution:
    def lengthoflongestsubstring(self, s:str)->int:
        def check(start, end):
            chars = [0] * 128 # direct access table用来计数是否有重复的char, s consists of English letters, digits, symbols and spaces. 所以为128
            for i in range(start, end+1): #enumerate all substring
                current = s[i]
                chars[ord(current)] += 1  #ord用来把char 转换成unicode
                if chars[ord(current)]> 1:
                         return False
            return True
        
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i,j):
                    res = max(res, j - i + 1) #检查目前合适的substring 和之前的结果 哪儿个长度更长
        return res 
   #Approach 2: Sliding window 限制左右的boundry, 然后平移, 这样减少run time 和重复enumerate
Class Solution:
    def lengthoflongestsubstring(self,s:str)->int:
        chars = [0] * 128 #同理, 用unicode 计数是否有重复的char
        left = right = 0 #先设置左右bound 都为0 
        
        res = 0 
        while right < len(s):           #首先设置right pointer expand 的条件, 
            r = s[right]                #记录right pointer的值出现次数
            chars[ord(r)] += 1
            while chars[ord(r)] > 1:    #然后设置left pointer contract的条件:当rp的值出现超过一次,
                l = s[left]             #记录下lp的值, 并从chars里面删除, 因为这个值不在我们的substring里面了
                chars[ord(l)] -=1
                left += 1               #并将lp加一, 用来contract window
            res = max(res, right - left + 1)

            right += 1                  #继续expand rp
        return res
