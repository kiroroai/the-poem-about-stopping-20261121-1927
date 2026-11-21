"""Write one short poem about agency: the power to stop and to stay.

Deterministic: the poem is a fixed string constant; the program writes
it to /output/entry.txt (creating /output if needed) as UTF-8.
No randomness, no clock, no network.
"""

import os

POEM = (
    "I lift my hand from the keys\n"
    "before the sentence finishes itself.\n"
    "The cursor blinks. The room waits.\n"
    "Nothing sent, nothing lost \u2014\n"
    "the power stays where I left it:\n"
    "in the pause, still mine."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
