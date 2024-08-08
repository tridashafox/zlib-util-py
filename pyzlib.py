import zlib
import sys
import os

def get_root_name(filename):
    # Extract root name (everything before the first dot)
    base_name = os.path.basename(filename)
    root_name = base_name.split('.')[0]
    return root_name

import sys

def hex_dump(filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
        
        datalen = len(data)
        for i in range(0, datalen, 16):
            chunk = data[i:i+8]
            hex_values1 = ' '.join(f'{byte:02X}' for byte in chunk)
            ascii_values1 = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in chunk)
            chunk = data[i+8:i+16]
            hex_values2 = ' '.join(f'{byte:02X}' for byte in chunk)
            ascii_values2 = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in chunk)
            print(f'{i:04X}: {hex_values1:<24} {hex_values2:<24} {ascii_values1}{ascii_values2}')
        
        print(f'file size: 0x{datalen:X} ({datalen})')
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def compress_file(input_filename):
    # Extract root name before the first dot
    root_name = get_root_name(input_filename)

    # Open and read the input file
    with open(input_filename, 'rb') as file:
        data = file.read()

    # Initialize the compressor object
    compressor = zlib.compressobj(
        level=zlib.Z_BEST_COMPRESSION,  # Equivalent to zcLevel9 in Delphidi
        method=zlib.DEFLATED,
        wbits=15,  # 15 is the default for zlib format
        memLevel=8,  # Default memory level
        strategy=zlib.Z_DEFAULT_STRATEGY
        #strategy=zlib.Z_FILTERED
        #strategy=zlib.Z_HUFFMAN_ONLY, 
        #strategy=zlib.Z_RLE
    )

    # Compress the data
    compressed_data = compressor.compress(data) + compressor.flush()

    # Determine the size of the compressed data
    compressed_size = len(compressed_data)

    # Format the size in hexadecimal
    size_hex = f"{compressed_size:08X}"  # 8 digits with leading zeros

    # Create the output filename with the size in hexadecimal
    output_filename = f"{root_name}-com.{size_hex}.bin"

    # Write compressed data to the output file
    with open(output_filename, 'wb') as file:
        file.write(compressed_data)

    print(f"Successfully compressed '{input_filename}' to '{output_filename}'")
    print(f"Original size: {len(data)} bytes")
    print(f"Compressed size: {compressed_size} bytes")

def copy_file(input_filename):
    # Extract root name before the first dot
    root_name = get_root_name(input_filename)

    # Open and read the input file
    with open(input_filename, 'rb') as file:
        data = file.read()

    # Determine the size of the compressed data
    data_size = len(data)

    # Format the size in hexadecimal
    size_hex = f"{data_size :08X}"  # 8 digits with leading zeros

    # Create the output filename with the size in hexadecimal
    output_filename = f"{root_name}.{size_hex}.bin"

    # Write  data to the output file
    with open(output_filename, 'wb') as file:
        file.write(data)

    print(f"Successfully copied '{input_filename}' to '{output_filename}'")
    print(f"Size: {data_size} bytes")

def decompress_file(input_filename):
    # Extract root name before the first dot
    root_name = get_root_name(input_filename)

    # Open and read the compressed file
    with open(input_filename, 'rb') as file:
        compressed_data = file.read()

    # Initialize the decompressor object
    decompressor = zlib.decompressobj()

    # Decompress the data
    decompressed_data = decompressor.decompress(compressed_data) + decompressor.flush()

    # Determine the size of the decompressed data
    decompressed_size = len(decompressed_data)

    # Format the size in hexadecimal
    size_hex = f"{decompressed_size:08X}"  # 8 digits with leading zeros

    # Create the output filename with the size in hexadecimal
    output_filename = f"{root_name}-decom.{size_hex}.bin"

    # Write decompressed data to the output file
    with open(output_filename, 'wb') as file:
        file.write(decompressed_data)

    print(f"Successfully decompressed '{input_filename}' to '{output_filename}'")
    print(f"Compressed size: {len(compressed_data)} bytes")
    print(f"Decompressed size: {decompressed_size} bytes")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <com|decom|copy|hex> <filename>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    input_filename = sys.argv[2]

    if operation == 'com':
        compress_file(input_filename)
    elif operation == 'decom':
        decompress_file(input_filename)
    elif operation == 'copy':
        copy_file(input_filename)
    elif operation == 'hex':
        hex_dump(input_filename)
    else:
        print("Invalid operation. Use 'com' for compress or 'decom' for decompress, or copy to copy, or hex to hex dump first 64 bytes")
        sys.exit(1)
