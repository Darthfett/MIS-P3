"""
Task VIII Implement a program which given 
(a) a 9-cell query image region consisting of 3 cells by 3 cells), 
(b) a color histogram specification (for color-based retrieval), and 
(c) a channel id (for the rest of the features), 
identi?es the best 10 matching image regions for each feature and displays the matches.
"""


def query_region(image_id):
    #retrieve cell_coord top left
    cell_coord = raw_input("Enter the coordinate ID for the top left cell in desired query region:  ")
    #retrieve 9 cells
    qr = []
    # row :  if x coord > # of cells in row - 2, then x = row.length -3 (account for index = 0)