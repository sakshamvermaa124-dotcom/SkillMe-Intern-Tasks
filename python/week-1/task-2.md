---
title: "Web Scraper with BeautifulSoup"
difficulty: "medium"
labels: ["week-1", "python", "scraping"]
---

## Task Description
Build a web scraper that extracts and saves structured data.

## Requirements
- Scrape a public site (e.g. `books.toscrape.com` or `quotes.toscrape.com`)
- Extract at least 3 fields per item (e.g. title, price, rating)
- Handle pagination (scrape at least 5 pages)
- Save results to a CSV file

## Acceptance Criteria
- [ ] Uses `requests` + `BeautifulSoup4`
- [ ] Handles HTTP errors gracefully (retry on 429/503)
- [ ] Adds a respectful delay between requests (`time.sleep(1)`)
- [ ] Output CSV has a header row and clean data
- [ ] Code is organised into functions (not one big script)

## Resources
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Books to Scrape](https://books.toscrape.com/)
