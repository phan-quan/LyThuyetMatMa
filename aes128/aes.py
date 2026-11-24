from .tables import validate_hex, bytes_to_state, state_to_hex
from .key_expansion import key_expansion
from .transformations import (
    add_round_key,
    sub_bytes, inv_sub_bytes,
    shift_rows, inv_shift_rows,
    mix_columns, inv_mix_columns
)


def aes128_encrypt(plaintext_hex: str, key_hex: str) -> tuple:
    validate_hex(plaintext_hex, "Plaintext")
    validate_hex(key_hex, "Key")

    round_keys, key_trace = key_expansion(key_hex)
    trace = {"Key_Expansion": key_trace}

    state = bytes_to_state(bytes.fromhex(plaintext_hex))
    add_round_key(state, round_keys[0])
    trace["Round_0"] = {"AddRoundKey": state_to_hex(state)}

    for r in range(1, 10):
        sub_bytes(state)
        sb = state_to_hex(state)
        shift_rows(state)
        sr = state_to_hex(state)
        mix_columns(state)
        mc = state_to_hex(state)
        add_round_key(state, round_keys[r])
        ark = state_to_hex(state)

        trace[f"Round_{r}"] = {
            "SubBytes": sb,
            "ShiftRows": sr,
            "MixColumns": mc,
            "AddRoundKey": ark
        }

    sub_bytes(state)
    sb = state_to_hex(state)
    shift_rows(state)
    sr = state_to_hex(state)
    add_round_key(state, round_keys[10])
    ark = state_to_hex(state)

    trace["Round_10"] = {
        "SubBytes": sb,
        "ShiftRows": sr,
        "AddRoundKey": ark
    }

    cipher_hex = state_to_hex(state)
    trace["Ciphertext"] = cipher_hex

    return cipher_hex, trace


def aes128_decrypt(ciphertext_hex: str, key_hex: str) -> tuple:
    validate_hex(ciphertext_hex, "Ciphertext")
    validate_hex(key_hex, "Key")

    round_keys, key_trace = key_expansion(key_hex)
    trace = {"Key_Expansion": key_trace}

    state = bytes_to_state(bytes.fromhex(ciphertext_hex))
    add_round_key(state, round_keys[10])
    trace["Round_10_Init"] = {"AddRoundKey": state_to_hex(state)}

    for r in range(9, 0, -1):
        inv_shift_rows(state)
        isr = state_to_hex(state)
        inv_sub_bytes(state)
        isb = state_to_hex(state)
        add_round_key(state, round_keys[r])
        ark = state_to_hex(state)
        inv_mix_columns(state)
        imc = state_to_hex(state)

        trace[f"Round_{r}"] = {
            "InvShiftRows": isr,
            "InvSubBytes": isb,
            "AddRoundKey": ark,
            "InvMixColumns": imc
        }

    inv_shift_rows(state)
    isr = state_to_hex(state)
    inv_sub_bytes(state)
    isb = state_to_hex(state)
    add_round_key(state, round_keys[0])
    ark = state_to_hex(state)

    trace["Round_0"] = {
        "InvShiftRows": isr,
        "InvSubBytes": isb,
        "AddRoundKey": ark
    }

    plaintext_hex = state_to_hex(state)
    trace["Plaintext"] = plaintext_hex

    return plaintext_hex, trace
