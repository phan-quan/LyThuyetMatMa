
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from des.des import des_encrypt, des_decrypt
from TestVectors.des_test_vectors import DES_TEST_VECTORS

def check_state(lines: list, name: str, actual: str, expected: dict) -> bool:
    if name in expected:
        exp_val = expected[name]

        if actual == exp_val:
            lines.append(f"[PASS] {name:<16}: {actual}")
            return True
        lines.append(
            f"[FAIL] {name:<16}: Actual={actual} | Expected={exp_val}"
        )
        return False
    lines.append(f"[INFO] {name:<16}: {actual}")
    return True
def run_des_tests(save_to_file: bool = True) -> bool:
    lines = []
    overall_passed = True

    for vec in DES_TEST_VECTORS:
        case_passed = True
        lines.append(f"=== TEST CASE: {vec['name']} ===")
        lines.append(f"Plaintext : {vec['plaintext']}")
        lines.append(f"Key       : {vec['key']}")
        lines.append("-" * 72)

        ciphertext, trace = des_encrypt(vec["plaintext"], vec["key"])
        expected = vec.get("expected", {})

        # 1. Key Schedule
        lines.append("--- Key Schedule ---")
        ks = trace["Key_Schedule"]

        # PC1: tach C0 va D0 tu 56 bit sau phep hoan vi PC1
        pc1 = ks["PC1"]

        if len(pc1) == 56 and set(pc1).issubset({"0", "1"}):
            c0_bin = pc1[:28]
            d0_bin = pc1[28:]

            c0 = format(int(c0_bin, 2), "07X")
            d0 = format(int(d0_bin, 2), "07X")

            pc1_display = f"C0={c0}, D0={d0}"
        else:
            pc1_display = pc1

        case_passed &= check_state(
            lines, "PC1", pc1_display, expected
        )
        # Kiem tra 16 khoa con
        for i in range(1, 17):
            case_passed &= check_state(
                lines, f"K{i}", ks[f"K{i}"], expected
            )
        # 2. Initial Permutation
        lines.append("\n--- Initial Permutation ---")

        case_passed &= check_state(
            lines, "IP_L0", trace["IP"]["L0"], expected
        )
        case_passed &= check_state(
            lines, "IP_R0", trace["IP"]["R0"], expected
        )
        # 3. Feistel Rounds
        lines.append("\n--- 16 Feistel Rounds ---")

        for i in range(1, 17):
            r_data = trace[f"Round_{i}"]
            f_data = r_data["Feistel"]

            lines.append(f"Round {i}:")

            case_passed &= check_state(
                lines, f"Round_{i}_E", f_data["E"], expected
            )
            case_passed &= check_state(
                lines, f"Round_{i}_XOR", f_data["XOR"], expected
            )
            case_passed &= check_state(
                lines,
                f"Round_{i}_SBOX",
                f_data["SBOX_output"],
                expected
            )
            case_passed &= check_state(
                lines, f"Round_{i}_P", f_data["P"], expected
            )
            case_passed &= check_state(
                lines, f"Round_{i}_L", r_data["L"], expected
            )
            case_passed &= check_state(
                lines, f"Round_{i}_R", r_data["R"], expected
            )
        # 4. Final Output
        lines.append("\n--- Final Output ---")

        case_passed &= check_state(
            lines, "Final_Swap", trace["Final_Swap"], expected
        )
        case_passed &= check_state(
            lines, "Ciphertext", ciphertext, expected
        )
        # 5. Decryption Check
        decrypted, _ = des_decrypt(ciphertext, vec["key"])

        if decrypted == vec["plaintext"].upper():
            lines.append(
                f"[PASS] {'Decrypt_Check':<16}: {decrypted}"
            )
        else:
            case_passed = False
            lines.append(
                f"[FAIL] {'Decrypt_Check':<16}: "
                f"Actual={decrypted} | "
                f"Expected={vec['plaintext'].upper()}"
            )
        lines.append("-" * 72)
        lines.append(
            f"KET QUA TEST CASE: {'PASS' if case_passed else 'FAIL'}"
        )
        lines.append("")
        overall_passed &= case_passed
    # 6. Overall Result
    lines.append("=" * 72)
    lines.append(
        f"KET QUA TONG QUAT DES: "
        f"{'PASS' if overall_passed else 'FAIL'}"
    )
    lines.append("=" * 72)

    output_text = "\n".join(lines)
    print(output_text)
    # 7. Save test result
    if save_to_file:
        output_dir = os.path.join(ROOT_DIR, "TestVectors")
        os.makedirs(output_dir, exist_ok=True)
        out_path = os.path.join(output_dir, "output_des.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output_text)
        print(f"\nDa luu ket qua tai: {out_path}")
    return overall_passed
if __name__ == "__main__":
    run_des_tests()

