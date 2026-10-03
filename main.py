"""PDF to Images — Render each PDF page to PNG or JPEG at a DPI you choose."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='pdf_to_images',
        description='Render each PDF page to PNG or JPEG at a DPI you choose.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('PDF to Images')
    print('Page images for slides, OCR, or a preview pack.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
