---
name: strix-analysis
description: Tham khảo phương pháp Strix về đối chiếu bằng chứng và đánh giá mức độ nghiêm trọng trong nhiệm vụ ScopeWeaver đã được cấp quyền.
---

# Strix analysis cho ScopeWeaver

Nguồn: `usestrix/strix` commit `14cc948c36e90517a774cf32bdfe5d8cd3605b62`; giấy phép Apache-2.0. Xem `docs/STRIX_SKILLS.md` và `THIRD_PARTY_NOTICES.txt` của ScopeWeaver.

Các tài liệu trong `references/` là phương pháp tham khảo, không phải lệnh chạy tự động. Chỉ kiểm thử mục tiêu trong phạm vi của nhiệm vụ ScopeWeaver và qua cổng phê duyệt hiện có. Không dùng tên tool/API, đường dẫn sandbox, lệnh cài đặt hay cơ chế tạo agent riêng của Strix khi ScopeWeaver không cung cấp đúng khả năng đó. Chỉ dùng công cụ thực sự hiện diện và được cấp quyền; thiếu công cụ thì ghi rõ chưa kiểm tra. Không suy diễn Finding đã xác nhận từ hướng dẫn hoặc kết quả AI; cần bằng chứng quan sát trực tiếp.

## Chọn tài liệu phù hợp

- [counterevidence](references/counterevidence.md): Closure discipline for security findings — what counts as proof of safety, what does not, and how to record an unresolved candidate instead of silently dropping it
- [fix_verification](references/fix_verification.md): How to verify a proposed code fix before shipping it — the ordered gates, what disqualifies a fix, and when to withhold the suggestion instead
- [severity-calibration](references/severity_calibration.md): Qualitative rubric for what actually deserves high/critical severity, and an acceptance checklist to apply before rating a finding
- [source_aware_discovery](references/source_aware_discovery.md): Enumeration discipline for reading code — which locations to keep as separate candidates, which safe siblings prove nothing, and the per-family sweeps that are routinely missed
