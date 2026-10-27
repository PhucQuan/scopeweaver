---
name: strix-vulnerabilities
description: Tham khảo phương pháp Strix về xác minh các lớp lỗ hổng trong nhiệm vụ ScopeWeaver đã được cấp quyền.
---

# Strix vulnerabilities cho ScopeWeaver

Nguồn: `usestrix/strix` commit `14cc948c36e90517a774cf32bdfe5d8cd3605b62`; giấy phép Apache-2.0. Xem `docs/STRIX_SKILLS.md` và `THIRD_PARTY_NOTICES.txt` của ScopeWeaver.

Các tài liệu trong `references/` là phương pháp tham khảo, không phải lệnh chạy tự động. Chỉ kiểm thử mục tiêu trong phạm vi của nhiệm vụ ScopeWeaver và qua cổng phê duyệt hiện có. Không dùng tên tool/API, đường dẫn sandbox, lệnh cài đặt hay cơ chế tạo agent riêng của Strix khi ScopeWeaver không cung cấp đúng khả năng đó. Chỉ dùng công cụ thực sự hiện diện và được cấp quyền; thiếu công cụ thì ghi rõ chưa kiểm tra. Không suy diễn Finding đã xác nhận từ hướng dẫn hoặc kết quả AI; cần bằng chứng quan sát trực tiếp.

## Chọn tài liệu phù hợp

- [agentic-system-security](references/agentic_system_security.md): Security testing for authorized AI agents and MCP-style tool ecosystems, covering effective authority, tool/resource/prompt inventory, confused-deputy behavior, side-effect authorization, cross-tenant isolation, executable component supply chain, shadow integrations, and repeatable safety regression
- [argument-injection](references/argument_injection.md): Test shell-free command argument injection across argv builders and CLI parsers, including option smuggling, response/config-file parsing, argument-boundary reparsing, and Windows Unicode-to-ANSI Best-Fit transformations
- [authentication-jwt](references/authentication_jwt.md): JWT and OIDC security testing covering token forgery, algorithm confusion, and claim manipulation
- [broken-function-level-authorization](references/broken_function_level_authorization.md): BFLA testing for action-level authorization failures across endpoints, admin functions, and API operations
- [browser-security](references/browser_security.md): Browser-internals security testing for browsing-context relationships, postMessage, client-side path traversal, XS-Leaks, service workers, Web Workers, navigation behavior, CSP interactions, caches, and cross-origin state machines
- [business-logic](references/business_logic.md): Business logic testing for workflow bypass, state manipulation, and domain invariant violations
- [csrf](references/csrf.md): CSRF testing covering token bypass, SameSite cookies, CORS misconfigurations, and state-changing request abuse
- [header-injection](references/header_injection.md): HTTP header injection testing covering CRLF / response splitting, cache poisoning, Host-header confusion, cookie fixation, and proxy / forwarding header smuggling
- [http-request-smuggling](references/http_request_smuggling.md): HTTP request smuggling testing covering CL.TE, TE.CL, H2.CL, H2.TE, and HTTP/2 desync techniques with practical detection and exploitation methodology
- [idor](references/idor.md): IDOR/BOLA testing for object-level authorization failures and cross-account data access
- [information-disclosure](references/information_disclosure.md): Information disclosure testing covering error messages, debug endpoints, metadata leakage, and source exposure
- [insecure-deserialization](references/insecure_deserialization.md): Insecure deserialization testing for Java, Python, PHP, .NET, Ruby, and Node.js covering gadget chains, type confusion, and safe validation
- [insecure-file-uploads](references/insecure_file_uploads.md): File upload security testing covering extension bypass, content-type manipulation, and path traversal
- [llm-prompt-injection](references/llm_prompt_injection.md): Deep testing for OWASP LLM01:2026 prompt injection in LLM, RAG, multimodal, memory, and tool-using applications, including direct/indirect injection, jailbreaks, instruction smuggling, and downstream impact validation. Use llm_applications for full OWASP 2026 LLM01-LLM10 coverage.
- [mass-assignment](references/mass_assignment.md): Mass assignment testing for unauthorized field binding and privilege escalation via API parameters
- [nosql-injection](references/nosql_injection.md): NoSQL injection testing covering MongoDB operator injection, authentication bypass, blind extraction, GraphQL variable injection, and Redis/DynamoDB/Elasticsearch/Neo4j-specific attack surfaces
- [open-redirect](references/open_redirect.md): Open redirect testing for phishing pivots, OAuth token theft, and allowlist bypass
- [path-traversal-lfi-rfi](references/path_traversal_lfi_rfi.md): Path traversal and file inclusion testing for local/remote file access and code execution
- [prototype-pollution](references/prototype_pollution.md): Client and server prototype pollution testing covering JavaScript object merge bugs, Node.js RCE chains, and filter bypasses
- [race-conditions](references/race_conditions.md): Race condition testing for TOCTOU bugs, double-spend, and concurrent state manipulation
- [rce](references/rce.md): RCE testing covering command injection, deserialization, template injection, and code evaluation
- [semantic-confusion](references/semantic_confusion.md): Cross-component semantic confusion testing for parser differentials, normalization mismatches, overloaded fields, lifecycle state drift, internal redirects, protocol translation, and validator-to-sink inconsistencies
- [sql-injection](references/sql_injection.md): SQL injection testing covering union, blind, error-based, and ORM bypass techniques
- [ssrf](references/ssrf.md): SSRF testing for cloud metadata access, internal service discovery, and protocol smuggling
- [ssti](references/ssti.md): Server-side template injection across Jinja / Mako / Velocity / Freemarker / Thymeleaf / Twig / Handlebars / EJS / ERB with engine fingerprinting, sandbox escape, and RCE gadget chains
- [subdomain-takeover](references/subdomain_takeover.md): Subdomain takeover testing for dangling DNS records and unclaimed cloud resources
- [weak-password-detection](references/weak_password_detection.md): Weak password detection, credential stuffing, and brute-force testing using common passwords, system-generated credentials, and HTTP fuzzing / NSE brute-force tooling
- [xss](references/xss.md): XSS and HTML injection testing covering reflected, stored, DOM-based, and normalization-dependent vectors
- [xxe](references/xxe.md): XXE testing for external entity injection, file disclosure, and SSRF via XML parsers
