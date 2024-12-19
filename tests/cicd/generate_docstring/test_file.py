// File: js_test_file.py.js

const assert = require('assert');

function testAPlusB() {
  assert.strictEqual(a_plus_b(1, 2), 3);
  assert.strictEqual(a_plus_b(-1, -1), -2);
  assert.strictEqual(a_plus_b(0, 0), 0);
}

function testCompare() {
  const keymap = 'value';
  const obj1 = { value: 1 };
  const obj2 = { value: 2 };
  const obj3 = { value: 1 };
  
  assert.strictEqual(compare(keymap, obj1, obj2), -1);
  assert.strictEqual(compare(keymap, obj2, obj1), 1);
  assert.strictEqual(compare(keymap, obj1, obj3), 0);
}

testAPlusB();
testCompare();
