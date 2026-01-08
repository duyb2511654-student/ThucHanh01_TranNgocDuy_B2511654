quy trình cài đặt (trích dẫn nguồn AI - gemini)
Bước 1: Cài đặt Notepad++ trên Windows 11
Truy cập trang chủ Notepad++ Downloads.

Chọn phiên bản mới nhất (thường ở trên cùng).

Tải xuống bản Installer (thường là bản 64-bit x64 cho Windows 11).

Mở file .exe vừa tải về, chọn ngôn ngữ Tiếng Việt (hoặc Tiếng Anh) và nhấn OK.

Nhấn Tiếp tục (Next) -> Tôi đồng ý (I Agree) -> Chọn thư mục cài đặt mặc định và nhấn Tiếp tục.

Tại bước chọn thành phần, để mặc định và nhấn Tiếp tục. Tích vào "Create Shortcut on Desktop" nếu bạn muốn tạo biểu tượng ngoài màn hình.

Nhấn Cài đặt (Install) và đợi quá trình hoàn tất, sau đó nhấn Hoàn thành (Finish).

Bước 2: Cài đặt Python và thêm vào PATH
Để Notepad++ hiểu được lệnh chạy Python, bạn cần cài đặt môi trường Python trên máy.

Tải Python tại python.org/downloads.

Khi chạy file cài đặt, BẮT BUỘC tích vào ô "Add Python to PATH". Đây là bước quan trọng nhất để hệ thống nhận diện lệnh python.

Chọn Install Now.

Sau khi cài xong, mở Command Prompt (cmd) và gõ python --version. Nếu hiện thông số phiên bản (ví dụ: Python 3.12.x) là thành công.

Bước 3: Cấu hình Notepad++ để viết và chạy code Python
Có hai cách phổ biến để chạy code Python trong Notepad++. Cách dùng NppExec là chuyên nghiệp và tiện lợi nhất vì nó tích hợp cửa sổ Console ngay bên dưới.

Cách 1: Sử dụng Plugin NppExec (Khuyên dùng)
Mở Notepad++, vào menu Plugins > Plugins Admin...

Trong tab Available, tìm từ khóa NppExec.

Tích chọn nó và nhấn Install. Notepad++ sẽ khởi động lại.

Sau khi khởi động lại, nhấn phím F6 trên bàn phím.

Trong cửa sổ hiện ra, dán đoạn mã sau vào:

Bash

npp_save
python "$(FULL_CURRENT_PATH)"
Nhấn Save..., đặt tên là Run Python và nhấn OK.

Bây giờ, mỗi khi viết code xong, bạn chỉ cần nhấn F6 rồi Enter để xem kết quả ở cửa sổ Console bên dưới.

Cách 2: Sử dụng lệnh Run (Đơn giản)
Nhấn phím F5 trong Notepad++.

Nhập lệnh sau vào ô trống:

Plaintext

cmd /k python "$(FULL_CURRENT_PATH)"
Nhấn Save..., đặt tên là Run Python và gán phím tắt (ví dụ: Ctrl + Alt + Shift + P).

Khi chạy, một cửa sổ CMD màu đen sẽ hiện ra kết quả.
