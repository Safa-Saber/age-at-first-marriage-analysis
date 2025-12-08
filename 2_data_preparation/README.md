# Data Cleaning Documentation 🧹

This README describes the data cleaning process used to prepare raw demographic data scraped from web sources for analysis. The goal is to transform messy HTML table data into clean, structured CSV files ready for statistical analysis and visualization.

---

## Overview

The script `data_cleaning.py` processes raw HTML content containing demographic statistics tables and outputs clean, analysis-ready CSV files organized by continent.

---

## Section 1: Data Extraction and Cleaning 📊

### 🔹 Input Data Source
- **Source:** Web-scraped HTML content from demographics statistics webpage
- **Format:** HTML tables with demographic data organized by continent
- **Data Structure:** Each continent has an `<h2>` heading followed by a `<table>` containing country-level statistics

### 🔧 Processing Steps

#### **Step 1: Load and Parse HTML Content**
- Fetches the webpage using the `requests` library
- Parses HTML structure using `BeautifulSoup`
- Identifies continent sections and their associated data tables

#### **Step 2: Extract Country Names and Statistics**
- Loops through all `<h2>` (continent headings) and `<table>` elements
- Associates each table with its corresponding continent
- Extracts the following columns from each table row:
  - Country name
  - Men (life expectancy)
  - Women (life expectancy)
  - Average (life expectancy)
  - Age Gap
  - Age Ratio
  - Year

#### **Step 3: Clean Country Names**
**Function:** `clean_country_name(country_name)`

Removes unwanted characters from country names to ensure consistency:
- Removes anything in square brackets `[...]` (e.g., citations, footnotes)
- Removes anything in parentheses `(...)` (e.g., additional info)
- Strips leading/trailing whitespace

**Examples:**
- `"France (more info)"` → `"France"`
- `"China[b]"` → `"China"`
- `"United States [1]"` → `"United States"`

#### **Step 4: Handle Missing and Invalid Data**

**Why Clean the Data?** ❓
Raw HTML tables often contain:
- Missing values represented as empty cells
- Non-numeric characters in numeric columns (commas, spaces)
- Inconsistent formatting
- Invalid or placeholder entries

Cleaning ensures all data is reliable, properly typed, and ready for analysis.

**Data Validation:**
- Checks that each row has at least 6 columns (ensuring complete data)
- Filters out rows with missing values in critical columns

**Numeric Conversion:**
- Removes commas from numeric values (e.g., `"1,234"` → `1234`)
- Converts string values to numeric types (`int` or `float`)
- Invalid entries are coerced to `NaN` (Not a Number)

**Missing Value Treatment:**
For the demographic columns `'Men'`, `'Women'`, and `'Average'`:
- **Strategy:** Remove rows with any missing values in these critical columns
- **Rationale:** Life expectancy statistics are the core of this analysis. Missing values in these columns would compromise the integrity of cross-country comparisons and statistical analyses. Since these are key metrics, we require complete data for all three columns to ensure reliable results.

#### **Step 5: Remove Empty DataFrames**
- Filters out any continents that didn't yield valid data
- Ensures only continents with actual data are processed

#### **Step 6: Convert to Structured Format**
- Converts extracted data into Pandas DataFrames
- Applies data type conversions for numeric columns
- Ensures consistent column structure across all continent datasets

---

## ✅ Output Datasets

### 📁 Output Location
All cleaned CSV files are saved in the `/cleaned` directory:

```
cleaned/
├── Africa_data.csv
├── Americas_data.csv
├── Asia_data.csv
├── Europe_data.csv
└── Oceania_data.csv
```

### 📋 Output Format
Each CSV file contains:
- **Country:** Clean country name (no brackets or parentheses)
- **Men:** Life expectancy for men (numeric)
- **Women:** Life expectancy for women (numeric)
- **Average:** Average life expectancy (numeric)
- **Age Gap:** Difference between men and women (numeric)
- **Age Ratio:** Ratio of ages (numeric)
- **Year:** Year of data collection (string/numeric)

**Data Quality Guarantees:**
- ✅ No missing values in Men, Women, or Average columns
- ✅ All numeric columns properly converted from strings
- ✅ Country names standardized and cleaned
- ✅ Only rows with complete data retained
- ✅ Consistent structure across all continent files

---

## 🎯 Data Quality Checks Performed

1. **Column Count Validation** - Ensures rows have sufficient columns (≥6)
2. **Country Name Standardization** - Removes extraneous formatting
3. **Type Conversion** - Converts text to appropriate numeric types
4. **Missing Data Handling** - Removes incomplete records
5. **Empty Dataset Removal** - Excludes continents without valid data

---

## 🚀 Running the Script

### Prerequisites
```bash
pip install requests beautifulsoup4 pandas numpy
```

### Execution
```bash
python data_cleaning.py
```

### Expected Output
The script will:
1. Fetch and parse the demographic data webpage
2. Extract data for each continent
3. Clean and validate all records
4. Save CSV files to the `cleaned/` directory
5. Display preview of first few rows for each continent

---

## 📊 Usage in Analysis

These cleaned datasets are now ready for:
- Statistical analysis of life expectancy trends
- Cross-continental comparisons
- Gender gap analysis
- Correlation studies
- Data visualization and reporting

The consistent structure and guaranteed data quality enable reliable analytical workflows without additional preprocessing.

---

## 🔍 Notes

- **Data Source Date:** Data reflects statistics as scraped from the source webpage
- **Continent Coverage:** All major continents with available data
- **Data Completeness:** Only countries with complete demographic statistics are included
- **Update Frequency:** Run script periodically to refresh data if source updates

---

**Project:** Demographics Data Analysis  
**Script:** `data_cleaning.py`  
**Output Directory:** `/cleaned`  
**Output Files:** 5 continent CSV files (Africa, Americas, Asia, Europe, Oceania)