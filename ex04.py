def is_palindrome(word):
    word = word.lower()
    reversed_word = word[::-1]  
    return word == reversed_word


def main():
    word = input("Enter a word: ")
    if is_palindrome(word):
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")


if __name__ == "__main__":
    main()
