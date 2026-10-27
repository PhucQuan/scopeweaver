# Bộ phương pháp Strix trong ScopeWeaver

Bản tham chiếu lấy từ [usestrix/strix](https://github.com/usestrix/strix) tại commit
`14cc948c36e90517a774cf32bdfe5d8cd3605b62` (đối chiếu ngày 24/10/2026).
Nguồn có 75 tài liệu skill; ScopeWeaver đóng gói 69 tài liệu thuộc chín nhóm thành
`skills/strix-*`. Sáu tài liệu `coordination` và `scan_modes` không được nhập vì
chúng yêu cầu cơ chế tạo agent, điều phối và ngân sách riêng của Strix. Bản gốc
được giữ nguyên trong `references/`; `SKILL.md` là lớp hướng dẫn tương thích.
Giấy phép của tài liệu nguồn là Apache-2.0, xem
[bản giấy phép](third_party/STRIX_APACHE-2.0.txt) và
`THIRD_PARTY_NOTICES.txt` ở thư mục gốc ScopeWeaver.

Các nhóm hiện có: `strix-analysis`, `strix-cloud`, `strix-custom`,
`strix-frameworks`, `strix-protocols`, `strix-reconnaissance`,
`strix-technologies`, `strix-tooling` và `strix-vulnerabilities`.

## Dùng trên ScopeWeaver

Thư mục skill được nạp qua API và cơ chế Skill của ScopeWeaver. Việc có thư mục
trên máy **không tự cấp quyền sử dụng** cho agent: quản trị viên phải chọn các
nhóm phù hợp trong phần hiển thị skill của từng agent. Chỉ bật trong nhiệm vụ đã
khai báo phạm vi và quyền kiểm thử. Nội dung Strix là phương pháp tham khảo;
lệnh, API tạo agent, đường dẫn sandbox và công cụ riêng của Strix không tự xuất
hiện trong ScopeWeaver. Nếu thiếu công cụ hoặc bằng chứng trực tiếp, báo là chưa
kiểm tra thay vì tạo Finding đã xác nhận.

Ảnh Docker có bản gốc tại `/app/bundled-skills` và dùng `/app/skills` để lưu
thay đổi của người dùng. Khi khởi động với volume cũ, `start.sh` chỉ sao chép
nhóm Strix còn thiếu; nó không ghi đè skill đã chỉnh qua giao diện. Vì vậy cần
build lại ảnh ScopeWeaver và khởi động lại dịch vụ ở máy `.61`, sau đó kiểm tra
`GET /api/skills` và bật quyền hiển thị cho agent muốn dùng. Nếu nhóm Strix đã
tồn tại từ lần trước, hãy so sánh và cập nhật có chủ đích; khởi động lại không
tự ghi đè bản đã sửa.

## Cập nhật từ Strix

Lấy checkout chính thức tại commit muốn dùng, đọc thay đổi và giấy phép, rồi
chạy `python tools/import_strix_skills.py --source <checkout> --commit <sha>`
trên một bản làm việc **chưa có** các thư mục `strix-*`. Công cụ từ chối ghi đè
để bảo vệ các sửa đổi tại ScopeWeaver. Đối chiếu tài liệu mới, kiểm tra phụ thuộc
và triển khai có chủ đích. Không tự động tải skill mới ở thời điểm agent chạy.
