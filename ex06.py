def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count


def main():
    sentence = input("Enter a sentence: ")
    vowel_count = count_vowels(sentence)
    print(f"The sentence contains {vowel_count} vowel(s).")


if __name__ == "__main__":
    main()
