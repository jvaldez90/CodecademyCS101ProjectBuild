# name.py
# Project: Anagram Word Generator
# Written by Joy Valdez
# Date Created: April 27, 2021
# Last Updated: May 7, 2021
# This program will ask a user for list of three to six letters.
# Then generate through all possible letter combinations.
# The results will then be printed to the console.

class Anagram:
    lst = []
    def greet():
        print(
            """
#####################################

Welcome to the Anagram Word Generator

#####################################
            """)
    def farewell():
        print(
            """
#####################################

GAME OVER: Thanks for playing!

#####################################
            """
        )
    def __init__(self, lst):
        self.lst = lst

    def three(self, lst):
        for i in range(len(lst)):
            for j in range(i):
                for k in range(j):
                    if (j != i and j != k):
                       print(lst[k]+""+lst[j]+""+lst[i]+"\t"+ 
                       lst[k]+""+lst[i]+""+lst[j]+"\t"+
                       lst[j]+""+lst[k]+""+lst[i]+"\t"+
                       lst[j]+""+lst[i]+""+lst[k]+"\t"+
                       lst[i]+""+lst[j]+""+lst[k]+"\t"+
                       lst[i]+""+lst[k]+""+lst[j]+"\t")
    def four(self, lst):
        for i in range(len(lst)):
            for j in range(i):
                for k in range(j):
                    for l in range(k):
                        if (j != i and j != k and l != k):
                            # SET 1 [l][*][*][*]
                            print(lst[l]+""+lst[k]+""+lst[j]+""+lst[i]+"\t"+
                                  lst[l]+""+lst[k]+""+lst[i]+""+lst[j]+"\t"+
                                  lst[l]+""+lst[j]+""+lst[k]+""+lst[i]+"\t"+
                                  lst[l]+""+lst[j]+""+lst[i]+""+lst[k]+"\t"+
                                  lst[l]+""+lst[i]+""+lst[j]+""+lst[k]+"\t"+
                                  lst[l]+""+lst[i]+""+lst[k]+""+lst[j]+"\t")
                            # SET 2 [*][l][*][*]
                            print(lst[k]+""+lst[l]+""+lst[j]+""+lst[i]+"\t"+
                                  lst[k]+""+lst[l]+""+lst[i]+""+lst[j]+"\t"+
                                  lst[j]+""+lst[l]+""+lst[k]+""+lst[i]+"\t"+
                                  lst[j]+""+lst[l]+""+lst[i]+""+lst[k]+"\t"+
                                  lst[i]+""+lst[l]+""+lst[j]+""+lst[k]+"\t"+
                                  lst[i]+""+lst[l]+""+lst[k]+""+lst[j]+"\t")
                            # SET 3 [*][*][l][*]
                            print(lst[k]+""+lst[j]+""+lst[l]+""+lst[i]+"\t"+
                                  lst[k]+""+lst[i]+""+lst[l]+""+lst[j]+"\t"+
                                  lst[j]+""+lst[k]+""+lst[l]+""+lst[i]+"\t"+
                                  lst[j]+""+lst[i]+""+lst[l]+""+lst[k]+"\t"+
                                  lst[i]+""+lst[j]+""+lst[l]+""+lst[k]+"\t"+
                                  lst[i]+""+lst[k]+""+lst[l]+""+lst[j]+"\t")
                            # SET 4 [*][*][*][l]
                            print(lst[k]+""+lst[j]+""+lst[i]+""+lst[l]+"\t"+
                                  lst[k]+""+lst[i]+""+lst[j]+""+lst[l]+"\t"+
                                  lst[j]+""+lst[k]+""+lst[i]+""+lst[l]+"\t"+
                                  lst[j]+""+lst[i]+""+lst[k]+""+lst[l]+"\t"+
                                  lst[i]+""+lst[j]+""+lst[k]+""+lst[l]+"\t"+
                                  lst[i]+""+lst[k]+""+lst[j]+""+lst[l]+"\t")
    def five(self,lst):
        for i in range((len(lst))):
            for j in range(i):
                for k in range(j):
                    for l in range(k):
                        for m in range(l):
                            if (j != i and k != j and l != k and m != l):
                                ## SET 1
                                # Block Set 1A [m}[l][*][*][*]
                                print(lst[m]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[i]+"\t"+
                                      lst[m]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[j]+"\t"+
                                      lst[m]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[i]+"\t"+
                                      lst[m]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[k]+"\t"+
                                      lst[m]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[k]+"\t"+
                                      lst[m]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[j]+"\t")
                                # Block Set 1B [l][m][*][*][*]
                                print(lst[l]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[i]+"\t"+
                                      lst[l]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[j]+"\t"+
                                      lst[l]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[i]+"\t"+
                                      lst[l]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[k]+"\t"+
                                      lst[l]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[k]+"\t"+
                                      lst[l]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[j]+"\t")
                                # Block Set 1C [l][*][m][*][*]
                                print(lst[l]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[i]+"\t"+
                                      lst[l]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[j]+"\t"+
                                      lst[l]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[i]+"\t"+
                                      lst[l]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[k]+"\t"+
                                      lst[l]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[k]+"\t"+
                                      lst[l]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[j]+"\t")
                                # Block Set 1D [l][*][*][m][*]
                                print(lst[l]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[i]+"\t"+
                                      lst[l]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[j]+"\t"+
                                      lst[l]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[i]+"\t"+
                                      lst[l]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[k]+"\t"+
                                      lst[l]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[k]+"\t"+
                                      lst[l]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[j]+"\t")
                                # Block Set 1E [l][*][*][*][m]
                                print(lst[l]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[m]+"\t"+
                                      lst[l]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[m]+"\t"+
                                      lst[l]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[m]+"\t"+
                                      lst[l]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[m]+"\t"+
                                      lst[l]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[m]+"\t"+
                                      lst[l]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[m]+"\t")
                                ## SET 2
                                # Block Set 2A [m][*][l][*][*]
                                print(lst[m]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[i]+"\t"+
                                      lst[m]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[j]+"\t"+
                                      lst[m]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[i]+"\t"+
                                      lst[m]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[k]+"\t"+
                                      lst[m]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[k]+"\t"+
                                      lst[m]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[j]+"\t")
                                # Block Set 2B [*][m][l][*][*]
                                print(lst[k]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[i]+"\t"+
                                      lst[k]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[j]+"\t"+
                                      lst[j]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[i]+"\t"+
                                      lst[j]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[j]+"\t")
                                # Block Set 2C [*][l][m][*][*]
                                print(lst[k]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[i]+"\t"+
                                      lst[k]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[j]+"\t"+
                                      lst[j]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[i]+"\t"+
                                      lst[j]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[j]+"\t")
                                # Block Set 2D [*][l][*][m][*]
                                print(lst[k]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[i]+"\t"+
                                      lst[k]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[j]+"\t"+
                                      lst[j]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[i]+"\t"+
                                      lst[j]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[j]+"\t")
                                # Block Set 2E [*][l][*][*][m]
                                print(lst[k]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[m]+"\t"+
                                      lst[k]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[m]+"\t"+
                                      lst[j]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[m]+"\t"+
                                      lst[j]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[m]+"\t"+
                                      lst[i]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[m]+"\t"+
                                      lst[i]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[m]+"\t")
                                ## SET 3
                                # Block Set 3A [m][*][*][l][*]
                                print(lst[m]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[i]+"\t"+
                                      lst[m]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[j]+"\t"+
                                      lst[m]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[i]+"\t"+
                                      lst[m]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[k]+"\t"+
                                      lst[m]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[k]+"\t"+
                                      lst[m]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[j]+"\t")
                                # Block Set 3B [*][m][*][l][*]
                                print(lst[k]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[i]+"\t"+
                                      lst[k]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[j]+"\t"+
                                      lst[j]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[i]+"\t"+
                                      lst[j]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[j]+"\t")
                                # Block Set 3C [*][*][m][l][*]
                                print(lst[k]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[i]+"\t"+
                                      lst[k]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[j]+"\t"+
                                      lst[j]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[i]+"\t"+
                                      lst[j]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[j]+"\t")
                                # Block Set 3D [*][*][l][m][*]
                                print(lst[k]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[i]+"\t"+
                                      lst[k]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[j]+"\t"+
                                      lst[j]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[i]+"\t"+
                                      lst[j]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[k]+"\t"+
                                      lst[i]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[j]+"\t")
                                # Block Set 3E [*][*][l][*][m]
                                print(lst[k]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[m]+"\t"+
                                      lst[k]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[m]+"\t"+
                                      lst[j]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[m]+"\t"+
                                      lst[j]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[m]+"\t"+
                                      lst[i]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[m]+"\t"+
                                      lst[i]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[m]+"\t")
                                ## SET 4
                                # Block Set 4A [m][*][*][*][l]
                                print(lst[m]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[l]+"\t"+
                                      lst[m]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[l]+"\t"+
                                      lst[m]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[l]+"\t"+
                                      lst[m]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[l]+"\t"+
                                      lst[m]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[l]+"\t"+
                                      lst[m]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[l]+"\t")
                                # Block Set 4B [*][m][*][*][l]
                                print(lst[k]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[l]+"\t"+
                                      lst[k]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[l]+"\t"+
                                      lst[j]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[l]+"\t"+
                                      lst[j]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[l]+"\t"+
                                      lst[i]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[l]+"\t"+
                                      lst[i]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[l]+"\t")
                                # Block Set 4C [*][*][m][*][l]
                                print(lst[k]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[l]+"\t"+
                                      lst[k]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[l]+"\t"+
                                      lst[j]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[l]+"\t"+
                                      lst[j]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[l]+"\t"+
                                      lst[i]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[l]+"\t"+
                                      lst[i]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[l]+"\t")
                                # Block Set 4D [*][*][*][m][l]
                                print(lst[k]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[l]+"\t"+
                                      lst[k]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[l]+"\t"+
                                      lst[j]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[l]+"\t"+
                                      lst[j]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[l]+"\t"+
                                      lst[i]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[l]+"\t"+
                                      lst[i]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[l]+"\t")
                                # Block Set 4E [*][*][*][l][m]
                                print(lst[k]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[m]+"\t"+
                                      lst[k]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[m]+"\t"+
                                      lst[j]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[m]+"\t"+
                                      lst[j]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[m]+"\t"+
                                      lst[i]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[m]+"\t"+
                                      lst[i]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[m]+"\t")
    def six(self,lst):
        for i in range((len(lst))):
            for j in range(i):
                for k in range(j):
                    for l in range(k):
                        for m in range(l):
                            for n in range(m):
                                if (j != i and k != j and l != m and n != m):
                                    ### SET 1A
                                    # Block Set 1A1 [n][m][l][*][*][*]
                                    print(lst[n]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1A2 [m][n][l][*][*][*]
                                    print(lst[m]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1A3 [m][l][n][*][*][*]
                                    print(lst[m]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1A4 [m][l][*][n][*][*]
                                    print(lst[m]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1A5 [m][l][*][*][n][*]
                                    print(lst[m]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 1A6 [m][l][*][*][*][n]
                                    print(lst[m]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 1B
                                    # Block Set 1B1 [n][l][m][*][*][*]
                                    print(lst[n]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1B2 [l][n][m][*][*][*]
                                    print(lst[l]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1B3 [l][m][n][*][*][*]
                                    print(lst[l]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1B4 [l][m][*][n][*][*]
                                    print(lst[l]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1B5 [l][m][*][*][n][*]
                                    print(lst[l]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 1B6 [l][m][*][*][*][n]
                                    print(lst[l]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 1C
                                    # Block Set 1C1 [n][l][*][m][*][*]
                                    print(lst[n]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1C2 [l][n][*][m][*][*]
                                    print(lst[l]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1C3 [l][*][n][m][*][*]
                                    print(lst[l]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1C4 [l][*][m][n][*][*]
                                    print(lst[l]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 1C5 [l][*][m][*][n][*]
                                    print(lst[l]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 1C6 [l][*][m][*][*][n]
                                    print(lst[l]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 1D
                                    # Block Set 1D1 [n][l][*][*][m][*]
                                    print(lst[n]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 1D2 [l][n][*][*][m][*]
                                    print(lst[l]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 1D3 [l][*][n][*][m][*]
                                    print(lst[l]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 1D4 [l][*][*][n][m][*]
                                    print(lst[l]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 1D5 [l][*][*][m][n][*]
                                    print(lst[l]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 1D6 [l][*][*][m][*][n]
                                    print(lst[l]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 1E
                                    # Block Set 1E1 [n][l][*][*][*][m]
                                    print(lst[n]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 1E2 [l][n][*][*][*][m]
                                    print(lst[l]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 1E3 [l][*][n][*][*][m]
                                    print(lst[l]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 1E4 [l][*][*][n][*][m]
                                    print(lst[l]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 1E5 [l][*][*][*][n][m]
                                    print(lst[l]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[m]+"\t")
                                    # Block Set 1E6 [l][*][*][*][m][n]
                                    print(lst[l]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[l]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[n]+"\t")
                                    ### SET 2A
                                    # Block Set 2A1 [n][m][*][l][*][*]
                                    print(lst[n]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2A2 [m][n][*][l][*][*]
                                    print(lst[m]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2A3 [m][*][n][l][*][*]
                                    print(lst[m]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2A4 [m][*][l][n][*][*]
                                    print(lst[m]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2A5 [m][*][l][*][n][*]
                                    print(lst[m]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 2A6 [m][*][l][*][*][n]
                                    print(lst[m]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[n]+"\t")
                                    #### SET 2B
                                    # Block Set 2B1 [n][*][m][l][*][*]
                                    print(lst[n]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2B2 [*][n][m][l][*][*]
                                    print(lst[k]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2B3 [*][m][n][l][*][*]
                                    print(lst[k]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2B4 [*][m][l][n][*][*]
                                    print(lst[k]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2B5 [*][m][l][*][n][*]
                                    print(lst[k]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 2B6 [*][m][l][*][*][n]
                                    print(lst[k]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 2C
                                    # Block Set 2C1 [n][*][l][m][*][*]
                                    print(lst[n]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2C2 [*][n][l][m][*][*]
                                    print(lst[k]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2C3 [*][l][n][m][*][*]
                                    print(lst[k]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2C4 [*][l][m][n][*][*]
                                    print(lst[k]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[j]+"\t")
                                    # Block Set 2C5 [*][l][m][*][n][*]
                                    print(lst[k]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 2C6 [*][l][m][*][*][n]
                                    print(lst[k]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 2D
                                    # Block Set 2D1 [n][*][l][*][m][*]
                                    print(lst[n]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 2D2 [*][n][l][*][m][*]
                                    print(lst[k]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 2D3 [*][l][n][*][m][*]
                                    print(lst[k]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 2D4 [*][l][*][n][m][*]
                                    print(lst[k]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 2D5 [*][l][*][m][n][*]
                                    print(lst[k]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 2D6 [*][l][*][m][*][n]
                                    print(lst[k]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 2E
                                    # Block Set 2E1 [n][*][l][*][*][m]
                                    print(lst[n]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 2E2 [*][n][l][*][*][m]
                                    print(lst[k]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 2E3 [*][l][n][*][*][m]
                                    print(lst[k]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 2E4 [*][l][*][n][*][m]
                                    print(lst[k]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 2E5 [*][l][*][*][n][m]
                                    print(lst[k]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[m]+"\t")
                                    # Block Set 2E6 [*][l][*][*][m][n]
                                    print(lst[k]+""+lst[l]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[l]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[l]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[l]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[n]+"\t")
                                    ### SET 3A
                                    # Block Set 3A1 [n][m][*][*][l][*]
                                    print(lst[n]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3A2 [m][n][*][*][l][*]
                                    print(lst[m]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3A3 [m][*][n][*][l][*]
                                    print(lst[m]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3A4 [m][*][*][n][l][*]
                                    print(lst[m]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3A5 [m][*][*][l][n][*]
                                    print(lst[m]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 3A6 [m][*][*][l][*][n]
                                    print(lst[m]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 3B
                                    # Block Set 3B1 [n][*][m][*][l][*]
                                    print(lst[n]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3B2 [*][n][m][*][l][*]
                                    print(lst[k]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3B3 [*][m][n][*][l][*]
                                    print(lst[k]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3B4 [*][m][*][n][l][*]
                                    print(lst[k]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3B5 [*][m][*][l][n][*]
                                    print(lst[k]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 3B6 [*][m][*][l][*][n]
                                    print(lst[k]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 3C
                                    # Block Set 3C1 [n][*][*][m][l][*]
                                    print(lst[n]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3C2 [*][n][*][m][l][*]
                                    print(lst[k]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3C3 [*][*][n][m][l][*]
                                    print(lst[k]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3C4 [*][*][m][n][l][*]
                                    print(lst[k]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[l]+""+lst[j]+"\t")
                                    # Block Set 3D5 [*][*][m][l][n][*]
                                    print(lst[k]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 3D6 [*][*][m][l][*][n]
                                    print(lst[k]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 3D
                                    # Block Set 3D1 [n][*][*][l][m][*]
                                    print(lst[n]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 3D2 [*][n][*][l][m][*]
                                    print(lst[k]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 3D3 [*][*][n][l][m][*]
                                    print(lst[k]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 3D4 [*][*][l][n][m][*]
                                    print(lst[k]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[m]+""+lst[j]+"\t")
                                    # Block Set 3D5 [*][*][l][m][n][*]
                                    print(lst[k]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[j]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[i]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[k]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[n]+""+lst[j]+"\t")
                                    # Block Set 3D6 [*][*][l][m][*][n]
                                    print(lst[k]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[i]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[k]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[j]+""+lst[n]+"\t")
                                    ### SET 3E
                                    # Block Set 3E1 [n][*][*][l][*][m]
                                    print(lst[n]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 3E2 [*][n][*][l][*][m]
                                    print(lst[k]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 3E3 [*][*][n][l][*][m]
                                    print(lst[k]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 3E4 [*][*][l][n][*][m]
                                    print(lst[k]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[i]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[k]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[j]+""+lst[m]+"\t")
                                    # Block Set 3E5 [*][*][l][*][n][m]
                                    print(lst[k]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[n]+""+lst[m]+"\t")
                                    # Block Set 3E6 [*][*][l][*][m][n]
                                    print(lst[k]+""+lst[j]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[l]+""+lst[i]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[l]+""+lst[k]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[l]+""+lst[j]+""+lst[m]+""+lst[n]+"\t")
                                    ### SET 4A
                                    # Block Set 4A1 [n][m][*][*][*][l]
                                    print(lst[n]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4A2 [m][n][*][*][*][l]
                                    print(lst[m]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4A3 [m][*][n][*][*][l]
                                    print(lst[m]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4A4 [m][*][*][n][*][l]
                                    print(lst[m]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4A5 [m][*][*][*][n][l]
                                    print(lst[m]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[l]+"\t")
                                    # Block Set 4A6 [m][*][*][*][l][n]
                                    print(lst[m]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[m]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[n]+"\t")
                                    ### SET 4B
                                    # Block Set 4B1 [n][*][m][*][*][l]
                                    print(lst[n]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4B2 [*][n][m][*][*][l]
                                    print(lst[k]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4B3 [*][m][n][*][*][l]
                                    print(lst[k]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4B4 [*][m][*][n][*][l]
                                    print(lst[k]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4B5 [*][m][*][*][n][l]
                                    print(lst[k]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[l]+"\t")
                                    # Block Set 4B6 [*][m][*][*][l][n]
                                    print(lst[k]+""+lst[m]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[m]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[m]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[m]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[n]+"\t")
                                    ### SET 4C
                                    # Block Set 4C1 [n][*][*][m][*][l]
                                    print(lst[n]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4C2 [*][n][*][m][*][l]
                                    print(lst[k]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4C3 [*][*][n][m][*][l]
                                    print(lst[k]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4C4 [*][*][m][n][*][l]
                                    print(lst[k]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[i]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[k]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[j]+""+lst[l]+"\t")
                                    # Block Set 4C5 [*][*][m][*][n][l]
                                    print(lst[k]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[n]+""+lst[l]+"\t")
                                    # Block Set 4C6 [*][*][m][*][l][n]	
                                    print(lst[k]+""+lst[j]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[m]+""+lst[i]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[m]+""+lst[k]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[m]+""+lst[j]+""+lst[l]+""+lst[n]+"\t")
                                    ### SET 4D
                                    # Block Set 4D1 [n][*][*][*][m][l]
                                    print(lst[n]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[l]+"\t")
                                    # Block Set 4D2 [*][n][*][*][m][l]
                                    print(lst[k]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[l]+"\t")
                                    # Block Set 4D3 [*][*][n][*][m][l]
                                    print(lst[k]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[m]+""+lst[l]+"\t")
                                    # Block Set 4D4 [*][*][*][n][m][l]
                                    print(lst[k]+""+lst[j]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[m]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[m]+""+lst[l]+"\t")
                                    # Block Set 4D5 [*][*][*][m][n][l]
                                    print(lst[k]+""+lst[j]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[n]+""+lst[l]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[n]+""+lst[l]+"\t")
                                    # Block Set 4D6 [*][*][*][m][l][n]
                                    print(lst[k]+""+lst[j]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[k]+""+lst[m]+""+lst[l]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[j]+""+lst[m]+""+lst[l]+""+lst[n]+"\t")
                                    ### SET 4E
                                    # Block Set 4E1 [n][*][*][*][l][m]
                                    print(lst[n]+""+lst[k]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[k]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[j]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[n]+""+lst[i]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[m]+"\t")
                                    # Block Set 4E2 [*][n][*][*][l][m]
                                    print(lst[k]+""+lst[n]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[n]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[n]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[n]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[m]+"\t")
                                    # Block Set 4E3 [*][*][n][*][l][m]
                                    print(lst[k]+""+lst[j]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[n]+""+lst[i]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[n]+""+lst[k]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[n]+""+lst[j]+""+lst[l]+""+lst[m]+"\t")
                                    # Block Set 4E4 [*][*][*][n][l][m]
                                    print(lst[k]+""+lst[j]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[i]+""+lst[n]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[k]+""+lst[n]+""+lst[l]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[j]+""+lst[n]+""+lst[l]+""+lst[m]+"\t")
                                    # Block Set 4E5 [*][*][*][l][n][m]
                                    print(lst[k]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[n]+""+lst[m]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[n]+""+lst[m]+"\t")
                                    # Block Set 4E6 [*][*][*][l][m][n]
                                    print(lst[k]+""+lst[j]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[k]+""+lst[i]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[k]+""+lst[i]+""+lst[l]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[j]+""+lst[i]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[j]+""+lst[k]+""+lst[l]+""+lst[m]+""+lst[n]+"\t"+
                                          lst[i]+""+lst[k]+""+lst[j]+""+lst[l]+""+lst[m]+""+lst[n]+"\t")
        
# TESTING METHODS
# my_list = ['c','a','t']
# print("TESTING: my_list = ['c','a','t']")
# anagram1 = Anagram(my_list)
# anagram1.three(my_list)

# ANAGRAM GAME STARTS HERE
Anagram.greet()
game_over = False
while not game_over:
    print('What letters are to unscramble? Please separate each letter with a space.')
    new_list = input().split()
    if len(new_list) < 3:
          print(new_list)
          print("OOPS! That's not enough letters. Try again.")
          game_over  = False
          print()
    elif len(new_list) > 6:
          print(new_list)
          print("Whoa! That's too many letters. Try again.")
          game_over = False
          print()
    else:
        if len(new_list) == 3:
            print(new_list)
            anagram3 = Anagram(new_list)
            anagram3.three(new_list)
            print("\nDo you want to play again?")
            user = input('1 for yes or 0 for n ')
            answer = int(user)
            if answer == 0:
                game_over = True
                Anagram.farewell()
            else:
                print('ERROR!. Invalid input.\nSetting input to 1')
                answer = 1
                game_pver = False
        elif len(new_list) == 4:
            print(new_list)
            anagram4 = Anagram(new_list)
            anagram4.four(new_list)
            print("\nDo you want to play again?")
            user = input('1 for yes or 0 for n ')
            answer = int(user)
            if answer == 0:
                game_over = True
                Anagram.farewell()
            else:
                print('ERROR!. Invalid input.\nSetting input to 1')
                answer = 1
                game_pver = False
        elif len(new_list) == 5:
            print(new_list)
            anagram5 = Anagram(new_list)
            anagram5.five(new_list)
            print("\nDo you want to play again?")
            user = input('1 for yes or 0 for n ')
            answer = int(user)
            if answer == 0:
                game_over = True
                Anagram.farewell()
            else:
                print('ERROR!. Invalid input.\nSetting input to 1')
                answer = 1
                game_pver = False
        else:
            print(new_list)
            anagram6 = Anagram(new_list)
            anagram6.six(new_list)
            print("\nDo you want to play again?")
            user = input('1 for yes or 0 for n ')
            answer = int(user)
            if answer == 0:
                game_over = True
                Anagram.farewell()
            else:
                print('ERROR!. Invalid input.\nSetting input to 1')
                answer = 1
                game_pver = False
