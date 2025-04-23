with open("sample.bin", "rb") as f:
    byte_content = f.read(1)
    while byte_content:
        # Printing the contents of the file
        print(byte_content)