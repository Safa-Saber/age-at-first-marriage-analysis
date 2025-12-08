# Data Analysis 📊🔍

This README provides a summary of the data analysis script for the cleaned demographics dataset.

---

## Section 1: Asia-Focused Analysis 🎯

📝 The script **demographics_analysis.py** performs comprehensive statistical analysis and visualization on age at first marriage data, with primary focus on Asian countries.

The goal is to explore marriage age patterns, gender disparities, and regional variations across 48 Asian countries and compare them with global trends.

---

### ⚽ Dataset Analyzed

**Dataset Names:** 
- `Asia_data.csv`
- `Africa_data.csv`
- `Americas_data.csv`
- `Europe_data.csv`
- `Oceania_data.csv`

**Content:** Contains demographic information about age at first marriage, including average ages for men and women, age gaps, age ratios, and data collection years for 192 countries across 5 continents.

---

### 🔍 How it Analyzes the Data

The script follows a structured analytical workflow:

#### 📥 Loading Data
- Loads cleaned CSV files into pandas DataFrames
- Organizes data by continent in dictionary structure
- Re-exports data for verification

#### 👀 Initial Data Examination
- Displays first 5 rows for each continent
- Counts total countries per continent (48 in Asia)
- Verifies data structure and completeness

#### 🧹 Data Preparation
- Converts age columns to numeric types
- Handles missing values using `pd.to_numeric()` with error coercion
- Removes commas from numeric values
- Drops rows with missing critical data

#### 📈 Statistical Analysis

**For Asia:**
- Calculates mean ages for men, women, and overall average
- Computes mode (most frequent age)
- Determines median (middle value)
- Calculates standard deviation (data spread)
- Computes variance (variability measure)

**For All Continents:**
- Calculates mean marriage age by continent
- Computes average age gap between men and women
- Determines gender-specific averages across regions
- Analyzes data recency (post-2018 collection percentage)

---

### 📊 Data Visualization

The script creates multiple visualization types to explore patterns:

#### 🌏 Asia-Specific Visualizations

1. **Average Age by Country (Bar Plot)**
   - Sorted by average age in descending order
   - Color gradient showing age ranges
   - Identifies highest and lowest marriage ages

2. **Age Gap Distribution (Violin Plot)**
   - Shows distribution of age gaps across countries
   - Sorted in ascending order
   - Highlights countries with smallest/largest disparities

3. **Age Gap vs Average Age (Scatter Plot)**
   - Explores relationship between marriage age and gender gap
   - Each country represented as a point
   - Identifies clusters and outliers

4. **Men's Marriage Age by Country (Bar Plot)**
   - Displays ages for men sorted low to high
   - Blue color scheme
   - Shows regional patterns

5. **Women's Marriage Age by Country (Bar Plot)**
   - Displays ages for women sorted low to high
   - Pink color scheme
   - Highlights gender differences

6. **Data Collection Years (Scatter Plot)**
   - Shows when data was collected for each country
   - Identifies temporal data gaps
   - Assesses data recency

---

#### 🌍 Cross-Continental Visualizations

7. **Average Age by Continent (Bar Chart)**
   - Compares mean marriage age across all 5 continents
   - Sorted in ascending order
   - Pastel color palette

8. **Age Gap by Continent (Bar Chart)**
   - Shows average gender gap for each continent
   - Sorted in ascending order
   - Identifies most/least egalitarian regions

9. **Age & Gap Comparison (Line Plot)**
   - Dual-line visualization showing both metrics
   - Blue line = Average age trend
   - Red line = Age gap trend
   - Reveals relationship between development and gender equality

10. **Men vs Women by Continent (Grouped Bar Chart)**
    - Side-by-side comparison of gender-specific ages
    - Blue bars = Men
    - Pink bars = Women
    - Shows gender gap visually across continents

---

#### 🗺️ Global Analysis Visualizations

11. **Global Country Ranking (Line Plot)**
    - All 192 countries sorted by average marriage age
    - Vertical lines highlight:
      - **Red line:** Lowest Asian country
      - **Green line:** Highest Asian country
    - Shows Asia's diversity in global context

12. **Data Collection Timeline (Multi-Panel Scatter)**
    - 5 subplots (one per continent)
    - Each shows year of data collection per country
    - Unique colors per continent:
      - Asia: Blue
      - Africa: Red
      - Americas: Green
      - Europe: Gold
      - Oceania: Teal

---

### 📋 Key Analyses Performed

#### Descriptive Statistics
- Mean, median, mode calculations
- Standard deviation and variance
- Country counts and percentages
- Data quality metrics (post-2018 coverage)

#### Comparative Analysis
- Asia vs other continents
- Men vs women across regions
- Country-level global rankings
- Temporal data distribution

#### Data Quality Assessment
- Countries per continent
- Post-2018 data availability
- Percentage of recent data
- Temporal consistency evaluation

---

### 🔧 Technical Operations

**Data Cleaning:**
```python
- Remove commas from numeric values
- Convert strings to numeric types
- Handle errors with coercion to NaN
- Drop incomplete records
```

**Sorting:**
```python
- Ascending order (low to high)
- Descending order (high to low)
- Multi-level sorting by continent then value
```

**Filtering:**
```python
- By continent (e.g., Asia only)
- By year (e.g., post-2018)
- By data completeness
```

**Aggregation:**
```python
- Mean/average calculations
- Count unique values
- Sum totals
- Percentage calculations
```

---

### 📊 Output Summary

**Console Output:**
- Statistical summaries (mean, median, mode, etc.)
- Country counts per continent
- Post-2018 data percentages
- Formatted comparison tables

**Visual Output:**
- 12+ interactive plots and charts
- Bar plots, scatter plots, line plots, violin plots
- Multi-panel visualizations
- Color-coded for clarity

**No File Output:**
- All visualizations displayed interactively
- No automatic saving of plots (can be added if needed)

---

**Project:** Demographics Data Analysis  
**Script:** `demographics_analysis.py`  
**Input Directory:** `/cleaned`  
**Visualizations:** 12+ charts and plots  
**Statistical Measures:** Mean, median, mode, standard deviation, variance

---

*For detailed instructions on running the script and data coverage information, see [GUIDE.md](GUIDE.md)*