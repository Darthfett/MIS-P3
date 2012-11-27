#Will divide an image into X by X cells.

#Divider function - takes in tuple of channels of WIDTH and HEIGHT
#Have an output tuple
#for each WIDTH*HEIGHT chunk of channel value 3-tuples, group them and push it to the output tuple
#return the output


#(Structure of the output consists of two layers: 	the cells,
#													inside each cell is the channel values of that cell)		
#output	|-> cell1 |-> r or y ch. values
#		|		  |-> g or u ch. values
#		|		  |-> b or v ch. values
#		|
#		|-> cell2 |-> r or y ch. values
#		|		  |-> g or u ch. values
#		|		  |-> b or v ch. values
#		|	.
#		|	.
#		|	.
#		|
#		|-> cellN |-> r or y ch. values
#				  |-> g or u ch. values
#				  |-> b or v ch. values
