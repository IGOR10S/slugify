# slugify

A simple Python script to normalize lines of text and convert them to **slug**.

## Requirements

- Python 3.x
- Standard module `sys`

## Description

`slugify.py` reads a text file line by line and generates a new file where each line is:

- cleaned of leading and trailing spaces
- converted to lowercase
- transformed by replacing spaces with `-`

It is useful for creating slugs, URL-friendly strings, readable identifiers, or for normalizing text lists.

> [!NOTE]
> The script does not change special or accented characters and does not remove symbols other than spaces. It is intended as a minimal and easily extendable utility

## Example

```bash
python3 slugify.py input.txt output.txt
```

input.txt:

```text
Hello World
   Test line
```

output.txt

```text
hello-world
test-line
```
