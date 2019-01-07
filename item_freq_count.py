from collections import Counter

text = '''And I hope that you die
And your death'll come soon
I will follow your casket
In the pale afternoon
And I'll watch while you're lowered
Down to your deathbed
And I'll stand over your grave
'Til I'm sure that you're dead'''

word_list = text.split()
print(word_list, '\n')

word_count = Counter(word_list)
print(word_count, '\n')

top_three = word_count.most_common(3)
print(top_three)