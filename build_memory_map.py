import numpy as np
import sqlite3

"""
conn = sqlite3.connect(dir + 'friends.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS MemoryLocation
    (address INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Functions
    (address INTEGER, function TEXT, UNIQUE(address, function))''')
"""

class memory_location(object):
    seen_functions = {}
    def __init__(self, address, name=None):
        """
        address should be an int
        """
        self.address = address
        if name is not None:
            self.name = name
        else:
            self.name = ""
        self.functions = {}
    def add_function(self, f, ref=None, name=None):
        """
        f is just whatever text we find
        ref is a literature reference
        """
        self.functions[f] = ref
        memory_location.seen_functions[f] = True
        if name is not None:
            self.name = name


# Prefill memobjs with ever address from [0x0000..0xFFFF]
memobjs = [memory_location(x) for x in np.arange(0x0000, 0xFFFF+1, 1)]

# So now we have stuff like this...
# In [12]: memobjs[0x0000].address
# Out[12]: 0
# In [13]: memobjs[0x0C00].address
# Out[13]: 3072

def assign_function_to_memory_location(address, f, name=None, ref=None):
    """
    values include stop value, so like this: ``[start, stop]``
    """
    memobjs[address].add_function(f, name=name, ref=ref)

def assign_function_to_memory_range(start, stop, f, ref=None):
    """
    values include stop value, so like this: ``[start, stop]``
    """
    #[memobjs[x].add_function(f, ref) for x in np.arange(start, stop+1)]
    [assign_function_to_memory_location(x, f, ref=ref) for x in np.arange(start, stop+1)]

#########################################
# Apple IIe Technical Reference Manual

## Pg 73
reference = "Figure 4-1, Apple IIe Technical Reference Manual"
assign_function_to_memory_range(0x0000, 0xBFFF, "Main RAM", ref=reference)
assign_function_to_memory_range(0xC000, 0xCFFF, "I/O", ref=reference)
assign_function_to_memory_range(0xD000, 0xFFFF, "ROM", ref=reference)
assign_function_to_memory_range(0xD000, 0xFFFF, "Bank-Switched RAM", ref=reference)

## Pg 85
reference = "Figure 4-4, Apple IIe Technical Reference Manual"
assign_function_to_memory_range(0x2000, 0x5FFF, "High-Resolution Graphics Display Buffers", ref=reference)

## Pg ??
reference = "Table 6-2, Apple IIe Technical Reference Manual"
assign_function_to_memory_range(0xC100, 0xC1FF, "Peripheral-Card ROM", ref=reference)
assign_function_to_memory_range(0xC200, 0xC2FF, "Peripheral-Card ROM", ref=reference)
assign_function_to_memory_range(0xC300, 0xC3FF, "Peripheral-Card ROM", ref=reference)
assign_function_to_memory_range(0xC400, 0xC4FF, "Peripheral-Card ROM", ref=reference)
assign_function_to_memory_range(0xC500, 0xC5FF, "Peripheral-Card ROM", ref=reference)
assign_function_to_memory_range(0xC600, 0xC6FF, "Peripheral-Card ROM", ref=reference)
assign_function_to_memory_range(0xC700, 0xC7FF, "Peripheral-Card ROM", ref=reference)
assign_function_to_memory_range(0xC100, 0xC1FF, "I/O SELECT", ref=reference)
assign_function_to_memory_range(0xC200, 0xC2FF, "I/O SELECT", ref=reference)
assign_function_to_memory_range(0xC300, 0xC3FF, "I/O SELECT", ref=reference)
assign_function_to_memory_range(0xC400, 0xC4FF, "I/O SELECT", ref=reference)
assign_function_to_memory_range(0xC500, 0xC5FF, "I/O SELECT", ref=reference)
assign_function_to_memory_range(0xC600, 0xC6FF, "I/O SELECT", ref=reference)
assign_function_to_memory_range(0xC700, 0xC7FF, "I/O SELECT", ref=reference)
assign_function_to_memory_range(0xC100, 0xC1FF, "Slot 1", ref=reference)
assign_function_to_memory_range(0xC200, 0xC2FF, "Slot 2", ref=reference)
assign_function_to_memory_range(0xC300, 0xC3FF, "Slot 3", ref=reference)
assign_function_to_memory_range(0xC400, 0xC4FF, "Slot 4", ref=reference)
assign_function_to_memory_range(0xC500, 0xC5FF, "Slot 5", ref=reference)
assign_function_to_memory_range(0xC600, 0xC6FF, "Slot 6", ref=reference)
assign_function_to_memory_range(0xC700, 0xC7FF, "Slot 7", ref=reference)

