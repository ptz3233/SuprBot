# SuprBot

Created to combat the fast sellout times from clothing retailer supremenewyork.com
Working with Supreme's website format as of F/W 2016

Uses:
* Requests to download html
* BeautifulSoup to find obfuscated product link
* Selenium for navigating website and entering forms
* Chromedriver for the broswer

Warning:
If you do not know what you are doing or do not understand this code, do not use it. You can easily accidentally buy things that you do not want, or possibly be baned from Supreme.

# Usage:

All user enterable fields are declared at the top of sup.py. Item name, size, and style must be entered *exactly* as they appear on the product page. They are case sensitive. Must enter mainUrl as the category page (sweatshirts, jackets, skate) not shop all or new. 

The line that actually clicks the process payment button is commented out. Uncomment only if you are ready to buy and understand what you are doing.

This program does not know when its 11am. If you try to run it minutes before it will constanly refresh and probably get you banned. I recomend typing go and pressing enter only at exactly 11am.

Thanks to whitij00 on github for a starting point for this.
