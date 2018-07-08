import urllib
import urllib2
import re
import math
import sys
from time import ctime
import smtplib
#enter the url and target discount
my_flipkart_url = "Buy Transcend StoreJet 25M3 2.5 inch 1 TB External Hard Disk Online at Best Prices In India | Flipkart.com"
my_target_discount = float(10)
def send_email (message, status):
 fromaddr = '<sender>'
 toaddrs = 'recievers'
 server = smtplib.SMTP('Page on Gmail', 587)
 server.ehlo()
 server.starttls()
 server.ehlo()
 server.login('<username>', '<password>')
 server.sendmail(fromaddr, toaddrs, 'Subject: %s\r\n%s' % (status, message))
 server.quit()
def Connect_to_Flipkart():
 aResp = urllib2.urlopen(my_flipkart_url); #read the source
 web_pg = aResp.read();
 #parse the required fields from the source
 selling_price_pattern = "'price' : \""+"(.*?)"+"\""
 MRP_pattern = "'amount' : \""+"(.*?)"+"\""
 Item_name = "'fn' : \""+"(.*?)"+"\""
 SP = re.search(selling_price_pattern, web_pg)
 CP = re.search(MRP_pattern, web_pg)
 Item = re.search(Item_name, web_pg)
 selling_price = SP.group(1)
 MRP = CP.group(1)
 selling_price = int(selling_price.replace(',',''))
 MRP = int(MRP.replace(',',''))
 discount_rs = MRP-selling_price
 discount_per = float(discount_rs*100/ MRP)
 File_name = "E:\\myscripts\\Report\\"+Item.group(1)+"_report.txt" #save report to the required folder
 if SP and CP and Item:
  current_time = ctime()
  final_line = "\n"+repr(current_time).rjust(2) + repr(MRP).rjust(3) +" "+repr(selling_price).rjust(4) + repr(discount_rs).rjust(5) + repr(discount_per).rjust(6)+"%"+repr(my_target_discount).rjust(7)
  with open(File_name, "a") as myfile:
   myfile.write(final_line)
  if my_target_discount <= discount_per:
   message = "Your product is ready to buy!\n"+"\nProduct name: "+str(Item.group(1))+"\nPrice: Rs."+str(selling_price)+"\nMRP: Rs."+str(MRP)+"\nTarget Discount:"+str(my_target_discount)+"%"+"\nCurrent Discount:"+str(discount_per)+"%"
   message = message + "\n\n-Rohit"
   send_email(message,'Hurry up!!') #send mail to subscriber
 else:
  final_line = "Error in parsing!!"
  with open(File_name, "a") as myfile:
   myfile.write(final_line)
def main():
  Connect_to_Flipkart() #connect to flipkart
if __name__ == '__main__':
    main()



















'''Wrote a script to monitor the price of an item on flipkart and send_email
notification if the item is available at required discount. Basically, parsed the source of the page. The input to the script 
is the url of the required product and the target discount. So when the current discount is ge to target discount email notification
 will be sent. With one of the VM which runs 24*7, I set the task scheduler to run the script once in 2hours. Also, the code redirects
  the output of each and every run to the text file so that we can always keep track of the price of the product over a period of 
  time. Code can be optimized with exception handling but with the current version my purpose was solved ;)

Here is how the screenshot of the notification looks:-'''