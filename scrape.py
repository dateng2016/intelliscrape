from bs4 import BeautifulSoup
from selenium import webdriver
import time


def scrape_website(website: str) -> str:
    print("Launching Chrome Browser...")

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    try:
        driver.get(website)
        print("Page loaded...")
        time.sleep(3)
        page_source = driver.page_source
    except Exception as err:
        print(err)
    finally:
        driver.quit()

    return page_source


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
