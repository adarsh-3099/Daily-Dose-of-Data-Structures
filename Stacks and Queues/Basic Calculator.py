class Solution:
    def calculate(self, s: str) -> int:
        
        res, num, sign, st = 0, 0, 1, []
        
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i in ["-","+"]:
                res = res + sign*num
                num = 0
                if i == "+":
                    sign = 1
                else:
                    sign = -1
            elif i == "(":
                st.append(res)
                st.append(sign)
                sign = 1
                res = 0
            elif i == ")":
                res += sign*num
                res *= st.pop()
                res += st.pop()
                num = 0
                
        return res+num*sign