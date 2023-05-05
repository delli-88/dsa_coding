def longestPalindrome(n: int, s: str) -> int:
    hash_char = {}
    for i in range(n):
        hash_char[s[i]] = hash_char.get(s[i],0) +1

    polin_cnt = 0
    odd_freq_char = 0
    for v in hash_char.values():
        if v%2==0:
            polin_cnt+=v
        else:
            polin_cnt += (v - 1)
            odd_freq_char = 1

    polin_cnt+=odd_freq_char

    return polin_cnt 
    
def main():
    n = int(input())
    s = input()
    result = longestPalindrome(n, s)
    print(result)

if __name__=="__main__":
    main()
''' 
Problem Description
You are given a string consisting of lower and upper case characters.
You need to find the length of the longest palindrome which you can create by using the characters from the string.
Sample Input 1
4 bbde
Sample Output 1
3
Explanation
The possible 3 size palindrome strings are :- beb and bdb
TC - O(n)
SC - O(n)
Approach :
We store the frequencies of all chars in a hash_map
we iterate through the values of hash_map
    if the value is even then we can add it to result
    else if it is odd, then we can substract 1 from that value and add it to result and we store 1 to add it at the end.

if we see any odd freq value then we add 1 to result
return result

EX -  s = "abcdabceee"
out - 9 (abceeecba or abcedecba)
'''
