#!/usr/bin/python -tt

# This file is part of secretsanta.
#    secretsanta is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    secretsanta is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with secretsanta.  If not, see <http://www.gnu.org/licenses/>.

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
        from_addr = 'Secret Santa <johnsmith@hotmail.com>'
        to_addr  = row[2]
        msg = "\r\n".join([
            "From: " + from_addr,
            "To: " + to_addr,
            "Subject: Secret Santa",
            "",
            "Dear " + row[0][1:] + " (room " + row[1] + ")",
            "",
            "Thanks for participating in the Secret Santa!",
            "",
            "Please find a present for " + row[3] + " (room " + row[4] + ").",
            "",
            "Please reply to this email if you have any questions or issues.",
            "",
            "See you then!",
            "",
            "Santa"
            ])
        username = 'johnsmith@hotmail.com'
        password = 'xxxxxxxx'
        server = smtplib.SMTP('smtp-mail.outlook.com',587) # if Hotmail/Microsoft Outlook
        #server = smtplib.SMTP('smtp.gmail.com:587') # if gmail
        server.ehlo()
        server.starttls()
        server.ehlo()
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