def read_and_write_file(filepath):
    # Read the file and print original line endings
    with open(filepath, 'rb') as f:
        content = f.read()
        print(f"Original line endings (hex):", content.hex())
    
    # Read using current implementation approach
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Write back using current implementation approach
    with open(filepath + '.modified', 'w') as f:
        f.write(content)
    
    # Read the modified file and print new line endings
    with open(filepath + '.modified', 'rb') as f:
        modified = f.read()
        print(f"Modified line endings (hex):", modified.hex())

if __name__ == "__main__":
    read_and_write_file('test_lineendings.py')