## Pg 141
reference = "Figure 6-3, Apple IIe Technical Reference Manual"
assign_function_to_memory_range(0xC000, 0xC0FF, "Internal Soft Switches and Peripheral I/O", ref=reference)
assign_function_to_memory_range(0xC800, 0xCFFF, "Peripheral Expansion ROM", ref=reference)
assign_function_to_memory_range(0xC800, 0xCFFF, "Peripheral Expansion ROM", ref=reference)

#########################################
# Apple II Family Hardware Information
# https://mirrors.apple2.org.za/Apple%20II%20Documentation%20Project/Companies/Apple/Manuals/Apple%20II%20Family%20Hardware%20Information.pdf

## Pg 6
reference = "Apple II Family Hardware Information"
assign_function_to_memory_range(0xB7E9, 0xB7F4, "RWTS Locations", ref=reference)
assign_function_to_memory_location(0xB7E9, "SLOT * 16", ref=reference)
assign_function_to_memory_location(0xB7EA, "DRIVE", ref=reference)
assign_function_to_memory_location(0xB7EB, "ZERO", ref=reference)
assign_function_to_memory_location(0xB7EC, "TRACK", ref=reference)
assign_function_to_memory_location(0xB7ED, "SECTOR", ref=reference)
assign_function_to_memory_location(0xB7F0, "BUFFER LO", ref=reference)
assign_function_to_memory_location(0xB7F1, "BUFFER HI", ref=reference)
assign_function_to_memory_location(0xB7F3, "ZERO", ref=reference)
assign_function_to_memory_location(0xB7F4, "SEEK/READ/WRITE", ref=reference)

## Pg 7
assign_function_to_memory_location(0x03E3, "LOAD X/Y WITH PARM LIST ADDRESS", ref=reference)
assign_function_to_memory_location(0x03D9, "CALL RWTS (MUST CALL ABOVE FIRST)", ref=reference)
assign_function_to_memory_location(0xB793, "SEEK/READ/WRITE MULTIPLE PAGES", ref=reference)
assign_function_to_memory_location(0xB7E1, "NUMBER OF PAGES", ref=reference)
assign_function_to_memory_location(0xB7E1, "ROM SUBROUTINES", ref=reference)

