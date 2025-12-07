# Age at First Marriage Analysis in Asia
## Statistical Patterns & Global Comparison

Welcome to **Age at First Marriage in Asia**, a comprehensive data science project that explores marriage age patterns across 48 Asian countries. Our mission is to build reproducible, insight-rich analysis that illuminates how cultural, economic, and social factors influence one of life's most significant decisions—getting married.

---

## 📋 Project Milestones

### ✅ Milestone 0: The Kick-Off – Defining the Mission
**Where it all began...**

Our journey started with a straightforward but meaningful question: *How do marriage patterns vary across Asia, and what factors explain these differences?*

We established clear objectives and designed research that would be both comprehensive and actionable.

**Check out**: [Domain Study Folder](./0_domain_study) for initial research

---

### ✅ Milestone 1: Scouting for Gold – Problem Identification
**Understanding the landscape...**

Through exploratory research, we identified key questions and gaps in understanding:
- How do marriage ages differ between men and women across Asian countries?
- What's Asia's position compared to other continents?
- How does data collection timing affect our conclusions?

**Problem Statement**

Despite globalization and economic development, marriage age patterns across Asia remain poorly understood. Different regions show vastly different trends—some countries still marry very young (21 years) while others delay marriage significantly (38 years). Understanding these patterns is crucial for policymakers, educators, and development organizations working on gender equality, education, and family planning.

**Core Research Question**

> **What are the statistical patterns of age at first marriage across Asian countries, how do these patterns differ by gender, and how does Asia compare to other continents?**

---

### ✅ Milestone 2: Filling the Trophy Cabinet – Data Collection & Preparation

This milestone was divided into **3 stages**: Data Collection, Data Preparation, and Data Exploration.

#### Stage 1: Data Collection

We gathered comprehensive marriage age data from a reliable, globally-recognized source:

- **Source**: Wikipedia's "List of countries by age at first marriage"
- **Coverage**: 48 Asian countries + comparative data from Africa, Americas, Europe, and Oceania
- **Variables**: Men's age at first marriage, Women's age at first marriage, Average age, Age gap, Age ratio, Data collection year
- **Timeframe**: Data spanning 1991–2023 (mostly recent: 56% from 2018 onwards)

**All datasets available here**: [Datasets Folder](./1_datasets)

#### Stage 2: Data Preparation

Raw data never comes clean. Here's what we did:

- Removed formatting artifacts (brackets, parentheses) from country names
- Converted text values to numeric types (removed commas, handled conversion errors)
- Dropped incomplete rows with missing critical values
- Standardized formatting across all continents
- Created clean, validated CSV files for each continent

The data preparation script and documentation are available here:  
[Data Preparation Folder](./2_data_preparation)

#### Stage 3: Data Exploration

Before diving into analysis, we explored the cleaned data to understand its structure:

- Distribution of marriage ages across countries
- Gender gaps and regional variations
- Data quality assessment and outlier identification
- Initial pattern recognition

Exploration notebooks and findings:  
[Data Exploration Folder](./3_data_exploration)

---

### ✅ Milestone 3: Breaking Down the Opposition – Statistical Analysis
**The core analysis...**

Using rigorous statistical methods, we analyzed 48 Asian countries to answer our research question.

#### What We Measured

We calculated key descriptive statistics:
- **Mean** (average age at marriage)
- **Median** (middle value, robust to outliers)
- **Mode** (most frequently occurring age)
- **Standard Deviation** (variability in marriage ages)
- **Variance** (spread of the data)

#### Key Findings: Asia at a Glance

| Metric | Men | Women | Overall |
|--------|-----|-------|---------|
| **Mean Age** | 28.69 years | 25.68 years | 27.20 years |
| **Median Age** | 28.6 years | 25.45 years | — |
| **Mode** | 27.2 years | 21.0 years | — |
| **Standard Deviation** | 3.20 | 3.42 | — |
| **Variance** | 10.23 | 11.71 | — |

**Translation:**
- Men in Asia marry approximately **3 years later** than women
- Women's marriage ages show **greater variability**, suggesting diverse cultural and socioeconomic influences
- Age consistency within countries but significant regional variation

#### Asia's Global Position

| Metric | Asia | Global Rank | Context |
|--------|------|-------------|---------|
| **Mean Age** | 27.20 yrs | 3rd | Higher than Africa (25.34) & Oceania (26.34) |
| | | | Lower than Europe (31.81) & Americas (28.86) |
| **Age Gap** | 3.01 yrs | Moderate | Larger than Europe (2.36), smaller than Africa (5.01) |
| **Men's Age** | 28.69 yrs | 3rd | Similar rank distribution |
| **Women's Age** | 25.68 yrs | 3rd | Similar rank distribution |

