import ascii
import sys
from time import sleep

def main():
    p1 = {"attempts": 0, "used_letters": []}
    p2 = {"attempts": 0, "used_letters": []}
    preparation(p1,p2)
    while p1["attempts"] < 6 or p2["attempts"] < 6:
        if p1["attempts"] < 6:
            turn(p1)
            new_screen()
        if p2["attempts"] < 6:
            turn(p2)
            new_screen()
    if p1["attempts"] == 6 and p2["attempts"] == 6:
        sys.exit(f"Game over. \n{p1['name']}'s word to guess was {p1['word']}. \n{p2['name']}'s word to guess was {p2['word']}. ")
    elif p1["attempts"] == 7 and p2["attempts"] == 7:
        sys.exit("You have both guessed your words. Good job!")
    elif p1["attempts"] == 7 and p2["attempts"] == 6:
        sys.exit(f"{p1['name']} wins! {p2['name']}'s word was {''.join(p2['word'])}")
    else: sys.exit(f"{p2['name']} wins! {p1['name']}'s word was {''.join(p1['word'])}")


def turn(p):
    print(f"It is {p['name']}'s turn:")
    print(ascii.HANGMANPICS[p['attempts']])
    print(f'Letters used so far: {p["used_letters"]}')
    print(f"Word: {p['code_word']}")
    letter = guess(p)
    if not letter:
        print(f"The word does not contain this letter.")
        p["attempts"] += 1
        if p["attempts"] == 6:
            print(ascii.HANGMANPICS[p['attempts']])
            print(f"Game over for {p['name']}. Your word was {''.join(p['word'])}")
    else:
        for i in range(len(p["word"])):
            if letter == p["word"][i]:
                p["code_word"][i] = letter
        print(p["code_word"])
        if ''.join(p["word"]) == ''.join(p["code_word"]):
            p['attempts'] = 7
            print(f"{p['name']} wins! The word was \"{''.join(p['word'])}\"")
    


def guess(p):
    while True:
        letter = input("What is your guess? ").lower()
        if letter in p["used_letters"]:
            print("You have already tried this letter.")
        elif len(letter) > 1 or not letter.isalpha():
            print("Guess must be a single letter.")
        else:
            p["used_letters"] += letter
            if letter in p["word"]:
                return letter
            else:
                return False
           
def new_screen():
    sleep(2)
    print("\n"*40)

def preparation(p1,p2):
    p1["name"] = input("What is the first player's name? ")
    p2["word"] = input("What word do you want your opponent guess? ").lower().strip()
    new_screen()
    p2["code_word"] = ["_" for c in p2["word"]]
    p2["name"] = input("What is the second player's name? ")
    p1["word"] = input("What word do you want your opponent to guess? ").lower().strip()
    new_screen()
    p1["code_word"] = ["_" for c in p1["word"]]

main()


#def player_turn(name, word, used_letters):
#    guess(input(f"It is {name}'s turn. What is your guess?:"), word, used_letters)
#
#   if letter not in used_letters:
#       used_letters.append(letter)
#
#def guess(letter, used_letters):
#    if len(letter) == 1 and letter.isalpha():
#        if letter in used_letters:
#            print("You have already tried this letter")
#            return False
#        else:
#            if letter not in used_letters:
#                used_letters.append(letter)
#            return True
#    else:
#        print("Guess must be a single letter.")
#        return False
#
#def decode(letter, word, code_word):
#    for i in range(len(word)):
#        if word[i] == letter:
#            lst = list(code_word)
#            lst[i] = letter
#            code_word = ''.join(lst)
#    return code_word
#
#
#
#
#if __name__ == "__main__":
#    main()