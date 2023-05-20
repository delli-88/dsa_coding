class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return str(self.__dict__)

class Tree:
    def __init__(self) -> None:
        self.root = None
        
    def __repr__(self) -> str:
        return str(self.__dict__)

    def pre_order_recr(self,root):
        if root==None:
            return
        print(root.data,end=" ")
        self.pre_order_recr(root.left)
        self.pre_order_recr(root.right)
        return
    
    def pre_order_iter(self,root):
        # two stacks
        # if root==None:
        #     return []
        # left = [root]
        # right = []
        # sol = []
        # while left or right:
        #     if left:
        #         curr_left = left.pop()
        #         sol.append(curr_left.data)
        #         if curr_left.left:
        #             left.append(curr_left.left)
        #         if curr_left.right:
        #             right.append(curr_left.right)
        #     else:
        #         curr_right = right.pop()
        #         sol.append(curr_right.data)
        #         if curr_right.left:
        #             left.append(curr_right.left)
        #         if curr_right.right:
        #             right.append(curr_right.right)
        # return sol
        #             
        if root==None:
            return []
        stack = [root]
        sol = []
        while stack:
            curr_node = stack.pop()
            sol.append(curr_node.data)
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
            
        return sol


    def in_order_recr(self,root):
        if root==None:
            return
        self.in_order_recr(root.left)
        print(root.data,end=" ")
        self.in_order_recr(root.right)
        return

    def in_order_iter(self,root):
        if root==None:
            return []
        
        stack = [root]
        sol = []
        curr_node = root.left
        while stack or curr_node:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                sol.append(curr_node.data)
                curr_node = curr_node.right
        return sol

    def post_order_recr(self,root):
        if root==None:
            return
        self.post_order_recr(root.left)
        self.post_order_recr(root.right)
        print(root.data,end=" ")
        return

    def post_order_iter(self,root):
        if root==None:
            return []

        stack1 = [root]
        stack2 = []
        while stack1:
            stack1_top = stack1.pop()
            stack2.append(stack1_top)
            stack2_top = stack2[-1]
            if stack2_top.left:
                stack1.append(stack2_top.left)
            if stack2_top.right:
                stack1.append(stack2_top.right)
        sol = []
        while stack2:
            sol.append(stack2.pop().data)
        return sol

    def pre_in_post_order(self,root):
        if root==None:
            return None
            
        stack = [[root,1]]
        pre_order,in_order,post_order = [],[],[]
        while stack:
            stack_top = stack[-1]
            if stack_top[1]==1:
                pre_order.append(stack_top[0].data)
                stack_top[1]+=1
                if stack_top[0].left:
                    stack.append([stack_top[0].left,1])
            elif stack_top[1]==2:
                in_order.append(stack_top[0].data)
                stack_top[1]+=1
                if stack_top[0].right:
                    stack.append([stack_top[0].right,1])
            else:#stack_top[1]==3
                post_order.append(stack_top[0].data)
                stack.pop()
        return [pre_order,in_order,post_order]

    def level_order(self,root):
        if root==None:
            return []
        sol = []
        queue = [root]
        
        while queue:
            level = [] 
            i = len(queue)
            for _ in range(i):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                level.append(queue.pop(0).data)
            sol.append(level)
        return sol
            



myTree = Tree()
root = Node(1)
myTree.root = root
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.right = Node(3)
root.right.left = Node(7)
root.right.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(10)
myTree.pre_order_recr(root)
print()
print(myTree.pre_order_iter(root))
myTree.in_order_recr(root)
print()
print(myTree.in_order_iter(root))
myTree.post_order_recr(root)
print()
print(myTree.post_order_iter(root))
print(myTree.level_order(root))
print()
print(myTree.pre_in_post_order(root))
print(myTree)