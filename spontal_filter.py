#!/usr/bin/env python
#Hennie Veldthuis

import sys
import xml.etree.ElementTree as ET

def main(argv):
    if len(argv) == 3:
        tree = ET.parse(argv[1])
        root = tree.getroot()
        
        for point in root:
            f0_start  = float(point[13].text)
            f0_end    = float(point[12].text)
            bottom_hz = float(point[5].text)
            top_hz    = float(point[7].text)
            if not((f0_start > bottom_hz) and (f0_start < top_hz) and (f0_end > bottom_hz) and (f0_end < top_hz)):
                # values are incorrect,
                # remove item
                root.remove(point)
        
        tree.write(argv[2])
    else:
        print("ERROR, not enough arguments, use: python3 spontal_test.py spontal.xml spontal_filtered.xml")
    
if __name__ == '__main__':
    main(sys.argv)
