letters=["a","b","c","d","e"]
def filter_vowels(letters):
    vowels=['a','e','i','o','u']
    return letters in vowels
result=filter(filter_vowels,letters)
print(list(result))