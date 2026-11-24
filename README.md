# LyThuyetMatMa
Bài tập môn Lý thuyết mật mã HUST
 
# BÀI TẬP LỚN LÝ THUYẾT MẬT MÃ
## Xây dựng và kiểm thử thuật toán DES và AES-128 bằng Python

## 1. Giới thiệu

Dự án được thực hiện nhằm tìm hiểu, xây dựng và kiểm thử hai thuật toán mã hóa khối phổ biến là DES (Data Encryption Standard) và AES-128 (Advanced Encryption Standard) bằng ngôn ngữ lập trình Python.

Chương trình được tổ chức theo mô hình module hóa, tách riêng các thành phần xử lý của từng thuật toán để thuận tiện cho việc theo dõi, kiểm thử, bảo trì và phát triển.

Các chức năng chính:
- Cài đặt thuật toán mã hóa và giải mã DES.
- Cài đặt thuật toán mã hóa và giải mã AES-128.
- Triển khai các bước xử lý trung gian của từng thuật toán.
- Kiểm thử bằng các bộ Test Vector.
- So sánh kết quả thực tế với kết quả mong đợi.
- Xuất kết quả kiểm thử ra các file văn bản.

## 2. Công nghệ sử dụng

- Ngôn ngữ lập trình: Python.
- Môi trường phát triển: Visual Studio.
- Phiên bản Python: Python 3.11.
- Các thư viện chính: Thư viện chuẩn của Python.

## 3. Cấu trúc thư mục dự án

```text
LyThuyetMatMa/
│
├── aes128/
│   ├── __init__.py
│   ├── aes.py
│   ├── key_expansion.py
│   ├── tables.py
│   └── transformations.py
│
├── des/
│   ├── __init__.py
│   ├── des.py
│   ├── feistel.py
│   ├── key_schedule.py
│   └── tables.py
│
├── test/
│   ├── __init__.py
│   ├── test_aes.py
│   └── test_des.py
│
├── TestVectors/
│   ├── __init__.py
│   ├── aes_test_vectors.py
│   ├── des_test_vectors.py
│   ├── output_aes128.txt
│   └── output_des.txt
│
├── main.py
└── README.md
```

### Chức năng các thư mục và file

**Thư mục `des/` – Thuật toán DES**

- `tables.py`: Chứa các bảng cố định của DES như IP, IP_INV, E, P, PC1, PC2, SHIFTS và S-BOX.
- `key_schedule.py`: Thực hiện xử lý khóa và sinh các khóa con cho 16 vòng mã hóa.
- `feistel.py`: Cài đặt hàm Feistel và các bước xử lý bên trong.
- `des.py`: Thực hiện mã hóa, giải mã DES và ghi nhận quá trình xử lý.
- `__init__.py`: Khởi tạo package DES và hỗ trợ import các thành phần.

**Thư mục `aes128/` – Thuật toán AES-128**

- `tables.py`: Chứa S-BOX, INV_S_BOX, RCON và các hàm xử lý dữ liệu cơ bản.
- `key_expansion.py`: Thực hiện quá trình mở rộng khóa, tạo 11 khóa vòng.
- `transformations.py`: Cài đặt các phép biến đổi SubBytes, ShiftRows, MixColumns, AddRoundKey và các phép biến đổi ngược.
- `aes.py`: Thực hiện thuật toán mã hóa và giải mã AES-128.
- `__init__.py`: Khởi tạo package AES-128 và hỗ trợ import các thành phần.

**Thư mục `test/` – Kiểm thử**

- `test_des.py`: Kiểm thử thuật toán DES.
- `test_aes.py`: Kiểm thử thuật toán AES-128.
- `__init__.py`: Khởi tạo package test.

**Thư mục `TestVectors/` – Dữ liệu kiểm thử**

- `des_test_vectors.py`: Chứa các bộ dữ liệu kiểm thử DES.
- `aes_test_vectors.py`: Chứa các bộ dữ liệu kiểm thử AES-128.
- `output_des.txt`: Lưu kết quả kiểm thử DES.
- `output_aes128.txt`: Lưu kết quả kiểm thử AES-128.

**File `main.py`**

Là chương trình chính, gọi các hàm kiểm thử DES và AES-128, sau đó tổng hợp kết quả thực hiện.

## 4. Thuật toán DES

### 4.1. Tổng quan

DES là thuật toán mã hóa khối đối xứng, có các đặc điểm:
- Kích thước khối dữ liệu: 64 bit.
- Kích thước khóa đầu vào: 64 bit.
- Độ dài khóa thực tế: 56 bit, 8 bit còn lại dùng cho kiểm tra chẵn lẻ.
- Số vòng mã hóa: 16 vòng.
- Cấu trúc: Mạng Feistel.

### 4.2. Quy trình mã hóa

Quá trình mã hóa DES gồm các bước:

1. Thực hiện hoán vị khởi đầu IP.
2. Chia khối dữ liệu thành hai nửa L0 và R0, mỗi nửa 32 bit.
3. Thực hiện 16 vòng Feistel:
   - Mở rộng R thành 48 bit bằng bảng E.
   - XOR với khóa con Ki.
   - Đưa kết quả qua 8 hộp S-Box.
   - Hoán vị kết quả bằng bảng P.
   - XOR với nửa trái Li.
   - Hoán đổi hai nửa dữ liệu.
4. Thực hiện hoán đổi cuối.
5. Thực hiện hoán vị nghịch đảo IP_INV để thu được bản mã.

### 4.3. Quy trình giải mã

Quá trình giải mã sử dụng cấu trúc tương tự mã hóa DES, nhưng thứ tự sử dụng các khóa con được đảo ngược từ K16 về K1.

## 5. Thuật toán AES-128

