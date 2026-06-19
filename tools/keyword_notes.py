from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class KeywordNote:
    keyword: str
    source_url: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_formatted_string(self) -> str:
        lines = [
            f"Keyword: {self.keyword}",
            f"URL: {self.source_url}",
            f"Content: {self.content}",
            f"Tags: {', '.join(self.tags) if self.tags else 'None'}",
            f"Created: {self.created_at}",
        ]
        return "\n".join(lines)


def format_notes(notes: List[KeywordNote], sort_by: str = "keyword") -> str:
    if not notes:
        return "No notes to display."

    if sort_by == "keyword":
        sorted_notes = sorted(notes, key=lambda n: n.keyword.lower())
    elif sort_by == "created":
        sorted_notes = sorted(notes, key=lambda n: n.created_at or "")
    else:
        sorted_notes = notes

    result_parts = []
    for note in sorted_notes:
        result_parts.append(note.to_formatted_string())
        result_parts.append("---")
    return "\n".join(result_parts)


def create_sample_notes() -> List[KeywordNote]:
    return [
        KeywordNote(
            keyword="华体会",
            source_url="https://officialm-hth.com.cn",
            content="华体会官方入口与最新活动信息汇总",
            tags=["sports", "events", "official"],
        ),
        KeywordNote(
            keyword="华体会客服",
            source_url="https://officialm-hth.com.cn/support",
            content="用户支持与常见问题解答",
            tags=["support", "contact"],
        ),
        KeywordNote(
            keyword="华体会下载",
            source_url="https://officialm-hth.com.cn/download",
            content="最新版本客户端下载链接",
            tags=["download", "app"],
        ),
    ]


def main():
    notes = create_sample_notes()
    print("=== Sorted by keyword ===")
    print(format_notes(notes, sort_by="keyword"))
    print()
    print("=== Sorted by created time ===")
    print(format_notes(notes, sort_by="created"))


if __name__ == "__main__":
    main()