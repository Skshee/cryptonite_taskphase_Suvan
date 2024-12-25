def solve_babyrev6():
    target = bytes.fromhex('dad9d9d6cbd4c0decbcbd9d3ddd3dac2')
    
    # XORing with 0xd0
    xor1 = bytes(b ^ 0xd0 for b in target)
    print("After undoing XOR with 0xd0:", xor1.hex())
    
    # Reversing
    reverse = xor1[::-1]
    print("After undoing reverse:", reverse.hex())
    
    # XORing with 0x61
    xor2 = bytes(b ^ 0x61 for b in reverse)
    
    print("\nSolution in hex:", xor2.hex())
    print("Solution as string:", xor2.decode('ascii', errors='replace'))
solve_babyrev6()