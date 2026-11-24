from .tables import S_BOX, RCON, validate_hex, bytes_to_state
def key_expansion(key_hex: str) -> tuple:
    validate_hex(key_hex, "Key")
    key_bytes = bytes.fromhex(key_hex)

    w = [list(key_bytes[i:i + 4]) for i in range(4)]
    for i in range(4, 44):
        temp = w[i - 1][:]
        if i % 4 == 0:
            temp = temp[1:] + temp[:1]
            temp = [S_BOX[b] for b in temp]
            temp[0] ^= RCON[i // 4 - 1]
        w.append([w[i - 4][j] ^ temp[j] for j in range(4)])

    round_keys = []
    key_trace = {}
    for r in range(11):
        rk_bytes = bytes(sum(w[r * 4:(r + 1) * 4], []))
        round_keys.append(bytes_to_state(rk_bytes))
        key_trace[f"RoundKey_{r}"] = rk_bytes.hex().upper()

    return round_keys, key_trace
