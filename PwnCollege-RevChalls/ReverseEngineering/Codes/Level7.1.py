def hex_to_bytes(hex_str):
    # Remove spaces and convert to bytes
    hex_str = hex_str.replace(" ", "")
    return bytes.fromhex(hex_str)

def reverse_operations(target):
    # Start with our target bytes
    current = bytearray(target)
    
    # 1. First XOR everything with 0xFA (this is its own inverse)
    for i in range(len(current)):
        current[i] ^= 0xFA
        
    # 2. Swap positions 7 and 17 back
    current[7], current[17] = current[17], current[7]
    
    # 3. Reverse the XOR operations
    for i in range(len(current)):
        if i % 2 == 0:  # even positions
            current[i] ^= 0x16
        else:  # odd positions
            current[i] ^= 0xBF
    
    # 4. Reverse first 13 pairs
    temp = current[:26]  # Get the pairs to reverse
    temp.reverse()
    current[:26] = temp
    
    return current

# Target string from objdump output
target_hex = "963f963f963f9522953d9a3399369f369d35832b862c843c89278d00"
target = hex_to_bytes(target_hex)

result = reverse_operations(target)
print("Result after reverse operations:")
print(result.hex())
print("\nAs ASCII (if printable):")
print(''.join(chr(b) if 32 <= b <= 126 else '.' for b in result))