# BBC Africa News Scraper

![BBC Africa News](images/bbcafrica.png)

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

---

### Usage, CSS Selectors Used, Learn More, and License

#### **Usage**
1. Clone the repository:
   ```bash
   git clone <repository-url>

2. Navigate to the project folder:
   ```bash
   cd bbc-news-scraper
3. Run the scraper:
   ```bash
   python main.py
4. Find the scraped data in `articles.csv`.

#### **CSS Selectors Used**
* Titles: `.hxRodh .sc-8ea7699c-3`
* Descriptions: `.bsWMfw p`
* Photos: `.kUyIkJ .efFcac`
* Timestamps: `.efYorw`

* #### **Learn More**
For a detailed explanation of the scraper and how it works, check out my Medium article:
[Building a Web Scraper to Extract BBC Africa News Data with Python and BeautifulSoup](https://medium.com/@wislyochoka/building-a-web-scraper-to-extract-bbc-africa-news-data-with-python-and-beautifulsoup-ec5db6955a34)

#### **License**
This project is licensed under the MIT License.