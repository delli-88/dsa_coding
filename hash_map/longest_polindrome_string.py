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