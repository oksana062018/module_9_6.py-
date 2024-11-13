def all_variants(text):
    l = len(text)
    for i in range(l):
        for k in range(i + 1, l + 1):
            yield text[i:k]


a = all_variants("abc")
for i in a:
    print(i)