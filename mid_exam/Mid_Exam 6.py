"""
Name: {orrasa jomchana}
SID: {364211760044}
Group: {MIT212}
"""

try:
    year = int(input( 'Input (ค.ศ.):' ))
except:
    year = 0

if year > 0:
    x = year + 543
    print('Output (พ.ศ.):',x,)