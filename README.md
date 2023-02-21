# <img src='Wikipedia-logo-v2.svg.png' height='50'></a> Wikipedia Scraper
This project scrapes all featured wikipedia articles from 2005-2009, saves their published date, title, and character count into a csv, then generates a histogram to visualize the distribution of length of the featured articles.

## How It's Made:

**Tech used:** Python, BeautifulSoup, Pandas, Matplotlib

Used Python's BeautifulSoup library to extract links, titles, and published date for every featured article on wikipedia in the given time frame (easily alterable using the range function in Python). Then used BeautifulSoup to parse the HTML of each article's page and extract only inner text, I used Python's built in len function to obtain the character count for each article.

After this, I used Python's csv library to write the each article its accompanying information as a row in a csv file.

In a separate python file I used Pandas to remove any outliers in terms of the articles' character counts. After cleaning the dataset I used Matplotlib to create a simple visualization of the distribution of character counts in the form of a histogram.
