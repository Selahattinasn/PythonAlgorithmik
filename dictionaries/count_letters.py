def count_letters(text):
    result={}
    for letter in text:
        if letter not in result:
            result[letter]=0
        result[letter]+=1
    return result
sample="sana dun bir tepeeden baktim ey azizi istanbul"

print(count_letters(sample))