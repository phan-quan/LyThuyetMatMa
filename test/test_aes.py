import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from aes128.aes import aes128_encrypt, aes128_decrypt
from TestVectors.aes_test_vectors import AES_TEST_VECTORS
def check_state(lines: list, name: str, actual: str, expected: dict) -> bool:
    if name in expected:
        exp_val = expected[name]
        if actual == exp_val:
            lines.append(f"[PASS] {name:<16}: {actual}")
            return True
        lines.append(f"[FAIL] {name:<16}: Actual={actual} | Expected={exp_val}")
        return False
    lines.append(f"[INFO] {name:<16}: {actual}")
    return True

def run_aes_tests(save_to_file: bool = True) -> bool:
    lines = []
    overall_passed = True

    for vec in AES_TEST_VECTORS:
        case_passed = True

        lines.append(f"=== TEST CASE: {vec['name']} ===")
        lines.append(f"Plaintext : {vec['plaintext']}")
        lines.append(f"Key       : {vec['key']}")
        lines.append("-" * 72)

        ciphertext, trace = aes128_encrypt(vec["plaintext"], vec["key"])
        expected = vec.get("expected", {})

        lines.append("--- Key Expansion ---")
        ke = trace["Key_Expansion"]
        for r in range(11):
            case_passed &= check_state(lines, f"RoundKey_{r}", ke[f"RoundKey_{r}"], expected)

        lines.append("\n--- Round 0 ---")
        case_passed &= check_state(lines, "R0_AddRoundKey", trace["Round_0"]["AddRoundKey"], expected)

        lines.append("\n--- Rounds 1 to 9 ---")
        for r in range(1, 10):
            r_data = trace[f"Round_{r}"]
            lines.append(f"Round {r}:")
            case_passed &= check_state(lines, f"R{r}_SubBytes", r_data["SubBytes"], expected)
            case_passed &= check_state(lines, f"R{r}_ShiftRows", r_data["ShiftRows"], expected)
            case_passed &= check_state(lines, f"R{r}_MixColumns", r_data["MixColumns"], expected)
            case_passed &= check_state(lines, f"R{r}_AddRoundKey", r_data["AddRoundKey"], expected)

        lines.append("\n--- Round 10 (Final) ---")
        r10 = trace["Round_10"]
        case_passed &= check_state(lines, "R10_SubBytes", r10["SubBytes"], expected)
        case_passed &= check_state(lines, "R10_ShiftRows", r10["ShiftRows"], expected)
        case_passed &= check_state(lines, "R10_AddRoundKey", r10["AddRoundKey"], expected)

        lines.append("\n--- Final Output ---")
        case_passed &= check_state(lines, "Ciphertext", ciphertext, expected)

        decrypted, _ = aes128_decrypt(ciphertext, vec["key"])
        if decrypted == vec["plaintext"].upper():
            lines.append(f"[PASS] {'Decrypt_Check':<16}: {decrypted}")
        else:
            case_passed = False
            lines.append(
                f"[FAIL] {'Decrypt_Check':<16}: "
                f"Actual={decrypted} | Expected={vec['plaintext'].upper()}"
            )
        lines.append("-" * 72)
        lines.append(f"KET QUA TEST CASE: {'PASS' if case_passed else 'FAIL'}\n")
        overall_passed &= case_passed

    lines.append("=" * 72)
    lines.append(f"KET QUA TONG QUAT AES-128: {'PASS' if overall_passed else 'FAIL'}")
    lines.append("=" * 72)

    output_text = "\n".join(lines)
    print(output_text)

    if save_to_file:
        output_dir = os.path.join(ROOT_DIR, "TestVectors")
        os.makedirs(output_dir, exist_ok=True)
        out_path = os.path.join(output_dir, "output_aes128.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output_text)
        print(f"\nDa luu ket qua tai: {out_path}")

    return overall_passed
if __name__ == "__main__":
    run_aes_tests()
