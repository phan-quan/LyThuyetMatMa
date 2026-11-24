from .tables import (
    IP, IP_INV,
    validate_hex, hex_to_bin, bin_to_hex, permute, xor_bits
)
from .key_schedule import generate_subkeys
from .feistel import feistel_trace

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