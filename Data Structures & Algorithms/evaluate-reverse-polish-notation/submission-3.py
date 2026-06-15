class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for data in tokens:
            if data == '+':
                stack.append(stack.pop() + stack.pop())
            elif data == '-':
                b= stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif data == "*":
                stack.append(stack.pop() *  stack.pop())
            elif data == "/":
                b= stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(data))

        return stack.pop()
            
                



        