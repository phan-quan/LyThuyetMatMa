from .tables import S_BOX, INV_S_BOX, xtime, gmul


def add_round_key(state: list, rk: list) -> None:
    for r in range(4):
        for c in range(4):
            state[r][c] ^= rk[r][c]


def sub_bytes(state: list) -> None:
    for r in range(4):
        for c in range(4):
            state[r][c] = S_BOX[state[r][c]]


def inv_sub_bytes(state: list) -> None:
    for r in range(4):
        for c in range(4):
            state[r][c] = INV_S_BOX[state[r][c]]

def shift_rows(state: list) -> None:
    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]

def inv_shift_rows(state: list) -> None:
    state[1] = state[1][-1:] + state[1][:-1]
    state[2] = state[2][-2:] + state[2][:-2]
    state[3] = state[3][-3:] + state[3][:-3]

def mix_columns(state: list) -> None:
    for c in range(4):
        a = [state[r][c] for r in range(4)]
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        state[0][c] ^= t ^ xtime(a[0] ^ a[1])
        state[1][c] ^= t ^ xtime(a[1] ^ a[2])
        state[2][c] ^= t ^ xtime(a[2] ^ a[3])
        state[3][c] ^= t ^ xtime(a[3] ^ a[0])

def inv_mix_columns(state: list) -> None:
    for c in range(4):
        a = [state[r][c] for r in range(4)]
        state[0][c] = gmul(a[0], 0x0E) ^ gmul(a[1], 0x0B) ^ gmul(a[2], 0x0D) ^ gmul(a[3], 0x09)
        state[1][c] = gmul(a[0], 0x09) ^ gmul(a[1], 0x0E) ^ gmul(a[2], 0x0B) ^ gmul(a[3], 0x0D)
        state[2][c] = gmul(a[0], 0x0D) ^ gmul(a[1], 0x09) ^ gmul(a[2], 0x0E) ^ gmul(a[3], 0x0B)
        state[3][c] = gmul(a[0], 0x0B) ^ gmul(a[1], 0x0D) ^ gmul(a[2], 0x09) ^ gmul(a[3], 0x0E)
