from steps.ModifyCode.ModifyCode import replace_code_in_file
import os
import binascii

def hex_dump(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    hex_content = binascii.hexlify(content).decode()
    print(f"\nHex dump of {file_path}:")
    print(hex_content)
    
    # Add visual markers for line endings
    content_str = content.decode('latin1')
    print("\nLine endings analysis:")
    for i, line in enumerate(content_str.splitlines(True)):
        ending = ""
        if line.endswith('\r\n'):
            ending = "CRLF (\\r\\n)"
        elif line.endswith('\n'):
            ending = "LF (\\n)"
        elif line.endswith('\r'):
            ending = "CR (\\r)"
        else:
            ending = "NO ENDING"
        print(f"Line {i+1}: {ending}")
    print()

# Test cases
test_cases = [
    {
        'name': 'test_no_endings.txt',
        'content': 'line1line2line3',  # No line endings at all
        'replace_line': 0,
        'new_content': 'new\nline\nhere\n'
    },
    {
        'name': 'test_crlf.txt',
        'content': 'line1\r\nline2\r\nline3\r\n',
        'replace_line': 1,
        'new_content': 'new line\nwith unix ending\n'
    },
    {
        'name': 'test_lf.txt',
        'content': 'line1\nline2\nline3\n',
        'replace_line': 1,
        'new_content': 'new line\r\nwith crlf ending\r\n'
    },
    {
        'name': 'test_mixed.txt',
        'content': 'line1\r\nline2\nline3\r\nline4\n',
        'replace_line': 1,
        'new_content': 'new line\nwith unix ending\n'
    }
]

for test in test_cases:
    print(f"=== Testing {test['name']} ===")
    
    # Create test file
    with open(test['name'], 'wb') as f:
        f.write(test['content'].encode())
    
    print("Original file:")
    hex_dump(test['name'])
    
    # Test replacing content
    print(f"Replacing line {test['replace_line']+1} with new content...")
    replace_code_in_file(test['name'], test['replace_line'], test['replace_line']+1, test['new_content'])
    
    print("After replacement:")
    hex_dump(test['name'])