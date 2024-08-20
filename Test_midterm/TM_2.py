def find_repeated_substrings(s: str) -> list:
    substr_count = {}
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if substring in substr_count:
                substr_count[substring] += 1
            else:
                substr_count[substring] = 1

    repeated_substrings = [k for k, v in substr_count.items() if v > 1 and len(k) > 1]

    return repeated_substrings


print(find_repeated_substrings("banana"))
# Output: ['an', 'ana', 'na']
print(find_repeated_substrings("abcdefg"))
# Output: []

print(find_repeated_substrings("abcabcabc"))
# Output: ['ab', 'abc', 'abca', 'abcab', 'abcabc', 'bc', 'bca', 'bcab','bcabc', 'ca', 'cab', 'cabc ']
print(find_repeated_substrings("aaaa"))
# Output: ['aa', 'aaa ']