**Key Insight**: Asians marry younger than Europeans and Americans, but older than Africans—positioned in the global middle ground.

---

### ✅ Milestone 4: Celebrating the Win – Key Insights
**What the data tells us...**

#### The Three Big Stories

**Story 1: The East-West Divide**

- **East Asia** (South Korea, Taiwan, Hong Kong, Japan): Delayed marriages (32–38 years)
  - Drivers: High education emphasis, urbanization, career focus, changing social norms
  
- **South/Southeast Asia** (Nepal, Laos, Cambodia): Early marriages (21–24 years)
  - Drivers: Economic constraints, cultural traditions, limited education access

**Implication**: Modern, developed Asian economies show convergence toward later marriages; traditional societies maintain earlier patterns.

---

**Story 2: The Gender Gap Story**

- Most Asian countries display a consistent **3-year gender gap**
- **Outliers**:
  - **Smallest**: Singapore (<1 year) – Suggests high gender equality in marriage timing
  - **Largest**: Syria (>5 years) – Indicates more traditional marriage structures

**Implication**: A country's gender gap at marriage may reflect broader gender equality and women's empowerment.

---

**Story 3: The Data Recency Challenge**

- ✅ **56.25%** of Asian countries have recent data (2018 onwards)
- ⚠️ **43.75%** have older data (may not reflect current trends)
- Data ranges: 1991 (Brunei) to 2023 (Japan, Singapore, Vietnam)

**Implication**: Recent data is generally reliable; older data may be outdated due to rapid social change.

---

**Detailed Analysis Reports**:
- Technical Report: For data scientists (Coming soon - `4_data_analysis/technical_report.md`)
- Non-Technical Summary: For general audiences (Coming soon - `4_data_analysis/non_technical_summary.md`)

For full analysis with visualizations:  
[Data Analysis Folder](./4_data_analysis)

---

## Repository Map

```
README.md                          # You're reading it now!
├── 0_domain_study/                # Research & problem framing
├── 1_datasets/                    # Raw and cleaned data
│   ├── raw/
│   │   └── wikipedia_source.md
│   └── cleaned/
│       ├── Asia_data.csv
│       ├── Africa_data.csv
│       ├── Americas_data.csv
│       ├── Europe_data.csv
│       └── Oceania_data.csv
├── 2_data_preparation/            # Cleaning & standardization scripts
├── 3_data_exploration/            # Initial analysis & pattern discovery
├── 4_data_analysis/               # Statistical analysis & key findings
├── 5_visualizations/              # Charts & plots
│   ├── average_age_by_country.png
│   ├── age_gap_distribution.png
│   ├── continental_comparison.png
│   ├── gender_comparison.png
│   └── data_collection_timeline.png
├── 6_reports/                     # Final deliverables
│   ├── technical_report.md
│   ├── non_technical_summary.md
│   └── limitations_analysis.md
├── notebooks/                     # Jupyter notebooks
│   ├── analysis.ipynb
│   └── data_exploration.ipynb
├── requirements.txt               # Python dependencies
├── LICENSE                        # MIT License
└── CHANGELOG.md                   # Version history
```

---

## The Extremes: Asia's Marriage Age Range

### Highest Average Marriage Age
**South Korea: 38 years** (39 for men, 37 for women)
- Drivers: Highly developed economy, education emphasis, delayed childbearing, career prioritization
- Trend: One of the world's oldest marriage ages

### Lowest Average Marriage Age
**Nepal & Laos: 21.9 years**
- Drivers: Economic constraints, cultural traditions, lower education access
- Context: Among the youngest globally

### The Spread
The **16.1-year difference** between highest and lowest showcases Asia's incredible diversity in marriage practices.

---

## Gender Disparities: The Numbers

