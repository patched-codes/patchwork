from patchwork.common.utils.utils import open_with_chardet

def test_empty_file():
    # Test empty file
    with open('test_empty.txt', 'wb') as f:
        f.write(b'')
    
    with open_with_chardet('test_empty.txt', 'r') as f:
        content = f.read()
    
    with open('test_empty_out.txt', 'w') as f:
        f.write(content)
        
    with open('test_empty.txt', 'rb') as f1, open('test_empty_out.txt', 'rb') as f2:
        assert f1.read() == f2.read(), "Empty file test failed"
    print("Empty file test passed")

def test_mixed_endings():
    # Test file with mixed line endings
    with open('test_mixed.txt', 'wb') as f:
        f.write(b'line1\n')  # LF
        f.write(b'line2\r\n')  # CRLF
        f.write(b'line3\n')  # LF
        
    with open_with_chardet('test_mixed.txt', 'r') as f:
        content = f.read()
    
    with open('test_mixed_out.txt', 'w') as f:
        f.write(content)
        
    with open('test_mixed.txt', 'rb') as f1, open('test_mixed_out.txt', 'rb') as f2:
        orig = f1.read()
        mod = f2.read()
        assert orig == mod, f"Mixed endings test failed:\nOriginal: {orig}\nModified: {mod}"
    print("Mixed endings test passed")

def test_no_final_newline():
    # Test file without final newline
    with open('test_no_final.txt', 'wb') as f:
        f.write(b'line1\r\nline2\r\nline3')  # No final newline
        
    with open_with_chardet('test_no_final.txt', 'r') as f:
        content = f.read()
    
    with open('test_no_final_out.txt', 'w') as f:
        f.write(content)
        
    with open('test_no_final.txt', 'rb') as f1, open('test_no_final_out.txt', 'rb') as f2:
        orig = f1.read()
        mod = f2.read()
        assert orig == mod, f"No final newline test failed:\nOriginal: {orig}\nModified: {mod}"
    print("No final newline test passed")

if __name__ == '__main__':
    test_empty_file()
    test_mixed_endings()
    test_no_final_newline()
    print("All edge case tests passed!")