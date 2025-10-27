# Emotions_in_Newspapers

This project analyzes emotions in articles from the German newspaper **Der Tag** (1911–1919).
It originated during the hackathon *culture.explore(data)* at the Berlin State Library (*Staatsbibliothek zu Berlin*).

The repository provides a **reproducible data pipeline** for:
1. **Data Preparation**: XML ➜ TXT ➜ normalization ➜ TSV (columns: `id`, `text`, `year`, ...)
2. **Classification**: Use the emotion classifier developed by *Leonard Konle et al., University of Würzburg*
3. **Merging and Metadata**: Merge classification results, clean one-word lines, add era information
4. **Visualization**: Generate time series and significance visualizations

## Quickstart

```bash
git clone <this-repo>
cd Emotions_in_Newspapers
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

**Download data (manual step):**
- Get the corpus from: https://lab.sbb.berlin/on-this-day/
- Place XML files in `data/raw/xml/` (create the folder if needed).

### 1) Data Preparation
```bash
python scripts/prepare_data.py --input-xml data/raw/xml --out-tsv data/processed/corpus.tsv --normalize --year-from-id
```

### 2) Emotion Classification (external)
- Follow the instructions from the Würzburg classifier repository.
- Use `data/processed/corpus.tsv` as input.
- Place resulting TSV files under `results/` (e.g., `results/run1.tsv`).

### 3) Merge and Add Metadata
```bash
python scripts/merge_classifier_outputs.py \
  --corpus data/processed/corpus.tsv \
  --inputs results/run1.tsv \
  --out data/processed/merged.tsv \
  --config config/eras.yaml \
  --drop-single-word-lines
```

### 4) Visualization
```bash
python scripts/visualize.py --input data/processed/merged.tsv --outdir reports/figures
```

Or run everything through Snakemake:
```bash
snakemake -j 1
```

## Project Structure

```text
Emotions_in_Newspapers/
├─ src/emotions_in_newspapers/
│  ├─ dataprep_from_notebook.py
│  └─ visualize_from_notebook.py
├─ scripts/
│  ├─ prepare_data.py
│  ├─ merge_classifier_outputs.py
│  └─ visualize.py
├─ config/eras.yaml
├─ data/
│  ├─ raw/xml/
│  └─ processed/
├─ results/
├─ reports/figures/
├─ requirements.txt
├─ Snakefile
├─ Makefile
└─ README.md
```

## Configuration of Eras

Era boundaries are defined in `config/eras.yaml`.  
Adjust the years for:
- **pre-war / war / post-war periods**
- **pre-/post-Hugenberg era**

The Hugenberg cutoff year is a placeholder (`null`); please replace it with the correct value based on historical research.

## Data Format (TSV)

Expected columns in `data/processed/corpus.tsv`:
- `id` (from filename)
- `text`
- `year` (extracted from ID or metadata)
- optional: `era1`, `era2`

After merging (`data/processed/merged.tsv`), additional columns include:
- emotion columns (e.g., `emo_anger`, `emo_joy`, ... depending on classifier output)
- `era_war` (`pre_war` / `war` / `post_war`)
- `era_hugenberg` (`pre_hugenberg` / `post_hugenberg`)

## Reproducibility and Reuse

- Notebook logic was mirrored into **modules** under `src/` for versioning and reuse.
- **Wrapper scripts** in `scripts/` provide stable command-line entry points.
- **Configuration files** replace hardcoded parameters.
- **Filtering option** (`--drop-single-word-lines`) removes single-word rows, which the classifier struggles with.
- **Documentation** explains every step from raw data to visual output.

## Citation

If you use this repository or parts of it, please acknowledge:
- *culture.explore(data) Hackathon @ Staatsbibliothek zu Berlin*
- *Leonard Konle et al., University of Würzburg, Emotion Classifier*

## License

Licensed under the **Creative Commons Attribution‑ShareAlike 4.0 International (CC BY‑SA 4.0)** license.  
See [LICENSE](LICENSE) for details.
