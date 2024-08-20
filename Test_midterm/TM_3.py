def word_frequency(text: str) -> dict:
    word_count = {}
    words = text.lower().split()
    if 1 <= len(words) <= 1000:
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count
    else:
        return "null"


print(word_frequency("Hello world! hello everyone."))
# Expect output: {'hello ': 2, 'world!': 1, 'everyone.': 1}

print(word_frequency("This is a test. This test is easy."))
# Expect output: {'this ': 2, 'is': 2, 'a': 1, 'test.': 2, 'easy.': 1}

print(word_frequency("Python is fun. Fun fun fun!"))
# Expect output: {'python ': 1, 'is': 1, 'fun.': 4}
print(word_frequency("One word , one word."))
# Expect output: {'one ': 2, 'word ': 2}
print(word_frequency(" "))
