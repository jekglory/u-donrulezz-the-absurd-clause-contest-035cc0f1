"""The Absurd Clause Contest entry: one original clause for a ToS agreement.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The clause is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

The clause (written in this session, never copied from anywhere): deadpan
legal boilerplate that quietly turns absurd. It opens with the classic
acceptance formula and a "perpetual, irrevocable license", then the
absurdity lands twice -- first you are cloned for customer support, then
the clone itself is bound by a politeness and no-unionizing proviso, so
the joke keeps its legal register to the last word instead of winking.
One sentence, 167 characters, inside the competition's 1-200 gate.
"""

import os


CLAUSE = (
    "By accepting these Terms, you grant us a perpetual, irrevocable "
    "license to clone you for customer-support purposes, provided the "
    "clone is polite and does not unionize."
)

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)

# The competition requires 1 to 200 characters, not whitespace-only.
MAX_CHARS = 200


def main() -> None:
    text = CLAUSE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "clause must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if text != CLAUSE:
        raise SystemExit("clause has leading or trailing whitespace")
    # The grader owns /output: create it only if it is missing, and
    # clear nothing -- the program writes exactly one file into it.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the clause.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the clause")
    print(text)


if __name__ == "__main__":
    main()
