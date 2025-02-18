import random
import base64
import sys
from secret import FLAG

ans = [
    "apple", "grape", "peach", "berry", "plum", "lemon", "melon", "mango",
    "bread", "cheese", "honey", "candy", "salad", "olive", "bacon", "cream",
    "drink", "water", "juice", "pizza", "pasta", "sushi", "tacos", "steak"
    ]
def game():
    random_word = random.choice(ans)

    encoded_word = base64.b64encode(random_word.encode("utf-8")).decode("utf-8")

    rot_shift = random.randint(1, 26)

    # 進行 ROT 位移
    userans= ''.join(
        chr((ord(char) - 65 + rot_shift) % 26 + 65) if 'A' <= char <= 'Z' else
        chr((ord(char) - 97 + rot_shift) % 26 + 97) if 'a' <= char <= 'z' else
        char
        for char in encoded_word
    )

    print("bot: ", userans)
    userinput = input(': ')

    if userinput == random_word:
        print("you win!")
        return
    else:
        print("you loss!")
        sys.exit()


def main():
    print(f"""
=======================
BASE64 & ROT CHALLENGE!
=======================
rules:
1. The bot will encode a word using Base64 and then apply a ROT (rotation) with a random shift value (from 1 to 26).
2. Your task is to decode the result by reversing both the Base64 encoding and the ROT shift.
3. If you make even one mistake, the game ends immediately.
4. Once you've decoded the word, send back the correct word as your answer.

ANS list: {ans}

          """)

    for i in range(100):
        print(f"===== chalenge {i+1} =====")
        game()
    print(FLAG)

try:
    main()
except:
    sys.exit()
