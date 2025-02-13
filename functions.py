import requests
from bs4 import BeautifulSoup


class BBCScraper:
    def __init__(self):
        self.base_url = "https://www.bbc.com/news/world/africa"
        self.titles = []
        self.descriptions = []
        self.photos = []
        self.hours_ago = []

    def fetch_page(self):
        """Fetch the HTML content of the base URL."""
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, "html.parser")
        else:
            print(f"Failed to fetch {self.base_url}. Status code: {response.status_code}")
            return None

    def extract_titles(self, soup):
        """Extract titles from the given BeautifulSoup object."""
        title_elements = soup.select(".hxRodh .sc-8ea7699c-3")  # CSS selector for titles
        self.titles = [title.text.strip() for title in title_elements]

    def extract_descriptions(self, soup):
        """Extract descriptions from the given BeautifulSoup object."""
        description_elements = soup.select(".bsWMfw p")  # CSS selector for descriptions
        self.descriptions = [
            desc.text.strip() for desc in description_elements
        ]

    def extract_photos(self, soup):
        """Extract photo URLs from the given BeautifulSoup object."""
        photo_elements = soup.select(".kUyIkJ .efFcac")  # CSS selector for photos
        self.photos = [
            photo.get("src") if photo else "No image available" for photo in photo_elements
        ]

    def extract_hours_ago(self, soup):
        """Extract 'hours ago' information from the given BeautifulSoup object."""
        time_elements = soup.select(".kUyIkJ .efFcac")  # CSS selector for hours ago
        self.hours_ago = [
            time.text.strip() for time in time_elements
        ]

    def get_results(self):
        """Combine extracted data into a single list of dictionaries."""
        return [
            {
                "title": self.titles[i] if i < len(self.titles) else "No title",
                "description": self.descriptions[i] if i < len(self.descriptions) else "No description",
                "photo": self.photos[i] if i < len(self.photos) else "No photo",
                "hours_ago": self.hours_ago[i] if i < len(self.hours_ago) else "No time",
            }
            for i in range(max(len(self.titles), len(self.descriptions), len(self.photos), len(self.hours_ago)))
        ]
