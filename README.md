# SMS Spam
SMS spam is a small script that allows the user to spam a 
specific number with a specific message for a specific amount of
texts sent. Great for educational use or harmless pranks on
friends and family.

##### **Warning: use this program at your own risk!**
**I really shouldn't have to tell you not to use this script 
maliciously. Use this script with integrity and morality 
and think to yourself  'will this get me in trouble?' 
and 'would I be sincerely upset if someone ran this 
script on me?'. If the answer to either of these questions 
are yes, do not use this script.**

## Requirements
- A gmail account
- A phone number (and known carrier)
- Python must be installed
- A sense of morality

## How to use SMS Spam
1) First make a gmail account.
2) Make sure your gmail allows for "less secure apps
to have access to your account".
[Here](https://hotter.io/docs/email-accounts/secure-app-gmail/)
 is a tutorial on how to do this.
3) Change the variables in vars.json to correspond to the
appropriate variables. Note, the file will not run properly
if the "repeat" variable is greater than 150 as to prevent 
over-spam.
4) Run the script.

Note: here are the supported carriers that can be changed
within the .json file.

Also note: This program prevents from sending over 500 messages, so set the variable to under 500.
```buildoutcfg
    att
    tmobile
    verizon
    sprint
    boost mobile
    cricket
    metroPCS
    tracfone
    US cellular
    virgin
```
#### What I learned from this project

- Familiarized myself with using json to set variables
- Became acquainted with smtplib and how to use it to send SMS messages
