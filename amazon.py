# ------------ import list ------------#
import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Create the URL for inspection
URL = "https://www.amazon.co.uk/LG-OLED55C9-OLED-Alpine-Stand/dp/B07RJCSKFJ/" \
      "ref=sr_1_4?keywords=oled&qid=1582201857&sr=8-4"


# A function to convert comma's into periods (for float conversion)
def comma_converter(word):
      changer = ""
      for letter in word:
            if letter in ",":
                  changer = changer + "."
            else:
                  changer = changer + letter
      return changer


# Allows servers to identify the os, application etc. of users computer
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                         "537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}

# A function to check the price of an item on an amazon page
def check_price():
      page = requests.get(URL, headers=headers)
      # converts the html into a more readable format for python
      soup = BeautifulSoup(page.content, 'html.parser')
      soup1 = BeautifulSoup(soup.prettify(), "html.parser")
      # gets the title and the price of the item on the webpage
      title = soup1.find(id="productTitle").get_text()
      price = soup1.find(id="price_inside_buybox").get_text()
      # converts the price into a floating point object
      new_price = comma_converter(price.strip())
      converted_price = float(new_price[1:6])
      # Checks to see if the listed price is less than an amount, then sends an email
      if (converted_price < 1.200):
            send_mail()


# a function to send an email
def send_mail():
      # creates a 'simple mail transfer protocol' for to send the email
      server = smtplib.SMTP('smtp.gmail.com', 587)
      # Creates a extended hello command to be sent to another server (to receive the mail)
      server.ehlo()
      # Creates a secure connection between the sender and recipient
      server.starttls()
      server.ehlo()
      # login to the server to send the email to recipients
      server.login('robbielcampbell31@gmail.com', 'spmkvmumnkaoccox')
      # The email contents
      subject = "The price fell down!"
      body = 'Check the amazon link dude: https://www.amazon.co.uk/' \
             'LG-OLED55C9-OLED-Alpine-Stand/dp/B07RJCSKFJ/' \
             '"ref=sr_1_4?keywords=oled&qid=1582201857&sr=8-4'
      msg = f"Subject: {subject}\n\n{body}"
      # Who will recieve the email
      server.sendmail(
            "robbielcampbell@hotmail.com",
            "robbielcampbell@hotmail.co.uk",
            msg
      )
      print("email has been sent")
      server.quit()

# A function to keep checking the price at daily intervals
i = 0
while True:
      check_price()
      time.sleep(4000)
      i += 1
      x = i + 1
      if i <= x:
            # check that the app is working correctly
            times = "times"
            if i == 1:
                times = " time"
            else:
                times = " times"
            print("The timer has clocked " + str(i) + times)
