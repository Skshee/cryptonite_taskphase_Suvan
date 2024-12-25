def recover_license():
    target = bytes.fromhex('2b 1d 5e 5a 79 32 5d 05 4b 5c 7d 2c 36 03 5f 50 60 43 24 0f 4e 59 6b 25 3f 13 44 5f')
    
    
    ''' 1. First undo XOR with 0xc39eb4
     For this we need to do it thrice separately For example, if the first few bytes of target are [0x2b, 0x1d, 0x5e]:

    First byte:  0x2b ^ 0xc3
    Second byte: 0x1d ^ 0x9e
    Third byte:  0x5e ^ 0xb4
    '''
    key1 = bytes([0xc3, 0x9e, 0xb4])
    step1 = bytes(target[i] ^ key1[i % 3] for i in range(len(target)))
    
    # 2. Undo swap of indexes 6 and 17
    step2 = bytearray(step1)
    temp = step2[6]
    step2[6] = step2[17]
    step2[17] = temp
    step2 = bytes(step2)
    
    # 3. Undo reverse
    step3 = step2[::-1]
    
    # 4. Undo XOR with 0xe992
    key2 = bytes([0xe9, 0x92])
    step4 = bytes(step3[i] ^ key2[i % 2] for i in range(len(step3)))
    
    # 5. Undo final reverse
    result = step4[::-1]
    print("\nFinal license key bytes:", result.hex())
    print("License key as ASCII:", result.decode('ascii'))

recover_license()