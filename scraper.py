import requests
from bs4 import BeautifulSoup

# 抓取台積電股價
def scrape_tsmc_stock_price():
    url = "https://www.google.com/finance/quote/2330:TPE"  # 台積電股價GOOGLE網站URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    stock_price = soup.find("div", class_="YMlKec fxKbKc").text  # 使用 BeautifulSoup 解析網頁並提取股價信息
    return stock_price

if __name__ == "__main__":
    stock_price = scrape_tsmc_stock_price()
    message = f"台積電股價：{stock_price}"
    requests.post("https://ntfy.sh/VAYjC6gEAjujK5xA",
    data=message.encode(encoding='utf-8'))