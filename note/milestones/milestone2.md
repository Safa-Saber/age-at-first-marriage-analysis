# Milestone 2: Data Collection

**Date:** December 1-2, 2024  
**Researcher:** Safa Saber

## Objective
Develop a data modeling strategy and prepare datasets.

## What I Did

### Data Source
- **Source:** Wikipedia - List of Countries by Age at First Marriage
- **Method:** Web scraping using Python (BeautifulSoup, requests)
- **Ethical Compliance:** Followed robots.txt and terms of use

### Web Scraping Script
Developed Python functions:
- `getParsedWebpage(url)` - Fetches and parses webpage with proper headers
- `clean_country_name()` - Removes unwanted characters from country names
- Extracted data by continent from HTML tables

### Data Variables Collected
- Country name
- Men's average age at first marriage
- Women's average age at first marriage
- Overall average age
- Age gap (difference between men and women)
- Age ratio
- Year of data collection

### Data Cleaning
- Removed special characters and parentheses from country names
- Converted text data to numeric types
- Handled missing values (dropped incomplete rows)
- Standardized format across all continents

### Data Organization
Created 5 continent-specific CSV files:
- `Africa_data.csv` (53 countries)
- `Americas_data.csv` (33 countries)
- `Asia_data.csv` (48 countries)
- `Europe_data.csv` (44 countries)
- `Oceania_data.csv` (14 countries)

## Deliverables Completed
✅ Data modeling strategy documented  
✅ Web scraping script (final_research_analysis_technical.ipynb)  
✅ 5 cleaned CSV datasets prepared  
✅ Data quality validated

---

**Status:** Complete  
**Next Milestone:** Data Analysis