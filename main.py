import sys
from stats import (
    count_words, count_chars
)

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)


    with open(sys.argv[1]) as f:
        file = f.read()

    words = count_words(file)
    chars = count_chars(file)

    char_list = []

    print(f'{words} words found in the document\n\n')

    print(f"e: {chars['e']}")
    print(f"t: {chars['t']}")
    
    for char, count in chars.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

            print(f"The '{char}' character was found {count} times\n")
if __name__ == '__main__':
    main()




