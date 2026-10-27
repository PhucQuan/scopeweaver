"""Đóng gói tài liệu Strix thành skill tương thích với ScopeWeaver.

Chạy với checkout Strix đã kiểm tra, ví dụ:
python tools/import_strix_skills.py --source <strix-repo> --commit <sha>
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path


CATEGORIES = {
    "analysis": "đối chiếu bằng chứng và đánh giá mức độ nghiêm trọng",
    "cloud": "đánh giá môi trường đám mây",
    "custom": "các phương pháp kiểm thử chuyên biệt",
    "frameworks": "kiểm thử theo framework",
    "protocols": "kiểm thử giao thức",
    "reconnaissance": "khảo sát bề mặt tấn công",
    "technologies": "kiểm thử theo nền tảng công nghệ",
    "tooling": "tham khảo cách dùng công cụ",
    "vulnerabilities": "xác minh các lớp lỗ hổng",
}
EXCLUDED = {"coordination", "scan_modes"}


def metadata(content: str) -> tuple[str, str]:
    if not content.startswith("---\n"):
        raise ValueError("Tài liệu Strix thiếu frontmatter")
    frontmatter = content.split("---", 2)[1]
    name = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not name or not description:
        raise ValueError("Tài liệu Strix thiếu name/description")
    return name.group(1).strip().strip('"\''), description.group(1).strip().strip('"\'')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Checkout Strix chính thức")
    parser.add_argument("--commit", required=True, help="Commit đã đối chiếu")
    parser.add_argument("--target", type=Path, default=Path(__file__).resolve().parents[1] / "skills")
    args = parser.parse_args()
    source = args.source.resolve()
    target = args.target.resolve()
    skills = source / "strix" / "skills"
    if not skills.is_dir() or not (source / "LICENSE").is_file():
        parser.error("Nguồn Strix thiếu thư mục skill hoặc LICENSE")
    if not re.fullmatch(r"[0-9a-f]{40}", args.commit):
        parser.error("Commit phải là SHA đầy đủ 40 ký tự")
    actual_commit = subprocess.run(
        ["git", "-C", str(source), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    if actual_commit != args.commit:
        parser.error(f"Commit nguồn khác commit khai báo: {actual_commit}")
    categories = {entry.name for entry in skills.iterdir() if entry.is_dir()}
    if categories != set(CATEGORIES) | EXCLUDED:
        parser.error(f"Danh mục Strix đã thay đổi: {sorted(categories)}")
    if any((target / f"strix-{category}").exists() for category in CATEGORIES):
        parser.error("Skill Strix đã tồn tại; kiểm tra khác biệt trước khi cập nhật")

    manifest: dict[str, list[tuple[Path, str, str]]] = {}
    for category in CATEGORIES:
        source_files = sorted((skills / category).glob("*.md"))
        if not source_files:
            parser.error(f"Danh mục {category} trống")
        manifest[category] = [(original, *metadata(original.read_text(encoding="utf-8")))
                              for original in source_files]

    count = 0
    for category, purpose in CATEGORIES.items():
        destination = target / f"strix-{category}"
        references = destination / "references"
        references.mkdir(parents=True)
        index = []
        for original, name, description in manifest[category]:
            shutil.copyfile(original, references / original.name)
            index.append(f"- [{name}](references/{original.name}): {description}")
            count += 1
        wrapper = (
            "---\n"
            f"name: strix-{category}\n"
            f"description: Tham khảo phương pháp Strix về {purpose} trong nhiệm vụ ScopeWeaver đã được cấp quyền.\n"
            "---\n\n"
            f"# Strix {category} cho ScopeWeaver\n\n"
            f"Nguồn: `usestrix/strix` commit `{args.commit}`; giấy phép Apache-2.0. "
            "Xem `docs/STRIX_SKILLS.md` và `THIRD_PARTY_NOTICES.txt` của ScopeWeaver.\n\n"
            "Các tài liệu trong `references/` là phương pháp tham khảo, không phải lệnh chạy tự động. "
            "Chỉ kiểm thử mục tiêu trong phạm vi của nhiệm vụ ScopeWeaver và qua cổng phê duyệt hiện có. "
            "Không dùng tên tool/API, đường dẫn sandbox, lệnh cài đặt hay cơ chế tạo agent riêng của Strix "
            "khi ScopeWeaver không cung cấp đúng khả năng đó. Chỉ dùng công cụ thực sự hiện diện và được cấp quyền; "
            "thiếu công cụ thì ghi rõ chưa kiểm tra. Không suy diễn Finding đã xác nhận từ hướng dẫn hoặc kết quả AI; "
            "cần bằng chứng quan sát trực tiếp.\n\n"
            "## Chọn tài liệu phù hợp\n\n" + "\n".join(index) + "\n"
        )
        (destination / "SKILL.md").write_text(wrapper, encoding="utf-8")
    print(f"{len(CATEGORIES)} skill groups, {count} references: {target}")


if __name__ == "__main__":
    main()
