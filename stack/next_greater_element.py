def nextLargerElement(arr):
    sol = [-1]*len(arr)
    stack = []
    for i in range(len(arr)):
        if stack:
            ele = arr[i]
            if ele >arr[stack[-1]]:
                while stack and arr[stack[-1]]<ele:
                    popped = stack.pop()
                    sol[popped] = ele

        stack.append(i)

    return sol

'''
Problem : https://www.geeksforgeeks.org/next-greater-element/
TC - O(n)
SC - O(n)
Approach :
We can use stack here
we loop through the array
    if stack is empty : just push the curr_ele into the stack
    else, if stack top is Greater than the curr_ele just append into the stack
            if the stack top is Less than curr_ele we just found the next greater element,
            so pop all the stack elements upto we find an element which is greater than curr_ele
            and copy the curr_ele to all the indices we just popped and finally append curr_ele to stack
return the sol arr

'''
print(nextLargerElement([1,4,5,6,7,2,3,8]))