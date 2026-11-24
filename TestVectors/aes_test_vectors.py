AES_TEST_VECTORS = [
    {
        "name": "AES-128 Class Example (Board Vector)",
        "plaintext": "00000000000000000000000000001111",
        "key": "00000000000000000000000000000000",
        "expected": {
            "RoundKey_1": "62636363626363636263636362636363",
            "R0_AddRoundKey": "00000000000000000000000000001111",
            "R1_SubBytes": "63636363636363636363636363638282",
            "R1_ShiftRows": "63636382636382636363636363636363",
            "R1_MixColumns": "82825BBA825BBA826363636363636363",
            "R1_AddRoundKey": "E0E138D9E038D9E10100000001000000",
            "Ciphertext": "442758DF6DDA9EDB6BF1468A17B93FE5"
        }
    }
]