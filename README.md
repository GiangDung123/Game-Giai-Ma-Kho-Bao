# 🏆 Game "Giải mã kho báu"

Trò chơi mô phỏng giáo dục giúp người chơi tìm hiểu và áp dụng các thuật toán mã hóa cổ điển và hiện đại: Caesar Cipher, Vigenère Cipher, RSA và AES.

## 🎮 Mục tiêu
- Giúp sinh viên thực hành các kiến thức môn Nhập môn An toàn và Bảo mật Thông tin.
- Làm quen cách mã hóa/giải mã và cách sử dụng thư viện mã hóa trong Python.
- Tăng khả năng tư duy bảo mật thông qua trò chơi tương tác.

## 🚀 Tính năng
✅ 4 cấp độ giải mã:
- **Caesar Cipher**
- **Vigenère Cipher**
- **RSA**
- **AES**

✅ Giao diện Tkinter trực quan:
- Màn hình chọn cấp độ
- Màn hình nhập đáp án
- Thông báo kết quả đúng/sai
- Ghi nhận điểm cao nhất

✅ Mỗi cấp độ có thông điệp là một câu ca dao tiếng Việt.

---

## 🧩 Cấu trúc thư mục

├── main_tkinter.py # Giao diện chính và luồng trò chơi

├── levels.py # Danh sách cấp độ và dữ liệu mã hóa

├── caesar.py # Mã hóa / Giải mã Caesar Cipher

├── vigenere.py # Mã hóa / Giải mã Vigenère Cipher

├── rsa_module.py # Mã hóa / Giải mã RSA

├── aes_module.py # Mã hóa / Giải mã AES

├── highscore.txt # File lưu điểm cao nhất

└── README.md # Hướng dẫn sử dụng



---

## 🛠️ Yêu cầu cài đặt

Python >=3.6

Các thư viện cần thiết:
```bash
pip install pycryptodome
💻 Cách chạy game

python main_tkinter.py
📝 Hướng dẫn sử dụng
Chạy chương trình.

Chọn cấp độ muốn chơi.

Nhập kết quả giải mã.

Nếu đúng: hệ thống chuyển cấp độ tiếp theo.

Nếu sai: hiện đáp án đúng để tham khảo.

🗄️ Tài liệu tham khảo
William Stallings, Cryptography and Network Security

PyCryptodome: https://pycryptodome.readthedocs.io

Tkinter Docs: https://docs.python.org/3/library/tkinter.html

🖋️ Tác giả
Nhóm sinh viên Đại học Đại Nam
GV hướng dẫn: ThS. Lê Thị Thùy Trang


💻 Cách chạy game
bash
Sao chép
Chỉnh sửa
python main_tkinter.py
📝 Hướng dẫn sử dụng
Chạy chương trình.

Chọn cấp độ muốn chơi.

Nhập kết quả giải mã.

Nếu đúng: hệ thống chuyển cấp độ tiếp theo.

Nếu sai: hiện đáp án đúng để tham khảo.

🗄️ Tài liệu tham khảo
William Stallings, Cryptography and Network Security

PyCryptodome: https://pycryptodome.readthedocs.io

Tkinter Docs: https://docs.python.org/3/library/tkinter.html

🖋️ Tác giả
Nhóm sinh viên Đại học Đại Nam
GV hướng dẫn: ThS. Lê Thị Thùy Trang

