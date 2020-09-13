import schedule
import time

def start_up():
   execfile('itemshop.py')
   print("Starting up itemshop.py!")


schedule.every().day.at("06:00").do(start_up)

while 1:
  schedule.run_pending()
  time.sleep(1)


