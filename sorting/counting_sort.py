def countSort(n: int, s: str) -> str:
    freq = [0]*26

    # updating frequencies of letters
    for i in range(n):
        freq[ord(s[i])-97]+=1
    
    # calculating the cumulative sum of freq
    for j in range(1,26):
        freq[j]+=freq[j-1]

    '''
    # right shifting the freqs
    for k in range(24,0,-1):
        freq[k] = freq[k-1]
    freq[0] = 0
    '''
    sorted_str_arr = [""]*n

    for l in range(n):
        sorted_str_arr[freq[ord(s[l])-97]-1] = s[l]
        freq[ord(s[l])-97]-=1
    
    sorted_str = "".join(sorted_str_arr)

    return sorted_str


print(countSort(7,"babdaac"))

'''
Problem Description
A string S is given consisting of lowercase alphabetical characters only. You need to return a sorted string using Count Sort.
TC - O(n) + O(26)
SC - O(n) -> (for just storing new string) + O(26)
Approach: (there are 2 ways to do this, mentioning other approach)
We init and update freq array which stores the frequencies of the lowercase alphabets
We calc the cumulative freq

we traverse through the string
    we look at the freq of the curr_elem and say its x and we know that there are x elements upto that x index including that,
    so we place the curr_ele in its freq -1 index and decrement its freq so that if we see that ele again thn it will be placed right before it

convert the array into string and return it
'''

