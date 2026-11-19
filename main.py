"""Vice City Dawn — write the 19 Nov 2026 front-page image to disk.

Reads entry.png.b64 next to this script, decodes it, and writes
entry.png into MAKEFUN_OUTPUT_DIR (default /output). Pure stdlib.
"""

import base64
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(HERE, "entry.png.b64"), "rb") as f:
        data = base64.b64decode(f.read())
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("decoded data is not a PNG image")
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes)" % (out_path, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
