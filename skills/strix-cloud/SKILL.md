---
name: strix-cloud
description: Tham khảo phương pháp Strix về đánh giá môi trường đám mây trong nhiệm vụ ScopeWeaver đã được cấp quyền.
---

# Strix cloud cho ScopeWeaver

Nguồn: `usestrix/strix` commit `14cc948c36e90517a774cf32bdfe5d8cd3605b62`; giấy phép Apache-2.0. Xem `docs/STRIX_SKILLS.md` và `THIRD_PARTY_NOTICES.txt` của ScopeWeaver.

Các tài liệu trong `references/` là phương pháp tham khảo, không phải lệnh chạy tự động. Chỉ kiểm thử mục tiêu trong phạm vi của nhiệm vụ ScopeWeaver và qua cổng phê duyệt hiện có. Không dùng tên tool/API, đường dẫn sandbox, lệnh cài đặt hay cơ chế tạo agent riêng của Strix khi ScopeWeaver không cung cấp đúng khả năng đó. Chỉ dùng công cụ thực sự hiện diện và được cấp quyền; thiếu công cụ thì ghi rõ chưa kiểm tra. Không suy diễn Finding đã xác nhận từ hướng dẫn hoặc kết quả AI; cần bằng chứng quan sát trực tiếp.

## Chọn tài liệu phù hợp

- [aws](references/aws.md): AWS cloud security testing covering IAM misconfigurations, S3 exposure, metadata abuse, and privilege escalation paths
- [azure](references/azure.md): Microsoft Azure and Entra security testing covering RBAC, Privileged Identity Management, Conditional Access, service principals, managed identities, Storage SAS, Key Vault, workload escalation, and cross-plane privilege paths
- [gcp](references/gcp.md): GCP cloud security testing covering IAM misconfigurations, public storage buckets, metadata abuse, and service account privilege escalation
- [kubernetes](references/kubernetes.md): Kubernetes cluster security testing - RBAC, API exposure, container escapes, network policies, secrets, and supply chain
