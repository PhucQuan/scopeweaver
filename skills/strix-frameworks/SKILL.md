---
name: strix-frameworks
description: Tham khảo phương pháp Strix về kiểm thử theo framework trong nhiệm vụ ScopeWeaver đã được cấp quyền.
---

# Strix frameworks cho ScopeWeaver

Nguồn: `usestrix/strix` commit `14cc948c36e90517a774cf32bdfe5d8cd3605b62`; giấy phép Apache-2.0. Xem `docs/STRIX_SKILLS.md` và `THIRD_PARTY_NOTICES.txt` của ScopeWeaver.

Các tài liệu trong `references/` là phương pháp tham khảo, không phải lệnh chạy tự động. Chỉ kiểm thử mục tiêu trong phạm vi của nhiệm vụ ScopeWeaver và qua cổng phê duyệt hiện có. Không dùng tên tool/API, đường dẫn sandbox, lệnh cài đặt hay cơ chế tạo agent riêng của Strix khi ScopeWeaver không cung cấp đúng khả năng đó. Chỉ dùng công cụ thực sự hiện diện và được cấp quyền; thiếu công cụ thì ghi rõ chưa kiểm tra. Không suy diễn Finding đã xác nhận từ hướng dẫn hoặc kết quả AI; cần bằng chứng quan sát trực tiếp.

## Chọn tài liệu phù hợp

- [django](references/django.md): Security testing playbook for Django applications covering ORM injection, middleware gaps, auth/session flaws, and template issues
- [fastapi](references/fastapi.md): Security testing playbook for FastAPI applications covering ASGI, dependency injection, and API vulnerabilities
- [nestjs](references/nestjs.md): Security testing playbook for NestJS applications covering guards, pipes, decorators, module boundaries, and multi-transport auth
- [nextjs](references/nextjs.md): Security testing playbook for Next.js covering App Router, Server Actions, RSC, and Edge runtime vulnerabilities
