from test.test_des import run_des_tests
from test.test_aes import run_aes_tests


if __name__ == "__main__":
    des_ok = run_des_tests(save_to_file=True)
    print("\n")
    aes_ok = run_aes_tests(save_to_file=True)

    print("\n" + "=" * 72)
    print(f"TONG KET: DES={'PASS' if des_ok else 'FAIL'} | AES-128={'PASS' if aes_ok else 'FAIL'}")
    print("=" * 72)