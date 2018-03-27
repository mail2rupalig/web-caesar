def alphabet_position(letter):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    position = alphabets.find(letter.lower())

    return position


def rotate_character(char, rot):
    if (ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122):  
        new_position = (alphabet_position(char) + rot) % 26
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        new_letter = alphabets[new_position] 
        if ord(char) >= 65 and ord(char) <= 90:
            return new_letter.upper()
        else:
            return new_letter
    else:
        return char        
def rotate_string(text,rot):
    encrypted_string = ""
    for each_char in text:
        encrypted_string = encrypted_string + rotate_character(each_char, rot)
    return encrypted_string

 