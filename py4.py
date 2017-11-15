def longestPalindrome( s):
    # write your code here
    maxlen = len(s)
    print maxlen
    ls = []
    oddmax = 0
    for ch in s:
        if s.count(ch) % 2 != 0:
            print s.count(ch),
            if s.count(ch) >= oddmax:
                oddmax = s.count(ch)
            if ch not in ls:
                ls.append(ch)
    s1 = s
    print ls
    for ch in ls:
        s1 = s1.replace(ch, '')
    print s1
    print oddmax
    return oddmax + len(s1)

s = 'NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy'
longestPalindrome(s)