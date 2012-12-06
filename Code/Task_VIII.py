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
    
    if coord % new_width >= (new_width - 2):
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
            qr.append(coord + x + (new_width * y))  #now we have a list of 3 x 3 coord_ids
            
    #using general historgram spec from task one
    histospec = get_histogram_spec()
    
    #need to get features of SELECTED COORDINATE CELLS from the lists created above.
    #each list above ids the coordinate by the index of the list item
    #simply need to referecne the coordinate id to get from ea list above
    cellinfo = []
    for index, coord in qr:
        cellinfoname = str(coord)  #uniquely name the dictionary of features
        cellinfoname = {'histogram': ihist[coord], 'dct': idct[coord], 'angle': iangle[coord], 'amplitude': iamp[coord], 'dwt': idwt[coord]}
        cellinfo[index] = cellinfoname  #should place a dictionary in each index of cellinfo
    
    #using Euclidean distance, need to identify "10 best image regions" for each feature
    #   For each feature item in dictionary, iterate through corresponding database table, gathering
    #   the values that EQUAL the query's value.  If more than 10 hits, keep going until no more matches, or #   list contains 50 values. If less than 10, find all instances that are +/- 1 up to 50 values.  List #   these cell_ids.  
    #   
    #   At the end of this, there will be one list containing up to 50 cell_ids per feature (5 lists)
    #
    #   Gather all cell_ids which are in all 5 lists.
    #   If less than 10 cell_ids, find all that are in 4 lists.
    #   Use Euclidean distance to determine best matches.  (using actual values of given feature from chosen #   cells)
    #   Smallest values rank higher
    #   Treat the features as a 5-tuple vector:  <histogram, dct, angle, amplitude, dwt>  (think:  linear alg)
    #display the matches 
    
    