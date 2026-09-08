class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for elem in tokens:
            if elem == "+" or elem == "-" or elem ==  "*" or elem == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                if elem == '+':
                    stack.append(num1+num2)
                if elem == '-':
                    stack.append(num1-num2)
                if elem == '*':
                    stack.append(num1*num2)
                if elem == '/':
                    stack.append(math.trunc(num1/num2))
            else:
                stack.append(int(elem))

        if stack:
            return stack.pop()
        return 0
