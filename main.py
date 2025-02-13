from functions import BBCScraper
import csv


def main():
    # Initialize the scraper
    scraper = BBCScraper()

    # Fetch the page
    soup = scraper.fetch_page()
    if not soup:
        print("Failed to fetch the page. Exiting.")
        return

    # Extract data
    scraper.extract_titles(soup)
    scraper.extract_descriptions(soup)
    scraper.extract_photos(soup)
    scraper.extract_hours_ago(soup)

    # Get combined results
    results = scraper.get_results()

    # Save results to CSV
    if results:
        with open("articles.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["title", "description", "photo", "hours_ago"]
            )
            writer.writeheader()  # Write the header row
            writer.writerows(results)  # Write the data rows

        print(f"Saved {len(results)} articles to 'articles.csv'.")
    else:
        print("No articles found to save.")

if __name__ == "__main__":
    main()
