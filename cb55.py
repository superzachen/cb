import string
import itertools
from utils import load_eng_dict

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
    pos_ans = []
    for rk in rk_words:
        for ck in ck_words:
            ans = []
            for tok in token_list:
                r_idx = rk.find(tok[0])
                c_idx = ck.find(tok[1])
                ans.append(board[r_idx][c_idx])
            ans = "".join(ans)
            pos_ans.append(ans)
    for ans in pos_ans:
        print(ans)
