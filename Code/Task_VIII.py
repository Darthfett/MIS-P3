"""
Task VIII Implement a program which given 
(a) a 9-cell query image region consisting of 3 cells by 3 cells), 
(b) a color histogram specification (for color-based retrieval), and 
(c) a channel id (for the rest of the features), 
identi?es the best 10 matching image regions for each feature and displays the matches.
"""
import task_II
import task_III
import task_IV
import task_V
import task_VI

def query_region():
    image, image_id = get_image()
    width, height = image.size
    
    new_height = int(ceil(height / 8))#cells in a column
    new_width = int(ceil(width / 8))#cells in a row
    print("================ Task II ================")
    ihist = task_II.histogram_generator(image, image_id, color_space)
    
    print("================ Task III ================")
    idct = task_III.dct_freq(image, image_id, color_space)
    
    print("================ Task IV ================")
    iangle = task_IV.do_task_4(image, image_id, color_space)
	
    print("================ Task V ================")
    iamp = task_V.do_task_5(image, image_id, color_space)
	
    print("================ Task VI ================")
    idwt = task_VI.dwt_freq(image, image_id, color_space)
    
    #retrieve cell_coord top left
    coord = raw_input("Enter the coordinate ID for the top left cell in desired query region:  ")
    #retrieve 9 cells
    qr = []
    
    # this gets our <0,0> for the region
    # row :  if x coord > # of cells in (row - 2), then x(an index #)= row.length -3 (account for index = 0)
    
    if coord % new_width >= (new_width -2):
        x = new_width - 3
    else:
        x = coord % new_width
    if coord // new_height >= (new_height - 2):
        y = new_height - 3
    else:
        y = coord // new_height    
    coord = x + new_width *y
    
    for y in range (3):
        for x in range (3):
            qr.append(coord + x + (new_width * y))
            
    #using general historgram spec from task one
    histospec = get_histogram_spec()
    
    