import numpy as np
from astropy.table import Table #import the Table class
from astropy.io import ascii # ascii plain text io
from astropy.io import fits # FITS format io

def sinvx():
    x = np.linspace(0,2*(np.pi),1000) 
    sinX = np.sin(x)
    data = Table([sinX,x],names=['sin(x)','x']) #create a talbe
    ascii.write(data, 'table.txt', format='commented_header') # write the table to file
    data_in = ascii.read('table.txt') #read the data in
    print(data_in)

if __name__ == "__main__":
    sinvx()
