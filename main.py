import string
import itertools
import typer  # noqa: F401
app = typer.Typer()

def ceaser_decrypt(input_str: str, shift: int) -> str:
    """
    Decrypts a Caesar cipher string by shifting each letter back.

    Args:
        input_str: The encrypted string (ciphertext).
        shift: The integer value used for the original encryption.

    Returns:
        The decrypted string (plaintext).
    """
    decrypted_text = ""

    for char in input_str:
        # Check if the character is an uppercase letter
        if "A" <= char <= "Z":
            # Calculate the new position after shifting back
            # (ord(char) - ord('A')) gives the 0-25 position
            # We subtract the shift and use modulo 26 to wrap around
            # ord('A') is added back to get the new ASCII value
            new_ord = (ord(char) - ord("A") - shift) % 26 + ord("A")
            decrypted_text += chr(new_ord)
        # Check if the character is a lowercase letter
        elif "a" <= char <= "z":
            # Same logic as uppercase, but using 'a' as the base
            new_ord = (ord(char) - ord("a") - shift) % 26 + ord("a")
            decrypted_text += chr(new_ord)
        # If it's not a letter, add it unchanged
        else:
            decrypted_text += char

    return decrypted_text

@app.command()
def ceaser(input: str, shift: int = 0) -> str:
    if shift == 0:
        dict_set = load_eng_dict()
        for i in range(25):
            plain_text = ceaser_decrypt(input, i + 1)
            words = plain_text.split(" ")
            hit_count = 0
            for w in words:
                if w.lower() in dict_set:
                    hit_count +=1
            hit_rate = hit_count / len(words)
            if hit_rate > 0.9:
                print(f"{i + 1}: {plain_text}")
    else:
        print(ceaser_decrypt(input, shift % 26))
    
def load_eng_dict() -> set:
    import pathlib

    myset = set()
    p = pathlib.Path("./words.txt")
    for line in p.read_text().split("\n"):
        myset.add(line.lower())
    return myset

@app.command()
def atbash(input: str) -> str:
    output = []
    for i in input:
        change = ord(i) - ord('a')
        output.append(chr(ord('z') - change))
    print(''.join(output))

@app.command()
def cb55(input:str, pob_key:str) -> str:
    input = input.lower()
    pob_key = pob_key.lower()
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] ]
    letters = [char for char in string.ascii_lowercase if char != 'j']
    pob_len = len(pob_key)
    for r in range(5):
        for c in range(5):
            if pob_len > 0:
                board[r][c] = pob_key[0]
                letters.remove(pob_key[0])
                pob_len -= 1
                pob_key = pob_key[1:]
            else:
                board[r][c] = letters[0]
                letters.pop(0)
    words = input.split(' ')
    rk_set = set()
    ck_set = set()
    token_list = []
    for word in words:
        for i in range(0, len(word), 2):
            token_list.append(word[i:i+2])
    for token in token_list:
        rk_set.add(token[0])
        ck_set.add(token[1])
    rk_combos = ["".join(p) for p in itertools.permutations(list(rk_set))]
    ck_combos = ["".join(p) for p in itertools.permutations(list(ck_set))]
    dict_set = load_eng_dict()
    rk_words = []
    ck_words = []
    for combo in rk_combos:
        if combo in dict_set:
            rk_words.append(combo)
    for combo in ck_combos:
        if combo in dict_set:
            ck_words.append(combo)
    print(ck_set, rk_set)


if __name__ == "__main__":
    app()

    