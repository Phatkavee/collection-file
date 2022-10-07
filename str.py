def main():
    count_string = 0
    count_vowel = 0
    count_capital = 0
    uppercase = []
    x = list('aeiouAEIOU')
    string = input("Input String: ")

    for s in string:
        if 'a' <= s <= 'z' or 'A' <= s <= 'Z' :
            count_string += 1
    for v in string:
        if v in x:
            count_vowel += 1
    for c in string:
        if c.isupper():
            count_capital += 1
            uppercase.append(c)

    print("Number of Letters:",count_string)
    print("Number of vowels:",count_vowel)
    print("Number of Capital:",str(count_capital)+',','['+', '.join(uppercase)+']')

main()