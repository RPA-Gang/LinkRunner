import pandas as pd
from pathlib import Path
from CustomClasses import URL, Soup


def retrieve_links(url: str) -> dict:
    """Converts a URL to a filepath before fetching and returning hyperlinks."""
    converted_url: Path = URL(url).convert_to_filepath()
    soup: Soup = make_soup(converted_url)
    return dict(soup.get_links())


def retrieve_table(url: str) -> pd.DataFrame:
    """Returns a pandas DataFrame using the first table located at a given URL."""
    converted_url: Path = URL(url).convert_to_filepath()
    return pd.read_html(converted_url)[0]


def make_soup(url: str | Path) -> Soup:
    """Helper function - Returns a Soup (ala BeautifulSoup) object using an open handle."""
    with open(url) as fp:
        return Soup(fp, "html5lib")
