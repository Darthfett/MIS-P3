"""
Task VIII Implement a program which given 
(a) a 9-cell query image region consisting of 3 cells by 3 cells), 
(b) a color histogram specification (for color-based retrieval), and 
(c) a channel id (for the rest of the features), 
identi?es the best 10 matching image regions for each feature and displays the matches.
"""
import task_II

def query_region():
    #get data for these 9 cells via processing of given image
    print("================ Task II ================")
    task_II.histogram_generator(image, image_id, color_space)
    
    print("================ Task III ================")
    image, image_id = get_image()
    task_III.dct_freq(image, image_id, color_space)
    
    print("================ Task IV ================")
    image, image_id = get_image()
    task_IV.do_task_4(image, image_id, color_space)
	
    print("================ Task V ================")
    image, image_id = get_image()
    task_V.do_task_5(image, image_id, color_space)
	
    print("================ Task VI ================")
    image, image_id = get_image()
    task_VI.dwt_freq(image, image_id, color_space)
    #retrieve cell_coord top left
    cell_coord = raw_input("Enter the coordinate ID for the top left cell in desired query region:  ")
    #retrieve 9 cells
    qr = []
    # row :  if x coord > # of cells in (row - 2), then x(an index #)= row.length -3 (account for index = 0)
    
    
    #using general historgram spec from task one
    histospec = get_histogram_spec()
    
    