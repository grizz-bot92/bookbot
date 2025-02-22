def count_words(words):
    return len(words.split())

def count_chars(words):
    chars = {}
    
    for char in words.lower():
        chars[char] = chars.get(char, 0) + 1
        
    return chars