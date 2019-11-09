
def vowel_count(word):
    v_count=""
    for char in word:
        if char in 'aeiouAEIOU':
            print(char)
            v_count += char
    return(v_count)

s=vowel_count("Madhuri Charugundla")
print(s)
