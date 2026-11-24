from .tables import (
    PC1, PC2, SHIFTS,
    validate_hex, hex_to_bin, bin_to_hex, permute, left_shift
)

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
