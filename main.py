"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code
breaks in production to /output/entry.txt. No network, deterministic.
"""

import os

# The joke: staging passing proves nothing — production is where real
# users, real data, and real consequences live, so "it worked in staging"
# is the classic developer excuse when it breaks on release day.
ENTRY = "It worked in staging because staging has no users, no data, and no consequences."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Validate the entry and write it to OUTPUT_PATH."""
    assert ENTRY and ENTRY.strip() == ENTRY, "entry must be non-empty with no surrounding whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 280, "entry must fit in one short line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Confirm the file round-trips exactly, with no added newline.
    with open(OUTPUT_PATH, encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY, "written entry does not match ENTRY"


if __name__ == "__main__":
    main()
