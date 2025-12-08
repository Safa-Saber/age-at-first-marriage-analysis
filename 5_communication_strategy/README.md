# Communication Strategy & Artifacts

## Overview
This folder contains the communication strategy and artifacts designed to present research findings on age at first marriage in Asia to diverse audiences.

---

## Files in This Folder

### 📊 `marriage_infographic.html`
**Purpose:** Visual one-page infographic summarizing key research findings

**Content:**
- Research question and approach
- Key statistics (27.2 years average, 3.01 year gap, 192 countries)
- Three data visualizations (global comparison, gender analysis, data timeline)
- Continental rankings
- Key findings and main insights
- Research methodology
- Researcher credit

**Target Audience:** Policymakers, educators, researchers, general public

**Usage:** 
- Open in any web browser (Chrome, Firefox, Safari, Edge)
- Can be printed directly to PDF (Ctrl+P / Cmd+P → Save as PDF)
- Shareable via email or file upload
- No internet connection required

---

### 📈 `image1.png` - Global Country Comparison
**Chart:** Average Age at Marriage by Country (Ascending Order)

**Shows:** 192 countries sorted by marriage age, highlighting Asia's range from Nepal/Laos (21.9 years) to South Korea (38 years)

---

### 📈 `image2.png` - Gender Comparison by Continent  
**Chart:** Comparison of Average Age for Men and Women by Continent

**Shows:** Gender differences across all continents, with Asia showing men at 28.69 years and women at 25.68 years

---

### 📈 `image3.png` - Data Collection Timeline
**Chart:** Year of Data Collection for Countries in Asia

**Shows:** When data was collected for each Asian country (1991-2023), revealing 56.25% have post-2018 data

---

### 📓 `final_research_analysis_technical.ipynb`
**Purpose:** Complete Jupyter notebook containing all data collection, cleaning, analysis, and visualization code

**Components:**
- Web scraping from Wikipedia using BeautifulSoup
- Data cleaning and preparation with pandas
- Statistical calculations (mean, median, mode, standard deviation, variance)
- Continental and gender comparisons
- Data visualization using matplotlib and seaborn (generates all charts)
- CSV export for each continent

**Key Sections:**
- `getParsedWebpage()` - Fetches and parses webpage content
- `clean_country_name()` - Standardizes country names
- Data processing for Asia and all continents
- Comprehensive statistical analysis
- Code outputs include all three visualization charts (Image1, Image2, Image3)

---

### 📄 `nontechnical_summary.md`
**Purpose:** Accessible summary of research findings for non-technical audiences

**Content:**
- Plain-language explanation of the research question
- Key findings presented without statistical jargon
- Context about why marriage age matters
- Real-world implications of the patterns discovered
- Data considerations explained simply

**Target Audience:** General public, policymakers, educators, anyone without technical background

---

### 📑 `Age at First Marriage_ Asia in Global Context.pdf`
**Purpose:** PDF version of the visual infographic for easy printing and sharing

**Content:**
- Same content as the HTML infographic
- Formatted for print and digital distribution
- Professional layout for reports and presentations
- Portable format compatible with all devices

**Usage:**
- Print for physical presentations
- Attach to emails or reports
- Share via any platform (no browser needed)
- Archive-friendly format

---

## Communication Strategy

### Target Audiences
1. **Policymakers** - Need quick insights for education and gender equality policies
2. **Researchers** - Want data-driven findings with clear methodology
3. **Educators** - Seek accessible explanations of marriage age patterns
4. **General Public** - Interested in understanding global social trends

### Distribution Methods
- **Digital sharing:** Email attachment, learning management systems, cloud storage
- **Print format:** PDF version for presentations and reports
- **Web viewing:** HTML file opens in any browser without installation
- **Data access:** Python script available for replication and verification

### Communication Goals
- Present complex statistical findings in an accessible visual format
- Highlight Asia's diversity in marriage age patterns
- Provide clear comparisons with global trends
- Demonstrate research methodology transparently
- Enable easy sharing and presentation of findings

---

## How to Use These Artifacts

### For Presentations
1. Open `marriage_infographic.html` in browser
2. Present directly or print to PDF
3. Reference specific charts (images 1-3) as needed

### For Reports
1. Export infographic as PDF
2. Embed individual charts in documents
3. Reference Python script for methodology details

### For Replication
1. Run `Data_Collection_and_Analysis.py` to reproduce analysis
2. Script generates all statistics and visualizations
3. Outputs CSV files for each continent

---

## Technical Requirements

### Infographic
- Any modern web browser
- Image files must be in same folder as HTML
- No internet connection needed

### Python Script
- Python 3.x
- Required libraries: requests, BeautifulSoup, pandas, matplotlib, seaborn, numpy
- Internet connection for web scraping

---

## Key Messages

1. **Asia is diverse:** 16.1 year range between youngest (Nepal/Laos) and oldest (South Korea) marriage ages
2. **Middle-ground globally:** Asia ranks 3rd, between developed regions (Europe, Americas) and developing regions (Africa, Oceania)
3. **Gender gaps persist:** 3.01 year average gap in Asia, moderate compared to global patterns
4. **Data quality matters:** 56.25% of Asian data is recent (post-2018), but variations exist

---

## Credits
**Researcher:** Safa Saber  
**Program:** MIT Emerging Talent Program  
**Project Type:** Data Science Research Project  
**Date:** December 2025

