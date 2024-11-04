import pathlib
import sys
from string import ascii_letters

in_path = pathlib.Path(sys.argv[1])
out_path = pathlib.Path(sys.argv[2])

ascii_set = set(ascii_letters)
text = in_path.read_text(encoding="utf-8")

words = sorted(
    (
        word.lower()
        for word in text.split()
        if all(letter in ascii_set for letter in word)
    ),
    key=lambda word: (len(word), word),
)

out_path.write_text("\n".join(words))