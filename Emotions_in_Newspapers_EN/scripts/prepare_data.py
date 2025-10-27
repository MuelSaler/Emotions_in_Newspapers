#!/usr/bin/env python3
"""CLI: Data preparation for 'Emotions_in_Newspapers'.

Tasks:
  1) Convert XML -> TXT
  2) Normalize text
  3) TXT -> TSV (columns: id, text, year, era1, era2)

Usage:
  python scripts/prepare_data.py --input-xml data/xml --out-tsv data/processed/corpus.tsv

Notes:
  - The core logic comes from src/emotions_in_newspapers/dataprep_from_notebook.py.
  - Implement a function run_all(...) there and call it from here.
"""
import argparse
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input-xml', type=Path, required=True, help='Folder with XML files (SBB On this day dataset)')
    ap.add_argument('--out-tsv', type=Path, required=True, help='Output TSV file')
    ap.add_argument('--normalize', action='store_true', help='Apply normalization if available')
    ap.add_argument('--encoding', default='utf-8', help='File encoding')
    ap.add_argument('--year-from-id', action='store_true', help='Extract year from file ID or filename')
    args = ap.parse_args()

    args.out_tsv.parent.mkdir(parents=True, exist_ok=True)
    print("Please implement run_all(...) in src/emotions_in_newspapers/dataprep_from_notebook.py")
    print("Target TSV path:", args.out_tsv)

if __name__ == '__main__':
    main()
