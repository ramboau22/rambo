word_count = {}
with open('test.txt', 'r') as f:
    for line in f:
        word = line.lower().split()
        for word1 in word:
            if word1 not in word_count:
                word_count[word1] =1
            else:
                word_count[word1] += 1

f.close()

for k, v in word_count.items():
    if v>=1:
        print(f'{k}:{v}')