assign_function_to_memory_location(0xFBC1, "IP Ar = vtab - 1", ref=reference, name="BASCLCTX")
assign_function_to_memory_location(0xFBC1, "OP $28.29 = base location htab 1", ref=reference, name="BASCLCTX") 
assign_function_to_memory_location(0xFC58,"", ref=reference, name="HOME") 
assign_function_to_memory_location(0xFDF0, "IP Ar = a character", ref=reference, name="CHAROUT") 
assign_function_to_memory_location(0xFDF0, "OP print Ar at ($28)+$36", ref=reference, name="CHAROUT") 
assign_function_to_memory_location(0xFD0C, "OP character in Ar", ref=reference, name="READKEY") 
assign_function_to_memory_location(0xFDE3, "IP Ar = a number 00-0F", ref=reference, name="PRINTHEX") 
assign_function_to_memory_location(0xFDE3, "OP Ar printed as a number, form $A", ref=reference, name="PRINTHEX") 
assign_function_to_memory_location(0xFDDA, "IP Ar = a number", ref=reference, name="PRBYTE") 
assign_function_to_memory_location(0xFDDA, "OP Ar printed as a number, form $AA", ref=reference, name="PRBYTE") 
assign_function_to_memory_location(0xF941, "IP Ar & Xr = a number", ref=reference, name="PRINTAX") 
assign_function_to_memory_location(0xF941, "OP Ar & Xr printed as a number, form $AAXX", ref=reference, name="PRINTAX") 
assign_function_to_memory_location(0xFB2F,"", ref=reference, name="TEXT") 
assign_function_to_memory_location(0xF411, "IP Ar, Xr, Yr = hires location, form YYXX,AA", ref=reference, name="BASCLCHI") 
assign_function_to_memory_location(0xF411, "OP ($26) = base address", ref=reference, name="BASCLCHI") 
assign_function_to_memory_location(0xF3F6, "IP $E6 = page, $1C = hcolor", ref=reference, name="CLRHIRES") 
assign_function_to_memory_location(0xF3F6, "OP hires screen cleared to given color", ref=reference, name="CLRHIRES") 
assign_function_to_memory_location(0xF3F6, "CLRHIRES has been found to ERASE parts of ProDOS if you don't make sure to set the hires page at $E6.", ref=reference, name="CLRHIRES") 
assign_function_to_memory_location(0xF457, "IP $E4 = hcolor, HPOSN called", ref=reference, name="HPLOT") 
assign_function_to_memory_location(0xF457, "OP point plotted", ref=reference, name="HPLOT") 
assign_function_to_memory_location(0xFE93,"", ref=reference, name="PRNMZERO") 
assign_function_to_memory_location(0xFE84, "OP $32: FF", ref=reference, name="NORMAL") 
assign_function_to_memory_location(0xFCA8, "IP Ar = length of pause", ref=reference, name="WAIT") 
assign_function_to_memory_location(0xFCA8, "OP returns after relative pause", ref=reference, name="WAIT") 
assign_function_to_memory_location(0xFCA8,"", ref=reference, name="WAIT") 
assign_function_to_memory_location(0xDEBE, "IP command line = char", ref=reference, name="CHKCOMMA") 
assign_function_to_memory_location(0xDEBE, "OP syntax error if not a comma", ref=reference, name="CHKCOMMA") 
assign_function_to_memory_location(0xF6B9, "IP command line = hires location", ref=reference, name="GETHIRES") 
assign_function_to_memory_location(0xF6B9, "OP location in form YYXX,AA, or ill. quant.", ref=reference, name="GETHIRES") 
assign_function_to_memory_location(0x00B1, "IP command line = char or token", ref=reference, name="GETCHAR") 
assign_function_to_memory_location(0x00B1, "OP char/token in Ar", ref=reference, name="GETCHAR") 
assign_function_to_memory_location(0xE6F8, "IP command line = number", ref=reference, name="GETSMNUM") 
assign_function_to_memory_location(0xE6F8, "OP Xr = number 00-FF", ref=reference, name="GETSMNUM") 
#GETBGNM $DD67 + $E752 IP command line = number
#GETBGNM $DD67 + $E752 OP $50.51 = number 0000-FFFF
assign_function_to_memory_location(0xF6E6,"", ref=reference, name="ILLQUAN") 
assign_function_to_memory_location(0xDEC9,"", ref=reference, name="SNTXERR") 
assign_function_to_memory_location(0xFE95, "IP: number in Areg", ref=reference, name="PRTAREG") 
assign_function_to_memory_location(0xFE95, "OP: number printed", ref=reference, name="PRTAREG") 
assign_function_to_memory_location(0xFB1E, "IP: Xreg = paddle #", ref=reference, name="RDPADDL") 
assign_function_to_memory_location(0xFB1E, "OP: xreg = pdl(x)", ref=reference, name="RDPADDL") 
