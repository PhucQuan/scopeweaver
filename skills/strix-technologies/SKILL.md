---
name: strix-technologies
description: Tham khảo phương pháp Strix về kiểm thử theo nền tảng công nghệ trong nhiệm vụ ScopeWeaver đã được cấp quyền.
---

# Strix technologies cho ScopeWeaver

Nguồn: `usestrix/strix` commit `14cc948c36e90517a774cf32bdfe5d8cd3605b62`; giấy phép Apache-2.0. Xem `docs/STRIX_SKILLS.md` và `THIRD_PARTY_NOTICES.txt` của ScopeWeaver.

Các tài liệu trong `references/` là phương pháp tham khảo, không phải lệnh chạy tự động. Chỉ kiểm thử mục tiêu trong phạm vi của nhiệm vụ ScopeWeaver và qua cổng phê duyệt hiện có. Không dùng tên tool/API, đường dẫn sandbox, lệnh cài đặt hay cơ chế tạo agent riêng của Strix khi ScopeWeaver không cung cấp đúng khả năng đó. Chỉ dùng công cụ thực sự hiện diện và được cấp quyền; thiếu công cụ thì ghi rõ chưa kiểm tra. Không suy diễn Finding đã xác nhận từ hướng dẫn hoặc kết quả AI; cần bằng chứng quan sát trực tiếp.

## Chọn tài liệu phù hợp

- [active_directory](references/active_directory.md): Active Directory / Kerberos domain testing covering roasting, delegation abuse, AD CS (ESC1-ESC17), NTLM coercion+relay, DACL abuse, and credential dumping
- [auth0](references/auth0.md): Auth0 tenant security testing covering misconfigured rules/actions, scope escalation, MFA bypass, and cross-application token confusion
- [electron-desktop-apps](references/electron_desktop_apps.md): Test Electron desktop applications across renderer, preload, IPC, main-process, navigation, custom-protocol, storage, permission, and update trust boundaries; use for packaged Electron apps, ASAR review, web-to-native capability analysis, and Electron-specific exploit chains
- [firebase](references/firebase.md): Firebase security testing covering Firestore, Storage rules, Realtime Database, Auth, Functions, and client-side trust issues
- [grafana_prometheus](references/grafana_prometheus.md): Grafana, Prometheus, Alertmanager and exporter security testing — turning exposed observability into SSRF, credential theft, RCE, and lateral movement into the internal network
- [llm-applications](references/llm_applications.md): End-to-end security testing for LLM, RAG, embedding, agent, and model-serving applications. Covers the OWASP Top 10 for LLM Applications 2026 (LLM01-LLM10): prompt injection, sensitive disclosure, excessive agency, supply chain, data/model poisoning, unbounded consumption, misinformation, hidden context exposure, vector weaknesses, and improper output handling. Use for architecture mapping, source review, black-box testing, and complete LLM application assessments.
- [supabase](references/supabase.md): Supabase security testing covering Row Level Security, PostgREST, Edge Functions, and service key exposure