| Finding | What It Means |
|---------|---------------|
| Women show **higher variability** (std: 3.42 vs men's 3.20) | Cultural factors affect women's marriage timing more |
| **~3 year gender gap** across most countries | Reflects traditional marriage structures (men older) |
| **Smallest gap**: Singapore (<1 year) | Gender equality in marriage timing |
| **Largest gap**: Syria (>5 years) | More traditional marriage structures |

---

## Asia in Global Context

**We're in the middle of the pack:**

1. **Europe**: 31.81 years (oldest marriages)
2. **Americas**: 28.86 years
3. **Asia**: 27.20 years ← **You are here**
4. **Oceania**: 26.34 years
5. **Africa**: 25.34 years (youngest marriages)

**What this suggests**: Asia is experiencing a **transition**—some countries rapidly modernizing (East Asia), while others maintain traditional patterns (South/Southeast Asia).

---

## Limitations & Honest Assessment

We believe in transparency. Here's what you should know:

| Limitation | Impact | Mitigation |
|-----------|--------|-----------|
| **Data collection years vary** (1991–2023) | Older data may not reflect current trends | 56% recent data; use caution with older entries |
| **Missing data** for some countries | Reduced sample in certain regions | Analysis valid for 48 countries; generalize carefully |
| **Different survey methodologies** | Data may not be perfectly comparable | Results show correlations, not causation |
| **External factors** not measured | Can't isolate single causes | Qualitative research needed to supplement |

---

## Technologies & Tools

```
Python 3.7+
├── pandas            # Data manipulation & analysis
├── numpy             # Numerical computing
├── matplotlib        # Static visualizations
├── seaborn           # Statistical graphics
├── beautifulsoup4    # Web scraping
└── requests          # HTTP requests
```

**Technology Stack**:
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Quick Start

### Prerequisites
```bash
Python 3.7 or higher
pip (Python package manager)
```

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/age-at-first-marriage-analysis.git
cd age-at-first-marriage-analysis

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Analysis

```bash
# Option 1: Run full pipeline
python 2_data_preparation/data_cleaning.py
python 4_data_analysis/statistical_analysis.py

# Option 2: Explore interactively
jupyter notebook notebooks/analysis.ipynb
```

### View Results

All visualizations are saved in `5_visualizations/` as PNG files:
- `average_age_by_country.png` – Marriage ages across Asia
- `continental_comparison.png` – How Asia compares globally
- `gender_comparison.png` – Men vs. women patterns
- `scatter_plot_correlation.png` – Age gap relationships

---

## Our Approach

### Data Collection
1. Identified Wikipedia as reliable, global source
2. Web scraped using ethical practices (BeautifulSoup)
3. Organized data by continent for comparison

### Analysis Framework
1. **Descriptive Statistics**: Mean, median, mode, standard deviation, variance
2. **Gender Comparison**: Separate analysis for men and women
3. **Continental Benchmarking**: Asia compared to four other continents
4. **Temporal Assessment**: Examined how data collection year affects trends

### Validation
- ✅ Verified data completeness (excluded incomplete rows)
- ✅ Checked type consistency (all numeric fields validated)
- ✅ Identified and documented outliers
- ✅ Cross-referenced with domain knowledge

---

## Documentation

For different audiences:

1. **Technical Report** (`4_data_analysis/technical_report.md`)
   - For: Data scientists, researchers, analysts
   - Contains: Detailed methodology, statistical formulas, code snippets

2. **Non-Technical Summary** (`4_data_analysis/non_technical_summary.md`)
   - For: General readers, journalists, policymakers
   - Contains: Key findings, plain-language explanations, actionable insights

3. **Limitations Analysis** (`6_reports/limitations_analysis.md`)
   - For: Critical readers, future researchers
   - Contains: Known constraints, future research directions

---

## How to Use This Research

**For Researchers**: 
- Foundation for deeper causal analysis
- Datasets available for further study
- Identify regions needing investigation

**For Policymakers**: 
- Understand regional marriage trends
- Inform education & social policies
- Target interventions (e.g., child marriage prevention)

**For Journalists**: 
- Reference data for articles on changing norms
- Cite statistics about gender gaps
- Contextualize cultural trends

**For Students**: 
- Learn data analysis best practices
- See reproducible research workflow
- Use as template for own projects

---

## License

This project is open-sourced under the **MIT License**. See [LICENSE](./LICENSE) for details.

All data sourced from Wikipedia remains under their terms of use.

---

## Acknowledgments

- **Data Source**: [Wikipedia - List of countries by age at first marriage](https://en.wikipedia.org/wiki/List_of_countries_by_age_at_first_marriage)
- **Guidance**: University of London, Emerging Talent Program
- **Tools**: Python community, pandas, matplotlib, seaborn
- **Support**: Everyone who encouraged this research

---

## Questions & Feedback

- **Questions?** Open an Issue on GitHub
- **Contact**: [Your Email/LinkedIn]
- **Contributing?** Pull requests welcome!

---

## About the Author

**Safa Saber**  
**Program**: Emerging Talent Program (MIT)  
**Project**: Capstone - Age at First Marriage Analysis  
**Completed**: December 2025  
**Focus**: Data Science, Statistical Analysis, Data Visualization, Research Methodology

**GitHub**: [@Safa-Saber](https://github.com/Safa-Saber)  
**LinkedIn**: [Safa Saber](https://www.linkedin.com/in/safasaber/)

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| 1.0 | Dec 2025 | Initial release – Complete analysis of Asian marriage age patterns |

---

## Ready to Explore?

**Start here**: 
- Interactive analysis: `notebooks/analysis.ipynb`
- Quick overview: `4_data_analysis/non_technical_summary.md`
- Visual findings: `5_visualizations/`

---

Last Updated: December 2025  
Status: Complete ✅  
Open for feedback, citations, and collaboration