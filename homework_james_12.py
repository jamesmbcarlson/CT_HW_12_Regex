# James Carlson 
# Coding Temple - SE FT-144
# Backend Module 3 Lesson 4 Assignment: Regex

import re

print("\n====== 1. Python Regular Expressions Mastery ======\n")

# code correction:
# code correction 1 - removed HTML tags!
text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
# added a-z to sets so lowercase is also covered
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
print(emails)



print("\n====== 2. Python Regular Expressions Deep Dive ======\n")

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, user4@exclude.net"
# added regex group to exclude strings with "exclude.com" from return
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)



print("\n====== 3. Advanced Text Processing with Python Regex ======\n")
print("    === 3.1 Advanced Data Extraction===\n")

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# find "Occupation" in string and extract following word:
occupation = re.search(r"Occupation:\s(\w+)", text).group(1)
print(occupation)



print("\n    === 3.2 URL Validator ===\n")

urls = ["https://example.com", "www.example.com", "http://test.com"]
# Validate each URL in the list.  A valid URL should start with 'http://' or 'https://', followed by a domain name.
for url in urls:
    match = re.match(r"(^https://|http://)+[A-Za-z0-9.-]+\.[A-z]{2,}", url)
    if match:
        print(url, "  <-- This is a valid URL!")
    else:
        print(url, "  <-- This is NOT a valid URL.")



### ??? ###
# now our assignment is gonna be, if tom was born 50 years before year 2035 and he went back to the 
# future 3 years and came back 5 years younger create a format for his age in a flipped format
#
# Tom was born in 1985 (the same year that Back to the Future was released and took place)!
# If he went "back to the future" for 3 years, he would have theoretically aged to 53.
# Positing that he came back 5 years younger probably means he experienced sort of time distortion
# as he traveled through time, but for our purposes he's now 45.
# I don't really know what creating "a format for his age in a flipped format" means, so I'll just 
# switch the digits around and call it a clean 54. Q.E.D.