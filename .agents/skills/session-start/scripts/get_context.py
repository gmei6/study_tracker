import os


def read_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as f:
        return f.read().strip()


def main():
    files_to_read = [
        "AGENTS.md",
        "okf/index.md",
        "okf/status.md",
        "okf/next-actions.md",
        "okf/open-questions.md",
        "DASHBOARD.md",
        "review/QUEUE.md",
        "review/BLOCKERS.md",
    ]

    output = []
    for filepath in files_to_read:
        content = read_file(filepath)
        if content:
            output.append(f"=== {filepath} ===")
            output.append(content)
            output.append("")

    if not output:
        print("No context files found — run from the study_tracker repo root.")
    else:
        print("\n".join(output))


if __name__ == "__main__":
    main()
