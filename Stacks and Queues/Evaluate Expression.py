class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        
        def add(a,b):
            return a+b
        def sub(a,b):
            return b-a
        def mult(a,b):
            return a*b
        def divide(a,b):
            return b//a
            
        store = {
            "+": add,
            "-": sub,
            "*": mult,
            "/": divide
        }
        
        li = []
        for i in A:
            if i not in store:
                li.append(int(i))
            else:
                a,b = li.pop(),li.pop()
                li.append(store[i](a,b))
        return li[0]
