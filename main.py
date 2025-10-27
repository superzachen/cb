import typer  # noqa: F401


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


if __name__ == "__main__":
    typer.run(ceaser)


    
