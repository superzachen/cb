def atbash(input: str) -> str:
    output = []
    for i in input:
        change = ord(i) - ord('a')
        output.append(chr(ord('z') - change))
    print(''.join(output))
