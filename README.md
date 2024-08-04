Simple python code which can decompress, compress, copy or hex dump information for a zlib data.
When it performs an operation it uses the root of the input file name for the output file name while adding on the operation perfromed and resulting size in hex with a .bin extension.
Set to use zlib BEST_COMPRESSION, zlib.DEFLATED, wbits=15, memLevel=8, DEFAULT_STRATEGY.

Examples using a zlib compressed block of data in the file fcompressed.bin:
```
F:\pyzlibtool>python pyzlib.py
Usage: python script.py <com|decom|copy|hex> <filename>

F:\pyzlibtool>python pyzlib.py hex fcompressed.bin
0000: 78 da b5 5d 7d 8c e4 c8 55 f7 de 6d c8 ed e6 fb  x..]}...U..m....
0010: 12 72 c7 47 a2 65 0f c1 ad c8 ce d8 55 6d 77 f7  .r.G.e......Umw.
0020: 4e c8 5d 77 4f cf cd e4 e6 2b d3 b3 b7 b9 b0 e0  N.]wO....+......
0030: 78 ba dd 33 ce 74 b7 1b db bd 73 b3 49 a4 28 77  x..3.t....s.I.(w

F:\pyzlibtool>python pyzlib.py decom fcompressed.bin
Successfully decompressed 'fcompressed.bin' to 'fcompressed-decom.00009B58.bin'
Compressed size: 7473 bytes
Decompressed size: 39768 bytes

F:\pyzlibtool>python pyzlib.py com fcompressed-decom.00009B58.bin
Successfully compressed 'fcompressed-decom.00009B58.bin' to 'fcompressed-decom-com.00001C44.bin'
Original size: 39768 bytes
Compressed size: 7236 bytes

F:\pyzlibtool>python pyzlib.py copy fcompressed.bin
Successfully copied 'fcompressed.bin' to 'fcompressed.00001D31.bin'
Size: 7473 bytes
```

