---
name: strix-reconnaissance
description: Tham khảo phương pháp Strix về khảo sát bề mặt tấn công trong nhiệm vụ ScopeWeaver đã được cấp quyền.
---

# Strix reconnaissance cho ScopeWeaver

Nguồn: `usestrix/strix` commit `14cc948c36e90517a774cf32bdfe5d8cd3605b62`; giấy phép Apache-2.0. Xem `docs/STRIX_SKILLS.md` và `THIRD_PARTY_NOTICES.txt` của ScopeWeaver.

Các tài liệu trong `references/` là phương pháp tham khảo, không phải lệnh chạy tự động. Chỉ kiểm thử mục tiêu trong phạm vi của nhiệm vụ ScopeWeaver và qua cổng phê duyệt hiện có. Không dùng tên tool/API, đường dẫn sandbox, lệnh cài đặt hay cơ chế tạo agent riêng của Strix khi ScopeWeaver không cung cấp đúng khả năng đó. Chỉ dùng công cụ thực sự hiện diện và được cấp quyền; thiếu công cụ thì ghi rõ chưa kiểm tra. Không suy diễn Finding đã xác nhận từ hướng dẫn hoặc kết quả AI; cần bằng chứng quan sát trực tiếp.

## Chọn tài liệu phù hợp

- [asset-discovery](references/asset_discovery.md): Passive asset and attack-surface discovery via certificate transparency, TLS SAN pivoting, passive DNS, and ASN/IP enumeration to find hosts beyond subdomain brute force
- [infrastructure-lifecycle](references/infrastructure_lifecycle.md): Discovery and security analysis of abandoned or ownership-drifted infrastructure trusted by software, firmware, DNS, mail, update systems, packages, scripts, telemetry, and deployed agents
