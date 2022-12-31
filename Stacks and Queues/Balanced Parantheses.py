class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        li = []
        for i in A:
            if i == "(":
                li.append("(")
            else:
                if li and li[-1] == "(":
                    li.pop()
                else:
                    li.append(")")

        if len(li) == 0:
            return 1
        return 0