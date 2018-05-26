def to_encrypt(text, delta):
    if delta < 0:
        delta = 26 + delta
    text_encrypted = ""
    for letter in text:
        text_encrypted += encrypt_letter(letter, delta)
    return text_encrypted

def encrypt_letter(letter, delta):
    if letter != " ":
        letter = (ord(letter) - 96) # 1 indexed alphabet value
        letter += delta
        letter = (letter % 26) + 96
        return(chr(letter))
    return(" ")

print(to_encrypt('abc', -1))

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', -1))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")