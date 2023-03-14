import random
my_list = [random.randint(1, 10) for _ in range(200)]
counts = {}
for num in my_list:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
word = lambda n: "раз" if n == 1 else "раза"
for num, count in sorted(counts.items()):
    print(f"Число {num} встречается в первоначальном списке {count} {word(count)}")
