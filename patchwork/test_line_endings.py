from pathlib import Path

def test_line_endings():
    # Create a test file with CRLF endings
    test_content = "line1\r\nline2\r\nline3\r\n"
    test_file = "test.txt"
    
    # Write with CRLF
    with open(test_file, "wb") as f:
        f.write(test_content.encode())
    
    # Read and write using current implementation
    path = Path(test_file)
    text = path.read_text()
    with open(test_file, "w") as file:
        file.write(text)
    
    # Check if endings changed
    with open(test_file, "rb") as f:
        result = f.read().decode()
    
    print("Original had CRLF:", "\r\n" in test_content)
    print("Result has CRLF:", "\r\n" in result)
    print("\nOriginal content (hex):", test_content.encode().hex())
    print("Final content (hex):", result.encode().hex())

test_line_endings()