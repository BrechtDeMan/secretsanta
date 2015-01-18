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

"""A 'Secret Santa' pairing script. Based on a list of names, email addresses
    and room numbers, it generates pairs such that a person won't have to buy 
    a present for themselves, their family members, or the person who has to 
    buy a present for them.
    The result is stored as a csv file.
    """

import sys
import csv
import random

"""Read csv with names, email addresses and room numbers of participants
    """
def read_file():
    with open('list.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        giver_list = list(reader)
        giver_list = giver_list[1:] # remove first row
        return giver_list

""" Write csv with names, email addresses and room numbers of givers and receivers
    """
def write_file(givers_list, rand_vec):
    with open('pairs.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for ind in range(givers_list.__len__()):
            writer.writerow([givers_list[ind][1] + ',' + givers_list[ind][2]
                + ',' + givers_list[ind][3]
                + ',' + givers_list[rand_vec[ind]][1] + ','
                + givers_list[rand_vec[ind]][2] + ',' + givers_list[rand_vec[ind]][3]])

""" Define a main() function that calls the necessary functions.
    """
def main():
    # Get givers list and generate receivers list
    givers_list = read_file() # read csv file
    N = givers_list.__len__() # number of participants
    rand_vec = list(range(N)) # array of indices
    max_iterations = 1000
    iteration = 0
    conditions_met = False
    while iteration<max_iterations and not conditions_met:
        iteration += 1           # increment iteration number
        random.shuffle(rand_vec) # randomise array of indices
        conditions_met = True    # unless one of following breaks
        for ind in range(N):     # go over all indices of random index vector
            # Condition 1: not to themselves
            if rand_vec[ind] == ind:
                conditions_met = False
                break
            # Condition 2: not to their own Secret Valentine
            elif rand_vec[rand_vec[ind]] == ind:
                conditions_met = False
                break
            # Condition 3: not to 'roommates' (people with same room number listed)
            elif givers_list[ind][2] == givers_list[rand_vec[ind]][2]:
                conditions_met = False
                break
    write_file(givers_list, rand_vec) # write csv file with pairs
    for ind in range(N): # print in Terminal
        print givers_list[ind][1], "(", givers_list[ind][2], ") to", \
            givers_list[rand_vec[ind]][1], "(", givers_list[rand_vec[ind]][2], ")"
    print "Number of iterations needed: ", iteration # Print number of iterations

""" This is the standard boilerplate that calls the main() function.
    """
if __name__ == '__main__':
    main()