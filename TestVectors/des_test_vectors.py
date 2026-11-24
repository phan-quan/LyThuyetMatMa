
DES_TEST_VECTORS = [
    {
        "name": "DES Standard Textbook Vector",
        "plaintext": "0123456789ABCDEF",
        "key": "133457799BBCDFF1",
        "expected": {
            "PC1": "C0=F0CCAAF, D0=556678F",
            "K1": "1B02EFFC7072",
            "K16": "CB3D8B0E17F5",
            "IP_L0": "CC00CCFF",
            "IP_R0": "F0AAF0AA",
            "Round_1_E": "7A15557A1555",
            "Round_1_XOR": "6117BA866527",
            "Round_1_SBOX": "5C82B597",
            "Round_1_P": "234AA9BB",
            "Round_1_L": "F0AAF0AA",
            "Round_1_R": "EF4A6544",
            "Round_2_L": "EF4A6544",
            "Round_2_R": "CC017709",
            "Round_16_L": "43423234",
            "Round_16_R": "0A4CD995",
            "Final_Swap": "0A4CD99543423234",
            "Ciphertext": "85E813540F0AB405"
        }
    }
]