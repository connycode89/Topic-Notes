# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 09:27:15 2017

@author: cdonovan
"""

# using code from this tutorial
# https://www.dataquest.io/blog/regular-expressions-data-scientists/?imm_mid=0f9342&cmp=em-data-na-na-newsltr_20171206

import os
os.chdir('C:\MyWorkingFolder\Github Repositories\Topic-Notes\Regex')

fh = open(r"fradulent_emails.txt", "r").read()

# Who e-mails are from:
# Regular Python
for line in fh.split("\n"):
    if "From:" in line:
        print(line)
        
# Regex
import re
for line in re.findall("From:.*", fh):
    print(line)

# Isolate only the name
match = re.findall("From:.*", fh)
for line in match:
     print(re.findall("\".*\"", line))
     
# e-mail address
for line in match:
     print(re.findall("\w\S*@.*\w", line))
     
# re.search() -> matches only the first instance and returns a re match object
match = re.search("From:.*", fh)
print(type(match))
print(type(match.group()))
print(match)
print(match.group())

# re.split() -> split a string on a specified delimiter
address = re.findall("From:.*", fh)
for item in address:
    for line in re.findall("\w\S*@.*\w", item):
        username, domain_name = re.split("@", line)
        print("{}, {}".format(username, domain_name))
        
# re.sub() -> substitute parts of a string
sender = re.search("From:.*", fh)
address = sender.group()
email = re.sub("From", "Email", address)
print(address)
print(email)

# Pandas
import re
import pandas as pd
import email

emails = []

fh = open(r"fradulent_emails.txt", "r").read()
contents = re.split(r"From r", fh)
contents.pop(0)

for item in contents:
    emails_dict = {}
    # Sender address and name
    # Step 1: find line beginning with "From:"
    sender = re.search(r"From:.*", item)
    # Step 2: find email address and name
    if sender is not None:
        s_email = re.search(r"\w\S*@.*\w", sender.group())
        s_name = re.search(r":.*<", sender.group())
    else:
        s_email = None
        s_name = None
#    print("sender type: " + str(type(sender)))
#    print("sender.group() type: " + str(type(sender.group())))
#    print("sender: " + str(sender))
#    print("sender.group(): " + str(sender.group()))
#    print(s_email)
#    print(s_name)
#    print("\n")
    # Step 3A: assign email address as string to a variable
    if s_email is not None:
        sender_email = s_email.group()
    else:
        sender_email = None
    # add to dict
    emails_dict["sender_email"] = sender_email
    # Step 3B: remove unwanted substrings, assign to variable
    if s_name is not None:
        sender_name = re.sub("\s*<","",re.sub(":\s*","",s_name.group()))
    else:
        sender_name = None
    emails_dict["sender_name"] = sender_name
#    print(sender_email)
#    print(sender_name)
    # Recipient
    recipient = re.search(r"To:.*", item)
    if recipient is not None:
        r_email = re.search(r"\w\S*@.*\w", recipient.group())
        r_name = re.search(r":.*<", recipient.group())
    else:
        r_email = None
        r_name = None
    if r_email is not None:
        recipient_email = r_email.group()
    else:
        recipient_email = None
    emails_dict["recipient_email"] = recipient_email
    if r_name is not None:
        break
        recipient_name = re.sub("\s*<","",re.sub(":\s*","",r_name.group()))
    else:
        recipient_name = None
    emails_dict["recipient_name"] = recipient_name
    # Date
    date_field = re.search(r"Date:.*", item)
    if date_field is not None:
        date = re.search(r"\d+\s\w+\s\d+", date_field.group())
    else:
        date = None
#    print(date_field.group())
    if date is not None:
        date_sent = date.group()
    else:
        date_sent = None
    emails_dict["date_sent"] = date_sent        
    subject_field = re.search(r"Subject: .*", item)
    if subject_field is not None:
        subject = re.sub(r"Subject: ","",subject_field.group())
    else:
        subject = None
    emails_dict["subject"] = subject
    # Body of email
    full_email = email.message_from_string(item)
    body = full_email.get_payload()
    emails_dict["email_body"] = body
    emails.append(emails_dict)
____________________________________________________________________
# difference b/w + and * - Example
d1 = re.search(r"\d+\s\w+\s\d+",date_field.group())
d2 = re.search(r"\d*\s\w*\s\d*",date_field.group())
d11 = d1.group()
d22 = d2.group()
print(d11)
print(d22)
____________________________________________________________________

print(emails)
print(len(emails))
# Print first item in the emails list to see how it looks.
for key, value in emails[0].items():
    print(str(key) + ": " + str(emails[0][key]))

emails_df = pd.DataFrame(emails)
emails_df.head(3)
#pd.DataFrame.head(emails_df, n=3)

# find sender email addresses containing one of these 2 domain names:
em2 = emails_df[~emails_df["sender_email"].isnull()] # em2 = emails_df with null sender_emails removed
em2[em2['sender_email'].str.contains("maktoob|spinfinder")]


# Step 1: find the index where the "sender_email" column contains "@maktoob.com".
index = em2[em2["sender_email"].str.contains(r"\w\S*@maktoob.com")].index.values
# Step 2: use the index to find the value of the cell in the "sender_email" column.
# The result is returned as pandas Series object
address_Series = em2.loc[index]["sender_email"]
print(address_Series)
print(type(address_Series))
# Step 3: extract the email address, which is at index 0 in the Series object.
address_string = address_Series[0]
print(address_string)
print(type(address_string))
# Step 4: find the value of the "email_body" column where the "sender email" column is address_string.
emails3 = emails_df[emails_df["sender_email"] == address_string]["email_body"].values # shows emails from 'james_ngola2002@maktoob.com'
print(emails3)
print(len(emails3))
eee = pd.DataFrame(emails3)