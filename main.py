
def count_words(words):
    return len(words.split())

def count_chars(words):
    chars = {}
    
    for char in words.lower():
        chars[char] = chars.get(char, 0) + 1
        
    return chars


def main():

    with open('books/frankenstein.txt') as f:
        file = f.read()

    words = count_words(file)
    chars = count_chars(file)

    char_list = []

    print(f'{words} words found in the document\n\n')
    
    for char, count in chars.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

            print(f"The '{char}' character was found {count} times\n")
if __name__ == '__main__':
    main()
