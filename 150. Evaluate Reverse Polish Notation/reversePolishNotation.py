class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i in op:
                x = stack.pop()
                y = stack.pop()
                if i == "+":
                    z = x + y
                elif i == "-":
                    z = y - x
                elif i == "*":
                    z = x * y
                elif i == "/":
                    z = int(y/x)
                stack.append(z)
                #print(x,i,y,z)
            else:
                stack.append(int(i))
            #print(stack)
        return stack[0]
