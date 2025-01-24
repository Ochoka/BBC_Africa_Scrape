# BBC Africa News Scraper

A Python web scraper for extracting news articles from the **BBC Africa News** section. The scraper collects **titles**, **descriptions**, **photos**, and **timestamps**, and saves them in a structured CSV file for further analysis.

## Features
- Fetches the latest news articles from the BBC Africa News page.
- Extracts:
  - Article titles
  - Descriptions
  - Image URLs
  - Timestamps (e.g., "2 hours ago")
- Saves the extracted data into a CSV file (`articles.csv`).
- Modularized design for clarity and reusability:
  - `functions.py`: Contains the scraper logic.
  - `main.py`: Entry point to execute the scraper.

## Prerequisites
- Python 3.x
- Installed libraries:
  - `requests`
  - `beautifulsoup4`

Install dependencies:
```bash
pip install requests beautifulsoup4
