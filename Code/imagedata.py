"""
schema:  (items marked with * denote primary key)
cells(*cell_id, image_id, cell_coord)
color_instance(cell_id, ci_id, ci_value)
channels(channel_id, channel_value)#RGB, YUV, or HSV
dct(cell_id, channel_id, freq_bin_id, freq_bin_value)
grad_angle(cell_id, channel_id, angle_bin_id, angle_bin_value)
grad_amp(cell_id, channel_id, amplitude_bin_id, amplitude_bin_val)
dwt(cell_id, channel_id, wavelet_bin_id, wavelet_bin_value)
"""

import sqlite3
import os.remove as delete

def make_db(fullfilepath):
	conn = sqlite3.connect(fullfilepath)
	cursor = conn.cursor()
	cursor.execute("""CREATE TABLE cells (cell_id integer NOT NULL, image_id text NOT NULL, cell_coord text NOT NULL, PRIMARY KEY (cell_id))""")
	cursor.execute("""CREATE TABLE color_instance (cell_id integer, ci_id text, ci_value integer)""")
	cursor.execute("""CREATE TABLE channels (channel_id text, channel_value text""")
	cursor.execute("""CREATE TABLE dct (cell_id integer,  channel_id text, freq_bin_id text, freq_bin_value integer)""")
	cursor.execute("""CREATE TABLE grad_angle(cell_id integer,  channel_id text, angle_bin_id text, angle_bin_value integer)""")
	cursor.execute("""CREATE TABLE grad_amp(cell_id integer,  channel_id text, amplitude_bin_id text, amplitude_bin_value integer)""")
	cursor.execute("""CREATE TABLE dwt(cell_id integer,  channel_id text, wavelet_bin_id text, wavelet_bin_value integer)""")
def add_cell(image_id, cell_coord):
	cursor.execute("""INSERT INTO cells (?,?)""", image_id, cell_coord)
def add_channels(colorspace):
	if colorspace == 'RGB':
		c1 = 'R'
		c2 = 'G'
		c3 = 'B'
	elif colorspace == 'YUV':
		c1 = 'Y'
		c2 = 'U'
		c3 = 'V'
	elif colorspace == 'HSV':
		c1 = 'H'
		c2 = 'S'
		c3 = 'V'
	else:
		#colorspace = RGB
		c1 = 'R'
		c2 = 'G'
		c3 = 'B'
	channels = [(1, c1),(2, c2), (3, c3)]
	cursor.executemany("""INSERT INTO channels VALUES (?,?)""", channels)
def clear_db(fullfilepath):
	delete(fullfilepath)
def add_dct(cell_id, channel_id, freq_bin_id, freq_bin_value):
	cursor.execute("""INSERT INTO dct VALUES (?,?,?,?)""", cell_id, channel_id, freq_bin_id, freq_bin_value)
def add_grad_angle(cell_id, channel_id, angle_bin_id, angle_bin_value):
	cursor.execute("""INSERT INTO grad_angle VALUES (?,?,?,?)""", cell_id, channel_id, angle_bin_id, angle_bin_value)
def add_grad_amp(cell_id, channel_id, amplitude_bin_id, amplitude_bin_value):
	cursor.execute("""INSERT INTO grad_amp VALUES (?,?,?,?)""", cell_id, channel_id, amplitude_bin_id, amplitude_bin_value)
def add_dwt(cell_id, channel_id, wavelet_bin_id, wavelet_bin_value):
	cursor.execute("""INSERT INTO dwt VALUES (?,?,?,?)""", cell_id, channel_id, wavelet_bin_id, wavelet_bin_value)
def query_db(qrystring):
	cursor.execute(qrystring)