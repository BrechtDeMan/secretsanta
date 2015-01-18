#!/usr/bin/python -tt
# TODO: add license

"""A 'Secret Santa' emailing application. It reads a csv file containing 
    names, room numbers and email addresses from both 'givers' and 'receivers', 
    as paired by the pairing.py script.
    Remember to remove your email password before sharing!
    """

import sys
import csv
import smtplib

""" Send email to gift buyers with info on their secret gift receiver
    """
def send_email(pair_list):
    for row in pair_list:
        from_addr = 'Goodenough Welfare <goodenoughwelfare@gmail.com>'
        to_addr  = row[2]
        msg = "\r\n".join([
            "From: " + from_addr,
            "To: " + to_addr,
            "Subject: Secret Valentine",
            "",
            "Dear " + row[0][1:] + " (room " + row[1] + ")",
            "",
            "Thanks for participating in the Secret Valentine!",
            "",
            "Please find a present for " + row[3] + " (room " + row[4] + ").",
            "You shouldn't spend over 5 pounds, and homemade presents are highly encouraged.",
            "If you cannot make it to the party, please do let us know and drop the gift in your person's pigeon hole on the day, or deliver it to us so we can hand it over on the party.",
            "",
            "Remember, the Secret Valentine party takes place 9 February at 8pm in the William Goodenough House Large Common Room.",
            "",
            "See you then!",
            "",
            "Your Goodenough Welfare officers"
            ])
        username = 'goodenoughwelfare@gmail.com'
        password = 'thisisnotthepassword'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(from_addr, to_addr, msg)
        server.quit()
        print "Email sent to", row[0][1:], ": ", to_addr # Debug: show confirmation in Terminal

""" Define a main() function that calls the necessary functions.
    """
def main():
    # Import list of givers and receivers
    csvfile = open('pairs.csv')
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    pair_list = list(reader)  # convert csv reader to list
    send_email(pair_list)     # Email receiver to each giver

""" This is the standard boilerplate that calls the main() function.
    """
if __name__ == '__main__':
    main()