IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

SHIFTS = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]


def validate_hex(value: str, name: str) -> None:
    if not isinstance(value, str):
        raise TypeError(f"{name} phai la chuoi HEX.")

    if len(value) != 16:
        raise ValueError(f"{name} phai co dung 16 ky tu HEX.")

    try:
        int(value, 16)
    except ValueError:
        raise ValueError(f"{name} chi duoc chua cac ky tu HEX 0-9, A-F.")


def hex_to_bin(hex_str: str) -> str:
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def bin_to_hex(bin_str: str) -> str:
    if not bin_str:
        return ""
    return format(int(bin_str, 2), f"0{len(bin_str) // 4}X")


def permute(bits: str, table: list) -> str:
    return ''.join(bits[i - 1] for i in table)


def xor_bits(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Hai chuoi bit phai co cung do dai.")

    return ''.join(
        '1' if x != y else '0'
        for x, y in zip(a, b)
    )


def left_shift(bits: str, n: int) -> str:
    return bits[n:] + bits[:n]


def generate_subkeys(key_hex: str) -> tuple:
    validate_hex(key_hex, "Key")

    key_bin = hex_to_bin(key_hex)
    key_56 = permute(key_bin, PC1)

    C = key_56[:28]
    D = key_56[28:]

    key_trace = {
        "PC1": f"C0={bin_to_hex(C)}, D0={bin_to_hex(D)}"
    }

    subkeys = []

    for i, shift in enumerate(SHIFTS, start=1):
        C = left_shift(C, shift)
        D = left_shift(D, shift)

        K_i = permute(C + D, PC2)

        subkeys.append(K_i)

        key_trace[f"C{i}"] = bin_to_hex(C)
        key_trace[f"D{i}"] = bin_to_hex(D)
        key_trace[f"K{i}"] = bin_to_hex(K_i)

    return subkeys, key_trace


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


def des_encrypt(plaintext_hex: str, key_hex: str) -> tuple:
    validate_hex(plaintext_hex, "Plaintext")
    validate_hex(key_hex, "Key")

    subkeys, key_trace = generate_subkeys(key_hex)
    trace = {"Key_Schedule": key_trace}

    pt_bin = hex_to_bin(plaintext_hex)
    ip_bin = permute(pt_bin, IP)

    L = ip_bin[:32]
    R = ip_bin[32:]

    trace["IP"] = {
        "L0": bin_to_hex(L),
        "R0": bin_to_hex(R)
    }

    for i in range(16):
        old_L = L
        old_R = R

        f_trace = feistel_trace(old_R, subkeys[i])

        L = old_R
        R = xor_bits(old_L, f_trace["output_bin"])

        trace[f"Round_{i + 1}"] = {
            "L": bin_to_hex(L),
            "R": bin_to_hex(R),
            "K": bin_to_hex(subkeys[i]),
            "Feistel": {
                "E": f_trace["E"],
                "XOR": f_trace["XOR"],
                "SBOX_values": f_trace["SBOX_values"],
                "SBOX_output": f_trace["SBOX_output"],
                "P": f_trace["P"]
            }
        }

    final_block = R + L
    trace["Final_Swap"] = bin_to_hex(final_block)

    cipher_bin = permute(final_block, IP_INV)
    cipher_hex = bin_to_hex(cipher_bin)

    trace["Ciphertext"] = cipher_hex

    return cipher_hex, trace


def des_decrypt(ciphertext_hex: str, key_hex: str) -> tuple:
    validate_hex(ciphertext_hex, "Ciphertext")
    validate_hex(key_hex, "Key")

    subkeys, key_trace = generate_subkeys(key_hex)
    reverse_subkeys = list(reversed(subkeys))

    trace = {"Key_Schedule": key_trace}

    cipher_bin = hex_to_bin(ciphertext_hex)
    ip_bin = permute(cipher_bin, IP)

    L = ip_bin[:32]
    R = ip_bin[32:]

    trace["IP"] = {
        "L0": bin_to_hex(L),
        "R0": bin_to_hex(R)
    }

    for i in range(16):
        old_L = L
        old_R = R

        f_trace = feistel_trace(old_R, reverse_subkeys[i])

        L = old_R
        R = xor_bits(old_L, f_trace["output_bin"])

        trace[f"Round_{i + 1}"] = {
            "L": bin_to_hex(L),
            "R": bin_to_hex(R),
            "K": bin_to_hex(reverse_subkeys[i]),
            "Feistel": {
                "E": f_trace["E"],
                "XOR": f_trace["XOR"],
                "SBOX_values": f_trace["SBOX_values"],
                "SBOX_output": f_trace["SBOX_output"],
                "P": f_trace["P"]
            }
        }

    final_block = R + L
    trace["Final_Swap"] = bin_to_hex(final_block)

    plaintext_bin = permute(final_block, IP_INV)
    plaintext_hex = bin_to_hex(plaintext_bin)

    trace["Plaintext"] = plaintext_hex

    return plaintext_hex, trace


def print_key_trace(key_trace: dict) -> None:
    print("\n========== KEY SCHEDULE ==========")
    print("PC1:", key_trace["PC1"])

    for i in range(1, 17):
        print(f"C{i} = {key_trace[f'C{i}']}")
        print(f"D{i} = {key_trace[f'D{i}']}")
        print(f"K{i} = {key_trace[f'K{i}']}")


def print_des_trace(trace: dict, mode: str = "encrypt") -> None:
    print("\n========== DES TRACE ==========")

    print("\n--- Initial Permutation ---")
    print("L0 =", trace["IP"]["L0"])
    print("R0 =", trace["IP"]["R0"])

    for i in range(1, 17):
        round_data = trace[f"Round_{i}"]
        feistel_data = round_data["Feistel"]

        print(f"\n--- Round {i} ---")
        print("K  =", round_data["K"])
        print("E  =", feistel_data["E"])
        print("XOR =", feistel_data["XOR"])
        print("SBOX values =", feistel_data["SBOX_values"])
        print("SBOX output =", feistel_data["SBOX_output"])
        print("P  =", feistel_data["P"])
        print("L  =", round_data["L"])
        print("R  =", round_data["R"])

    print("\n--- Final Swap ---")
    print(trace["Final_Swap"])

    if mode == "encrypt":
        print("\nCiphertext =", trace["Ciphertext"])
    else:
        print("\nPlaintext =", trace["Plaintext"])


if __name__ == "__main__":
    plaintext = "0123456789ABCDEF"
    key = "133457799BBCDFF1"

    print("========== DES ENCRYPTION ==========")

    ciphertext, encrypt_trace = des_encrypt(plaintext, key)

    print("Plaintext :", plaintext)
    print("Key       :", key)
    print("Ciphertext:", ciphertext)

    print_key_trace(encrypt_trace["Key_Schedule"])
    print_des_trace(encrypt_trace, "encrypt")

    print("\n========== DES DECRYPTION ==========")

    decrypted, decrypt_trace = des_decrypt(ciphertext, key)

    print("Ciphertext:", ciphertext)
    print("Key       :", key)
    print("Plaintext :", decrypted)

    if decrypted == plaintext.upper():
        print("\nDES TEST: PASS")
    else:
        print("\nDES TEST: FAIL")