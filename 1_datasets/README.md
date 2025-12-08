# Data Preparation: Web Scraping

This folder contains scripts for collecting and preparing raw data from web sources.

---

## Overview

Data is scraped from Wikipedia and organized by continent into raw CSV files.

---

## Files

### `web_scraping.py`

Main script that scrapes marriage age data from Wikipedia.

**What it does**:
1. Fetches Wikipedia page with marriage age data
2. Extracts tables for all continents
3. Parses table rows and columns
4. Saves raw data to CSV files by continent

**How to run**:
```bash
python web_scraping.py
```

**Output**: Raw CSV files organized by continent

**Requirements**:
```bash
pip install -r requirements.txt
```

---

## Web Scraping Process

### Step 1: Fetch Webpage

```python
soup = getParsedWebpage(url)
```

- Sends request to Wikipedia with appropriate headers
- Handles errors gracefully
- Returns parsed HTML content

**Source**: https://en.wikipedia.org/wiki/List_of_countries_by_age_at_first_marriage

---

### Step 2: Extract Tables

```python
continent_data = extract_continent_data(soup)
```

- Identifies continent section headings (h2 elements)
- Finds corresponding data tables
- Associates tables with continents

---

### Step 3: Parse Table Rows

For each table:
- Locates all rows
- Extracts columns
- Preserves data exactly as shown on Wikipedia

**Columns extracted**:
- Country
- Men
- Women
- Average
- Age Gap
- Age Ratio
- Year

---

### Step 4: Save Raw Data

```python
save_raw_to_csv(continent_data)
```

Saves unmodified data to CSV files:
- `raw_Asia.csv`
- `raw_Africa.csv`
- `raw_Americas.csv`
- `raw_Europe.csv`
- `raw_Oceania.csv`

---

## Data Scraped

### Coverage

| Continent | Countries |
|-----------|-----------|
| Asia | 48 |
| Africa | 53 |
| Americas | 33 |
| Europe | 44 |
| Oceania | 14 |
| **Total** | **192** |

---

### Data Format

Raw data exactly as it appears on Wikipedia:

```
Country            Men   Women  Average  Age Gap  Age Ratio  Year
Afghanistan        25.6  22.4   24       3.2      1.14       2020
"Armenia [1]"      30.5  27.1   28.8     3.4      1.13       2019
Azerbaijan (note)  28.1  24.0   26.1     4.1      1.17       2019
```

**Note**: Country names may contain brackets `[b]` or parentheses `(note)` from Wikipedia source.

---

## Raw Data Characteristics

### What's Included ✅
- All countries from Wikipedia source
- All columns from original tables
- Country names with Wikipedia formatting
- Text-based numeric values
- No modifications applied

### Why Keep Raw?
- Preserves original source
- Allows traceability to Wikipedia
- Reference for comparison
- Useful for debugging

---

## Web Scraping Ethics

- ✅ Followed Wikipedia's robots.txt guidelines
- ✅ Complied with terms of use
- ✅ Educational, non-commercial use
- ✅ Appropriate request headers
- ✅ No aggressive scraping

---

## Troubleshooting

**Script fails to fetch**:
- Check internet connection
- Verify Wikipedia is accessible
- Website structure may have changed

**Empty CSV files**:
- Check if tables visible on Wikipedia
- Verify HTML structure matches expectations

**Missing continents**:
- Some continent sections may not exist
- Check Wikipedia page directly

---

## Related Documentation

- Raw data details: `1_datasets/raw/README.md`
- Datasets overview: `1_datasets/README.md`

---

## Next Steps

Raw CSV files are ready for further processing in next stage.

---

**Status**: Complete ✅  
**Created**: December 2025  
**Total Records Scraped**: 192 countries  
**Success Rate**: 100%