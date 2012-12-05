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
from os import remove as delete
from os import path as path
import os
 
class myDB(object):
    def __init__(self, filename):
        default_db_location = os.path.realpath(path.join(path.split(__file__)[0], "../", "Databases"))
        self.conn = sqlite3.connect(path.join(default_db_location, filename))
        self.cursor = self.conn.cursor()
    def make_db(self):
        self.cursor.execute("CREATE TABLE cells (cell_id integer NOT NULL, image_id text NOT NULL, cell_coord text NOT NULL, PRIMARY KEY (cell_id))")
        self.cursor.execute("CREATE TABLE color_instance (cell_id integer, ci_id text, ci_value integer)")
        self.cursor.execute("CREATE TABLE channels (channel_id text, channel_value text)")
        self.cursor.execute("CREATE TABLE dct (cell_id integer,  channel_id text, freq_bin_id text, freq_bin_value integer)")
        self.cursor.execute("CREATE TABLE grad_angle(cell_id integer,  channel_id text, angle_bin_id text, angle_bin_value integer)")
        self.cursor.execute("CREATE TABLE grad_amp(cell_id integer,  channel_id text, amplitude_bin_id text, amplitude_bin_value integer)")
        self.cursor.execute("CREATE TABLE dwt(cell_id integer,  channel_id text, wavelet_bin_id text, wavelet_bin_value integer)")
        self.conn.commit()
    def add_cell(self, image_id, cell_coord):
        info = [image_id, cell_coord]
        self.cursor.execute("INSERT INTO cells VALUES (NULL, ?, ?)", info)
        self.conn.commit()
    def get_cell_id(self, image_id, cell_coord):
        info = [image_id, cell_coord]
        self.cursor.execute("SELECT cell_id FROM cells WHERE image_id = (?) AND cell_coord =(?)", info)
    def add_channels(colorspace):
        if colorspace in {'RGB', 'YUV', 'HSV'}:
            c = colorspace
        else:
            c = 'RGB'
        
        channels = zip(range(1,4), c)
        self.cursor.executemany("""INSERT INTO channels VALUES (?,?)""", channels)
        channels = [(1, c1),(2, c2), (3, c3)]
        self.cursor.executemany("INSERT INTO channels VALUES (?,?)", channels)
        self.conn.commit()
    def clear_db(fullfilepath):
        self.conn.close()
        delete(fullfilepath)
    def add_dct(self, cell_id, channel_id, freq_bin_id, freq_bin_value):
        info = [cell_id, channel_id, freq_bin_id, freq_bin_value]
        self.cursor.execute("INSERT INTO dct VALUES (?,?,?,?)", info)
        self.conn.commit()
    def add_grad_angle(self, cell_id, channel_id, angle_bin_id, angle_bin_value):
        info = [cell_id, channel_id, angle_bin_id, angle_bin_value]
        self.cursor.execute("INSERT INTO grad_angle VALUES (?,?,?,?)", info)
    def add_grad_amp(self, cell_id, channel_id, amplitude_bin_id, amplitude_bin_value):
        info = [cell_id, channel_id, amplitude_bin_id, amplitude_bin_value]
        self.cursor.execute("INSERT INTO grad_amp VALUES (?,?,?,?)", info)
        self.conn.commit()
    def add_dwt(self, cell_id, channel_id, wavelet_bin_id, wavelet_bin_value):
        info = [cell_id, channel_id, wavelet_bin_id, wavelet_bin_value]
        self.cursor.execute("INSERT INTO dwt VALUES (?,?,?,?)", info)
        self.conn.commit()
    def query_db(self, qrystring):
        self.cursor.execute(qrystring)
        self.conn.commit()
    