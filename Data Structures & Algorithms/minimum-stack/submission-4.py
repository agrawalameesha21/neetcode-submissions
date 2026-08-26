class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            num = val
            for index, n in enumerate(self.min_stack):
               if n > num: 
                temp = self.min_stack[index]
                self.min_stack[index] = num
                num = temp
            self.min_stack.append(num)
        
    def pop(self) -> None:
        val = self.top()
        self.stack.pop()
        for index, n in enumerate(self.min_stack):
            if n == val: 
                del self.min_stack[index]
                break


    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min_stack[0]
        # min = self.stack[0]
        # for n in self.stack:
        #     if n < min: min = n
        # return min
        
