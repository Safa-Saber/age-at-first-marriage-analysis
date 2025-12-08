"""
Web Scraping: Age at First Marriage Data
=========================================
This script scrapes marriage age data from Wikipedia and saves raw CSV files.

Source: https://en.wikipedia.org/wiki/List_of_countries_by_age_at_first_marriage

Process:
1. Fetch Wikipedia page
2. Extract continent tables
3. Parse table rows
4. Save raw CSV files by continent
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# ============================================================================
# STEP 1: Fetch and Parse Wikipedia Page
# ============================================================================

def getParsedWebpage(url):
    """
    Fetch and parse a webpage while handling access errors.
    
    Parameters:
        url (str): The URL of the webpage to fetch
        
    Returns:
        BeautifulSoup object or str: Parsed webpage content or 'error'
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/93.0",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "DNT": "1"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to fetch webpage. Status code: {response.status_code}")
            return 'error'
        else:
            print("✅ Webpage fetched successfully!")
            return BeautifulSoup(response.content, 'html.parser')
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error occurred: {e}")
        return 'error'


# ============================================================================
# STEP 2: Extract Continent Names and Tables
# ============================================================================

def extract_continents_and_tables(soup):
    """
    Extract continent headings and tables from parsed webpage.
    
    Returns:
        tuple: (continent_headings, tables)
    """
    continents = ['Africa', 'Asia', 'Europe', 'Americas', 'Oceania']
    continent_headings = soup.find_all('h2')
    
    # Filter only continent headings
    filtered_headings = [h for h in continent_headings 
                        if any(cont in h.get_text() for cont in continents)]
    
    # Find all data tables
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    print(f"\n✅ Found {len(filtered_headings)} continents")
    print(f"✅ Found {len(tables)} tables\n")
    
    return filtered_headings, tables


# ============================================================================
# STEP 3: Extract Data from Tables
# ============================================================================

def extract_continent_data(soup):
    """
    Associate continent headings with tables and extract country data.
    
    Returns:
        dict: Raw data organized by continent
    """
    continent_name = None
    continent_data = {}
    
    # Loop through all headings and tables
    for element in soup.find_all(['h2', 'table']):
        if element.name == 'h2':
            # Extract continent name from id attribute
            continent_name = element.get('id')
            
        elif element.name == 'table' and continent_name:
            rows = element.find_all('tr')
            table_data = []
            
            # Skip header row
            for row in rows[1:]:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                
                # Ensure we have enough columns
                if len(cols) >= 7:
                    country_data = {
                        'Country': cols[0],
                        'Men': cols[1],
                        'Women': cols[2],
                        'Average': cols[3],
                        'Age Gap': cols[4],
                        'Age Ratio': cols[5],
                        'Year': cols[6]
                    }
                    table_data.append(country_data)
            
            # Store data under continent name
            continent_data[continent_name] = table_data
    
    return continent_data


# ============================================================================
# STEP 4: Save Raw Data to CSV
# ============================================================================

def save_raw_to_csv(continent_data, output_path='1_datasets/raw/'):
    """
    Save raw data to CSV files by continent.
    
    Parameters:
        continent_data (dict): Dictionary with continent data
        output_path (str): Path to save CSV files
    """
    # Remove empty continents
    continent_data = {cont: data for cont, data in continent_data.items() if data}
    
    for continent, data in continent_data.items():
        df = pd.DataFrame(data)
        filename = f"{output_path}raw_{continent}.csv"
        df.to_csv(filename, index=False)
        print(f"✅ Saved {continent}: {filename} ({len(df)} countries)")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("AGE AT FIRST MARRIAGE: WEB SCRAPING")
    print("=" * 70)
    
    # Step 1: Fetch webpage
    print("\n[1/4] Fetching Wikipedia page...")
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_age_at_first_marriage'
    soup = getParsedWebpage(url)
    
    if soup == 'error':
        print("❌ Failed to fetch webpage. Exiting.")
        exit()
    
    # Step 2: Extract continents and tables
    print("[2/4] Extracting continents and tables...")
    headings, tables = extract_continents_and_tables(soup)
    
    # Step 3: Extract data
    print("[3/4] Extracting data from tables...")
    continent_data = extract_continent_data(soup)
    print(f"✅ Extracted data for {len(continent_data)} continents\n")
    
    # Step 4: Save raw data
    print("[4/4] Saving raw data to CSV...")
    save_raw_to_csv(continent_data)
    
    # Summary
    print("\n" + "=" * 70)
    print("✅ WEB SCRAPING COMPLETE")
    print("=" * 70)
    print(f"Raw CSV files saved to: 1_datasets/raw/")
    print("=" * 70)