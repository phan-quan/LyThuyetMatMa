from .tables import E, P, S_BOXES, bin_to_hex, permute, xor_bits

def feistel_trace(R: str, subkey: str) -> dict:
    if len(R) != 32:
        raise ValueError("R phai co do dai 32 bit.")
    if len(subkey) != 48:
        raise ValueError("Khoa con phai co do dai 48 bit.")
    expanded = permute(R, E)
    xored = xor_bits(expanded, subkey)

    sbox_out = ""
    sbox_values = []
    for i in range(8):
        block = xored[i * 6:(i + 1) * 6]

        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)

        value = S_BOXES[i][row][col]

        sbox_values.append(value)
        sbox_out += format(value, "04b")
    p_out = permute(sbox_out, P)
    return {
        "E": bin_to_hex(expanded),
        "XOR": bin_to_hex(xored),
        "SBOX_values": sbox_values,
        "SBOX_output": bin_to_hex(sbox_out),
        "P": bin_to_hex(p_out),
        "output_bin": p_out
    }


def feistel(R: str, subkey: str) -> str:
    return feistel_trace(R, subkey)["output_bin"]
