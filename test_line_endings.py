import os

def create_test_files():
    # Create a file with CRLF endings
    with open('test_crlf.txt', 'wb') as f:
        f.write(b'line1\r\nline2\r\nline3\r\n')
    
    # Read and write using current implementation
    from patchwork.common.utils.utils import open_with_chardet
    
    # Read the file
    with open_with_chardet('test_crlf.txt', 'r') as f:
        content = f.read()
    
    # Write back to a new file
    with open('test_output.txt', 'w') as f:
        f.write(content)
    
    # Compare the files
    with open('test_crlf.txt', 'rb') as f1, open('test_output.txt', 'rb') as f2:
        original = f1.read()
        modified = f2.read()
        
    print(f"Original file bytes: {original}")
    print(f"Modified file bytes: {modified}")
    print(f"Files are identical: {original == modified}")

create_test_files()