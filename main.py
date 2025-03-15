keypad = {
    '0': [],
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

def check(phonenumber, words):

    # Loop through all words
    for word in words:
        # For each character of the word, determine corresponding number in keypad
        # collect all corresponding numbers in nr
        nr = ""
        for i in range(len(word)):
            for idx, val in keypad.items():
                if word[i] in val:
                    nr += idx
                    break
        
        # If collected keypad numbers are equal to given phone number then
        # word is contained in phone number else it is not
        if phonenumber == nr:
            print(f"{word} is contained in phonenumber")
        else:
            print(f"{word} is not contained in phonenumber")

if __name__ == "__main__":
    phonenumber = "36622277"
    words = ["foo", "bar", "baz", "foobar", "emo", "cap", "car", "cat","domabcrs"]
    check(phonenumber, words)