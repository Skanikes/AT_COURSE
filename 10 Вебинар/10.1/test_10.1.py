import random
"""Комментарий с другого клона"""

def generate_random_name():
    while True:
        word1_length = random.randint(1, 15)
        word1_characters = []
        for i in range(word1_length):
            word1_characters.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        word1 = ''.join(word1_characters)

        word2_length = random.randint(1, 15)
        word2_characters = []
        for i in range(word2_length):
            word2_characters.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        word2 = ''.join(word2_characters)

        yield f'{word1} {word2}'



gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))