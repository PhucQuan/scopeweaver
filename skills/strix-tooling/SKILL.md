---
name: strix-tooling
description: Tham khảo phương pháp Strix về tham khảo cách dùng công cụ trong nhiệm vụ ScopeWeaver đã được cấp quyền.
---

# Strix tooling cho ScopeWeaver

Nguồn: `usestrix/strix` commit `14cc948c36e90517a774cf32bdfe5d8cd3605b62`; giấy phép Apache-2.0. Xem `docs/STRIX_SKILLS.md` và `THIRD_PARTY_NOTICES.txt` của ScopeWeaver.

Các tài liệu trong `references/` là phương pháp tham khảo, không phải lệnh chạy tự động. Chỉ kiểm thử mục tiêu trong phạm vi của nhiệm vụ ScopeWeaver và qua cổng phê duyệt hiện có. Không dùng tên tool/API, đường dẫn sandbox, lệnh cài đặt hay cơ chế tạo agent riêng của Strix khi ScopeWeaver không cung cấp đúng khả năng đó. Chỉ dùng công cụ thực sự hiện diện và được cấp quyền; thiếu công cụ thì ghi rõ chưa kiểm tra. Không suy diễn Finding đã xác nhận từ hướng dẫn hoặc kết quả AI; cần bằng chứng quan sát trực tiếp.

## Chọn tài liệu phù hợp

- [agent_browser](references/agent_browser.md): agent-browser CLI for headless Chrome via shell. Snapshot-and-ref workflow, click/fill/extract, screenshots, multi-tab, multi-session, network mocking. Pre-installed in the sandbox; invoke via exec_command.
- [ffuf](references/ffuf.md): ffuf fuzzing syntax with matcher/filter strategy and non-interactive defaults.
- [httpx](references/httpx.md): ProjectDiscovery httpx probing syntax, exact probe flags, and automation-safe output patterns.
- [hurl](references/hurl.md): Reproducible, reviewable HTTP request chains and response assertions with Hurl for authorized multi-step security validation, vulnerable-versus-fixed regression cases, captured values, and low-rate semantic oracles
- [hypothesis](references/hypothesis.md): Property-based local differential testing with Hypothesis for parsers, canonicalizers, serializers, validators, routers, and other pure functions, emphasizing explicit invariants, shrinking, reproducibility, and bounded resource use
- [katana](references/katana.md): Katana crawler syntax, depth/js/known-files behavior, and stable concurrency controls.
- [naabu](references/naabu.md): Naabu port-scanning syntax with host input, scan-type, verification, and rate controls.
- [nmap](references/nmap.md): Canonical Nmap CLI syntax, two-pass scanning workflow, and sandbox-safe bounded scan patterns.
- [nuclei](references/nuclei.md): Exact Nuclei command structure, template selection, and bounded high-throughput execution controls.
- [python](references/python.md): Run Python through exec_command in the SDK sandbox. Use the image-baked caido_api module for Caido proxy automation from Python scripts.
- [semgrep](references/semgrep.md): Exact Semgrep CLI structure, metrics-off scanning, scoped ruleset selection, and automation-safe output patterns.
- [sqlmap](references/sqlmap.md): sqlmap target syntax, non-interactive execution, and common validation/enumeration workflows.
- [subfinder](references/subfinder.md): Subfinder passive subdomain enumeration syntax, source controls, and pipeline-ready output patterns.
