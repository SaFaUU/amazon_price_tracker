from bs4 import BeautifulSoup
from lxml import etree
import requests
import smtplib

# Add Your product URL Below
WEBSITE_URL = "https://www.amazon.com/PNY-GeForce-Gaming-Epic-X-Graphics/dp/B08X12YK8G/ref=sr_1_1_sspa?crid=1VNZYRP2F72IF&keywords=rtx%2B3060&qid=1653423373&sprefix=rtx%2B30%2Caps%2C330&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFTQjdZU0lMREIxRTAmZW5jcnlwdGVkSWQ9QTA5NzQyNTIxUTRSNkVCSTM1UkpPJmVuY3J5cHRlZEFkSWQ9QTEwMzAwNjMzTDJGSk1HTUY0NVM3JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
amazon_webpage = requests.get(WEBSITE_URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Request Line": "GET / HTTP/1.1"}).text
soup = BeautifulSoup(amazon_webpage, "lxml")
prices = soup.find_all(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay")
for price in prices:
    current_price = price.getText().split("$")
    print(current_price[1])

with smtplib.SMTP("smtp.gmail.com") as connections:
    connections.starttls()
    connections.login(user="...",password="...") ##insert your own email and password
    
    # Add the email you want to send email notificiation to and change the message if you want to
    connections.sendmail(from_addr="...", to_addrs="...", msg=f"Subject: Current Price of 3060\n\n Here is the link: {WEBSITE_URL}\n\nThe current price is: {current_price[1]}")