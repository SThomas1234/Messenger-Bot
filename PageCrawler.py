

"""

from selenium import webdriver

# Open up brower and navigate to webpage

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/dp/B07Q9MJKBV/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B07Q9MJKBV&pd_rd_w=pCLBf&pf_rd_p=8a8f3917-7900-4ce8-ad90-adf0d53c0985&pd_rd_wg=5FDhW&pf_rd_r=Q3DH83P1BWXDW3HFGQZV&pd_rd_r=a379cb1f-c9b2-45ab-bfd2-3e24c9a98adb&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTVJDUzI2SFIyNzImZW5jcnlwdGVkSWQ9QTA3NjUzMzgzRVNRTEtYTFFSQVNEJmVuY3J5cHRlZEFkSWQ9QTA5MDc1MDMzSldHUDBaTFIwUjQyJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")

# Extract data

title = driver.find_element_by_xpath("//div[@)

"""