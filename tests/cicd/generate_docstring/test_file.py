// File: tests/cicd/generate_docstring/js_test_file.py.js
const assert = require('assert');

function test_a_plus_b() {
    assert.strictEqual(a_plus_b(2, 3), 5);
    assert.strictEqual(a_plus_b(-1, 1), 0);
    assert.strictEqual(a_plus_b(0, 0), 0);
}

function test_compare() {
    const obj1 = {key: 1};
    const obj2 = {key: 2};
    const keymap = 'key';

    assert.strictEqual(compare(keymap, obj1, obj2), -1);
    assert.strictEqual(compare(keymap, obj2, obj1), 1);
    assert.strictEqual(compare(keymap, obj1, {key: 1}), 0);
}

test_a_plus_b();
test_compare();
