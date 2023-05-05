class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []        

    def push(self, val: int) -> None:
        if len(self.min_stack)==0 or val<=self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = -1
        if self.stack:
            popped = self.stack.pop()
            if popped==self.min_stack[-1]:
                self.min_stack.pop()      
        return popped        

    def top(self) -> int:
        top1 = -1
        if self.stack:
            top1 = self.stack[-1]       
        return top1         

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# problem: https://leetcode.com/problems/min-stack