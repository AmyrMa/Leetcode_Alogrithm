'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
'''
# Appraoch 1: 
class Solution:
    def convert(self, s: str, numRows: int) -> str:
                                                        #设置empty string array 用来储存每行的字母
        row = ['']*numRows                              # numrows= 3, row =['','','']
        current=1                                       # 记录目前的row number
        
        if numRows < 2:                                 # 如果只有一个row 直接return
            return s
        
        
        for i in s:                                     # 从左到右循环string s
            row[current-1] = row[current-1] + i         # row里面的empty string加上现在的i
            if current == 1:                            # 当current 到第一行和最后一行的时候,变换方向
                direction = 1                           # direction 的1 代表向下, +1, -1 代表向上挪动
            elif current == numRows:
                direction = -1
            current = current + direction 
            
        
        res =''                                         # 把string 加在一起
        for string in row:
            res = res + string
        return res
            
        
