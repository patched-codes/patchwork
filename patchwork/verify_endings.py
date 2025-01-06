from steps.ModifyCode.ModifyCode import replace_code_in_file
import os
import binascii

def hex_dump(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    hex_content = binascii.hexlify(content).decode()
    print(f"Hex dump of {file_path}:")
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

# Test file paths
test_file = "test_crlf.txt"

print("Original file:")
hex_dump(test_file)

# Test replacing content
print("Replacing line 2 with new content...")
replace_code_in_file(test_file, 1, 2, "new line\nwith unix ending")

print("After replacement:")
hex_dump(test_file)