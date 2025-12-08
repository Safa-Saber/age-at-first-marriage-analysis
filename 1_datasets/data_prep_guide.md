# Guide: Data Preparation - Web Scraping

Quick reference for scraping marriage age data from Wikipedia.

---

## What This Folder Does

Scrapes marriage age data from Wikipedia and saves it as raw CSV files by continent.

---

## Files in This Folder

- **web_scraping.py** - Main scraping script
- **README.md** - Detailed documentation
- **guide.md** - This quick reference

---

## Quick Start

### Run the Script

```bash
python web_scraping.py
```

### What Happens

1. Connects to Wikipedia
2. Finds marriage age tables
3. Extracts data for all continents
4. Saves 5 CSV files (one per continent)

### Output Location

```
1_datasets/raw/
├── raw_Asia.csv
├── raw_Africa.csv
├── raw_Americas.csv
├── raw_Europe.csv
└── raw_Oceania.csv
```

---

## Requirements

Install before running:

```bash
pip install -r requirements.txt
```

**Needed packages**:
- requests
- beautifulsoup4
- pandas

---

## Script Overview

### Step 1: Fetch Webpage
Connects to Wikipedia with appropriate headers.

### Step 2: Extract Tables
Finds continent sections and their data tables.

### Step 3: Parse Data
Extracts columns: Country, Men, Women, Average, Age Gap, Age Ratio, Year

### Step 4: Save CSV
Saves raw (unmodified) data to CSV files.

---

## Output Details

### File Naming
- Format: `raw_[Continent].csv`
- Examples: `raw_Asia.csv`, `raw_Africa.csv`

### Data Format
- Exactly as it appears on Wikipedia
- Country names may contain brackets `[b]` or parentheses `(note)`
- Numbers stored as text

### Records Per Continent
- Asia: 48 countries
- Africa: 53 countries
- Americas: 33 countries
- Europe: 44 countries
- Oceania: 14 countries
- **Total: 192 countries**

---

## Troubleshooting

**Script won't run?**
- Check internet connection
- Verify Wikipedia is accessible
- Ensure pandas and requests are installed

**No output files?**
- Check `1_datasets/raw/` folder exists
- Verify write permissions
- Check disk space

**Empty CSV files?**
- Website structure may have changed
- Check Wikipedia page directly

---

## Data Source

**URL**: https://en.wikipedia.org/wiki/List_of_countries_by_age_at_first_marriage

**Access**: Public, no login required

**Ethics**: 
- Follows robots.txt
- Non-commercial use
- Educational purposes

---

## What's Next?

Raw CSV files are ready for further processing.

See: README.md for detailed information

---

**Status**: ✅ Complete  
**Purpose**: Web scraping only  
**Output**: Raw CSV files by continent