### 5.1. Tổng quan

AES-128 là thuật toán mã hóa khối đối xứng thuộc tiêu chuẩn AES, có các đặc điểm:
- Kích thước khối dữ liệu: 128 bit.
- Kích thước khóa: 128 bit.
- Số vòng mã hóa: 10 vòng.
- Số khóa vòng: 11 khóa, bao gồm khóa ban đầu.
- Cấu trúc: Substitution-Permutation Network.

### 5.2. Quy trình mở rộng khóa

Quá trình Key Expansion tạo ra 44 word, mỗi word có 32 bit, tương ứng với 11 khóa vòng.

Các phép xử lý chính:
- RotWord.
- SubWord.
- XOR với Rcon.
- XOR với word trước đó.

### 5.3. Quy trình mã hóa

Quá trình mã hóa AES-128 gồm:

**Bước đầu tiên: AddRoundKey**

Thực hiện XOR trạng thái ban đầu với khóa vòng 0.

**Các vòng từ 1 đến 9:**

1. SubBytes: Thay thế từng byte thông qua S-Box.
2. ShiftRows: Dịch vòng các hàng của ma trận trạng thái.
3. MixColumns: Biến đổi các cột trong trường hữu hạn GF(2^8).
4. AddRoundKey: XOR trạng thái với khóa vòng tương ứng.

**Vòng thứ 10:**

1. SubBytes.
2. ShiftRows.
3. AddRoundKey.

Ở vòng cuối không thực hiện MixColumns.

### 5.4. Quy trình giải mã

Quá trình giải mã AES-128 sử dụng các phép biến đổi ngược:
- InvShiftRows.
- InvSubBytes.
- AddRoundKey.
- InvMixColumns.

Các khóa vòng được sử dụng theo thứ tự ngược từ khóa vòng 10 về khóa vòng 0.

## 6. Hướng dẫn chạy chương trình

### 6.1. Yêu cầu

- Đã cài đặt Python 3.11 hoặc phiên bản tương thích.
- Đã mở dự án bằng Visual Studio.
- Các thư mục và file được đặt đúng cấu trúc như mục 3.

### 6.2. Chạy chương trình

Mở file `main.py`, sau đó chạy chương trình bằng Visual Studio.

Có thể sử dụng tổ hợp phím:

```text
Ctrl + F5
```

Chương trình sẽ lần lượt:
1. Chạy kiểm thử thuật toán DES.
2. Chạy kiểm thử thuật toán AES-128.
3. So sánh kết quả với các giá trị trong Test Vector.
4. Kiểm tra khả năng giải mã khôi phục bản rõ.
5. Xuất kết quả ra các file văn bản.
6. Tổng hợp trạng thái kiểm thử.

### 6.3. Các câu lệnh import chính

Import hàm kiểm thử DES và AES-128:

```python
from test.test_des import run_des_tests
from test.test_aes import run_aes_tests
```

Import các hàm mã hóa và giải mã AES-128:

```python
from aes128.aes import aes128_encrypt, aes128_decrypt
```

## 7. Kết quả kiểm thử

### 7.1. Kiểm thử DES

Sử dụng bộ dữ liệu kiểm thử:

| Thông số | Giá trị |
|---|---|
| Plaintext | `0123456789ABCDEF` |
| Key | `133457799BBCDFF1` |
| Ciphertext mong đợi | `85E813540F0AB405` |

Kết quả thực tế:
- Ciphertext thu được trùng với kết quả mong đợi.
- Giải mã khôi phục đúng bản rõ ban đầu.
- Các bước xử lý được ghi lại trong file `output_des.txt`.

**Kết quả: PASS**

### 7.2. Kiểm thử AES-128

Sử dụng bộ dữ liệu kiểm thử:

| Thông số | Giá trị |
|---|---|
| Plaintext | `00000000000000000000000000001111` |
| Key | `00000000000000000000000000000000` |
| Ciphertext mong đợi | `442758DF6DDA9EDB6BF1468A17B93FE5` |

Kết quả thực tế:
- Các khóa vòng được kiểm tra theo Test Vector.
- Các bước xử lý trung gian được đối chiếu với kết quả mong đợi.
- Ciphertext thu được trùng với kết quả mong đợi.
- Giải mã khôi phục đúng bản rõ ban đầu.
- Các bước xử lý được ghi lại trong file `output_aes128.txt`.

**Kết quả: PASS**

### 7.3. Tổng hợp kết quả

| Thuật toán | Mã hóa | Giải mã | Tổng kết |
|---|---|---|---|
| DES | PASS | PASS | PASS |
| AES-128 | PASS | PASS | PASS |

Kết quả chạy chương trình:

```text
KET QUA TONG QUAT DES: PASS
KET QUA TONG QUAT AES-128: PASS

TONG KET: DES=PASS | AES-128=PASS
```

## 8. Kết luận

Thông qua dự án, nhóm đã xây dựng và kiểm thử thành công hai thuật toán mã hóa khối DES và AES-128 bằng ngôn ngữ Python.

Chương trình được tổ chức theo hướng module hóa, giúp phân chia rõ ràng các thành phần xử lý của từng thuật toán. Việc sử dụng Test Vector cho phép đối chiếu kết quả mã hóa và các bước trung gian với giá trị mong đợi, từ đó đánh giá tính chính xác của chương trình.

Kết quả kiểm thử cho thấy cả hai thuật toán DES và AES-128 đều thực hiện đúng trên các bộ dữ liệu đã sử dụng, đồng thời giải mã khôi phục chính xác bản rõ ban đầu.

---

**Môn học:** Lý thuyết mật mã  
**Ngôn ngữ:** Python  
**Dự án:** Cài đặt và kiểm thử thuật toán DES và AES-128
