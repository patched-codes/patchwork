import tempfile
import os

def test_line_endings():
    # Create a test file with CRLF line endings
    content = "line1\r\nline2\r\nline3\r\n"
    
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as f:
        f.write(content.encode('utf-8'))
        temp_path = f.name

    # Now try to modify it using our ModifyCode functions
    from steps.ModifyCode.ModifyCode import replace_code_in_file
    
    # Try to replace the second line
    replace_code_in_file(temp_path, 1, 2, "new line2\r\n")
    
    # Read the result
    with open(temp_path, 'rb') as f:
        result = f.read().decode('utf-8')
    
    print("Original line endings preserved?" + str("\r\n" in result))
    print("Result content (in hex):")
    print(''.join(hex(ord(c))[2:].zfill(2) for c in result))
    
    os.unlink(temp_path)

if __name__ == "__main__":
    test_line_endings()