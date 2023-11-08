import string

alphabet = list(string.ascii_lowercase)


def solution(x):  # Example: ZYX
    decodedString = []
    for ch in list(x):  # For each letter in the given string, find its value
        if ch.isalpha() and ch.islower():
            pos = alphabet.index(ch) # Gives the position within the alphabet
            decodedString.append(alphabet[25 - pos]) # Find the opposing letter position
        else:
            decodedString.append(ch)
    print(''.join(decodedString))

solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")