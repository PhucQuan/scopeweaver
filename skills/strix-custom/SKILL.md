---
name: strix-custom
description: Tham khảo phương pháp Strix về các phương pháp kiểm thử chuyên biệt trong nhiệm vụ ScopeWeaver đã được cấp quyền.
---

# Strix custom cho ScopeWeaver

Nguồn: `usestrix/strix` commit `14cc948c36e90517a774cf32bdfe5d8cd3605b62`; giấy phép Apache-2.0. Xem `docs/STRIX_SKILLS.md` và `THIRD_PARTY_NOTICES.txt` của ScopeWeaver.

Các tài liệu trong `references/` là phương pháp tham khảo, không phải lệnh chạy tự động. Chỉ kiểm thử mục tiêu trong phạm vi của nhiệm vụ ScopeWeaver và qua cổng phê duyệt hiện có. Không dùng tên tool/API, đường dẫn sandbox, lệnh cài đặt hay cơ chế tạo agent riêng của Strix khi ScopeWeaver không cung cấp đúng khả năng đó. Chỉ dùng công cụ thực sự hiện diện và được cấp quyền; thiếu công cụ thì ghi rõ chưa kiểm tra. Không suy diễn Finding đã xác nhận từ hướng dẫn hoặc kết quả AI; cần bằng chứng quan sát trực tiếp.

## Chọn tài liệu phù hợp

- [api_spec_testing](references/api_spec_testing.md): Spec-driven API pentesting — systematically exercise every endpoint from an ingested OpenAPI/Swagger/Postman inventory for authz, injection, and business-logic flaws
- [dependency-cve-scanning](references/dependency_cve_scanning.md): Supply-chain / SCA playbook — scan repository lockfiles for known dependency CVEs and report them with create_dependency_report (no dynamic PoC required)
- [npx-confusion](references/npx_confusion.md): Test package and executable identity confusion in npx, npm exec, and bunx fallback, plus explicit auto-fetch runners such as pnpm/yarn dlx and deno run npm:, with runner-specific resolution analysis, registry-state controls, reporting gates, and false-positive elimination
- [source-aware-sast](references/source_aware_sast.md): Practical source-aware SAST and AST playbook for semgrep, ast-grep, gitleaks, and trivy fs
