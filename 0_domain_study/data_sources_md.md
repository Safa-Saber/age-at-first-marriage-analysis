# Data Sources

## Primary Source

**Wikipedia**: List of countries by age at first marriage  
**URL**: https://en.wikipedia.org/wiki/List_of_countries_by_age_at_first_marriage  
**Access**: Web scraping with BeautifulSoup  
**Date**: December 2025

---

## Why Wikipedia?

- Global coverage: 192 countries across 5 continents
- Free and public
- Consistent format
- Community-reviewed
- Ideal for educational analysis

---

## Data Structure

| Column | Description |
|--------|-------------|
| Country | Country name |
| Men | Avg age for men |
| Women | Avg age for women |
| Average | Avg age both |
| Age Gap | Men - Women |
| Year | Collection year |

**Coverage**: 48 Asia, 53 Africa, 33 Americas, 44 Europe, 14 Oceania

---

## Data Quality

### Strengths ✅
- Complete for all primary variables
- Clear geographic organization
- Data collection year provided
- Good for descriptive analysis

### Limitations ⚠️
- Data collection years vary (1980-2023)
- No confidence intervals
- Different methodologies by country
- Aggregate data only (no regional breakdowns)

---

## Cleaning Process

- Removed country name formatting (brackets, parentheses)
- Converted ages to numeric values
- Dropped rows with missing critical data
- Standardized data types

---

## What Data Shows & Doesn't Show

### Shows ✅
- Average marriage ages by country
- Gender differences
- Continental patterns

### Doesn't Show ✗
- Why patterns exist
- Causal relationships
- Future predictions
- Individual variation

---

## Reproducibility

Clone repo and run:
```bash
pip install -r requirements.txt
python 2_data_preparation/data_cleaning.py
```

Cleaned CSV files in: `1_datasets/cleaned/`

---

## Citation

> Saber, S. (2025). Age at First Marriage: Global Analysis. Data from Wikipedia: List of countries by age at first marriage. https://github.com/Safa-Saber/age-at-first-marriage-analysis

---

**Status**: Complete ✅  
**Created**: December 2025