import tempfile
import os

def test_with_endings(line_ending, description):
    print(f"\n=== Test with {description} ===")
    
    # Create test content with specified line endings
    content = f'line1{line_ending}line2{line_ending}line3{line_ending}'
    print(f"Content to write (repr): {repr(content)}")
    
    # Create different content to replace with, using LF endings
    # This simulates real usage where new code comes with normalized \n endings
    replace_content = 'newline1\nnewline2\nnewline3\n'
    
    with tempfile.NamedTemporaryFile(delete=False) as f:
        test_file = f.name
    
    # Write initial content in binary mode
    with open(test_file, 'wb') as f:
        f.write(content.encode('utf-8'))
    
    # Read and verify original content
    with open(test_file, 'rb') as f:
        original = f.read()
        print(f"\nOriginal file bytes (repr): {repr(original)}")
    
    # Test save_file_contents with original content
    from patchwork.steps.ModifyCode.ModifyCode import save_file_contents, replace_code_in_file
    print("\nTesting save_file_contents...")
    save_file_contents(test_file, content)
    
    with open(test_file, 'rb') as f:
        modified = f.read()
        print(f"Modified file bytes (repr): {repr(modified)}")
    
    # Verify save_file_contents preserved endings
    if original != modified:
        print("\nFAILURE: save_file_contents modified line endings!")
        print(f"Original length: {len(original)}, Modified length: {len(modified)}")
        return False
        
    # Test replace_code_in_file with different content
    print("\nTesting replace_code_in_file...")
    replace_code_in_file(test_file, 0, 3, replace_content)
    
    with open(test_file, 'rb') as f:
        modified2 = f.read()
        print(f"Modified file bytes after replace (repr): {repr(modified2)}")
    
    # Cleanup
    os.unlink(test_file)
    
    # For replace_code_in_file, verify:
    # 1. The content was actually changed (should NOT equal original)
    # 2. The new content uses the original line endings
    # 3. The file ends with a line ending only if original did
    content_changed = original != modified2
    uses_right_endings = line_ending.encode('utf-8') in modified2
    ends_correctly = original.endswith(line_ending.encode('utf-8')) == modified2.endswith(line_ending.encode('utf-8'))
    
    success = content_changed and uses_right_endings and ends_correctly
    print(f"\n{'SUCCESS' if success else 'FAILURE'}: {'All checks passed!' if success else 'Checks failed:'}")
    if not success:
        print(f"Content changed: {content_changed}")
        print(f"Uses right endings: {uses_right_endings}")
        print(f"Ends correctly: {ends_correctly}")
        print(f"Original length: {len(original)}, Replace length: {len(modified2)}")
    return success

def test_complex_case():
    print("\n=== Test with complex indentation and empty lines ===")
    # Create content with mixed indentation and empty lines, using CRLF endings
    content = '    line1\r\n\r\n        line2\r\n    line3\r\n'
    replace_content = 'newline1\n\n    newline2\n'  # Note: less indented
    
    with tempfile.NamedTemporaryFile(delete=False) as f:
        test_file = f.name
    
    # Write initial content
    with open(test_file, 'wb') as f:
        f.write(content.encode('utf-8'))
    
    # Read original content
    with open(test_file, 'rb') as f:
        original = f.read()
    print(f"Original file bytes (repr): {repr(original)}")
    
    # Test replace_code_in_file
    from patchwork.steps.ModifyCode.ModifyCode import replace_code_in_file
    replace_code_in_file(test_file, 0, 4, replace_content)
    
    with open(test_file, 'rb') as f:
        modified = f.read()
    print(f"Modified file bytes (repr): {repr(modified)}")
    
    # Cleanup
    os.unlink(test_file)
    
    # Verify:
    # 1. Content was changed
    # 2. Uses original CRLF endings
    # 3. Empty lines were handled correctly
    # 4. Indentation was adjusted correctly
    content_changed = original != modified
    uses_crlf = b'\r\n' in modified
    has_empty_line = b'\r\n\r\n' in modified
    proper_indent = b'    newline' in modified
    
    success = content_changed and uses_crlf and has_empty_line and proper_indent
    print(f"\n{'SUCCESS' if success else 'FAILURE'}: Complex case {'passed!' if success else 'failed!'}")
    if not success:
        print(f"Content changed: {content_changed}")
        print(f"Uses CRLF: {uses_crlf}")
        print(f"Has empty line: {has_empty_line}")
        print(f"Proper indent: {proper_indent}")
    return success

def test_partial_replacement():
    print("\n=== Test partial file replacement ===")
    # Create content with CRLF endings and indentation
    content = 'header1\r\nheader2\r\n    line1\r\n    line2\r\n    line3\r\nfooter\r\n'
    replace_content = 'newline1\nnewline2\n'  # Replace middle part only
    
    with tempfile.NamedTemporaryFile(delete=False) as f:
        test_file = f.name
    
    # Write initial content
    with open(test_file, 'wb') as f:
        f.write(content.encode('utf-8'))
    
    # Read original content
    with open(test_file, 'rb') as f:
        original = f.read()
    print(f"Original file bytes (repr): {repr(original)}")
    
    # Test replace_code_in_file on middle section (lines 2-4)
    from patchwork.steps.ModifyCode.ModifyCode import replace_code_in_file
    replace_code_in_file(test_file, 2, 5, replace_content)
    
    with open(test_file, 'rb') as f:
        modified = f.read()
    print(f"Modified file bytes (repr): {repr(modified)}")
    
    # Cleanup
    os.unlink(test_file)
    
    # Verify:
    # 1. Header is unchanged
    # 2. Footer is unchanged
    # 3. Middle section is replaced with new content
    # 4. All line endings are CRLF
    # 5. Indentation is preserved
    
    # Split content for easier verification
    lines = modified.split(b'\r\n')
    
    # Check each aspect
    header_preserved = lines[:2] == [b'header1', b'header2']
    footer_preserved = lines[-2] == b'footer'  # -2 because -1 is empty string after last \r\n
    has_new_content = lines[2:4] == [b'    newline1', b'    newline2']
    all_crlf = b'\n' not in modified.replace(b'\r\n', b'') and b'\r\n' in modified
    proper_indent = all(line.startswith(b'    ') for line in lines[2:4])
    
    success = header_preserved and footer_preserved and has_new_content and all_crlf and proper_indent
    print(f"\n{'SUCCESS' if success else 'FAILURE'}: Partial replacement {'passed!' if success else 'failed!'}")
    if not success:
        print(f"Header preserved: {header_preserved}")
        print(f"Footer preserved: {footer_preserved}")
        print(f"Has new content: {has_new_content}")
        print(f"All CRLF endings: {all_crlf}")
        print(f"Proper indent: {proper_indent}")
    return success

def test_line_endings():
    results = []
    
    # Test with different line endings
    results.append(test_with_endings('\r\r\n', 'double-CR line endings (\\r\\r\\n)'))
    results.append(test_with_endings('\r\n', 'CRLF line endings (\\r\\n)'))
    results.append(test_with_endings('\n', 'LF line endings (\\n)'))
    results.append(test_with_endings('\r', 'CR line endings (\\r)'))
    
    # Test complex case with indentation and empty lines
    results.append(test_complex_case())
    
    # Test partial file replacement
    results.append(test_partial_replacement())
    
    # Overall result
    print("\n=== Overall Test Results ===")
    if all(results):
        print("SUCCESS: All line ending tests passed!")
        return True
    else:
        print("FAILURE: Some line ending tests failed!")
        return False

if __name__ == '__main__':
    test_line_endings()

if __name__ == '__main__':
    test_line_endings()