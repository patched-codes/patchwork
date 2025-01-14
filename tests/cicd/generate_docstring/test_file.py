const assert = require('assert');
const sinon = require('sinon');

describe('a_plus_b', function() {
    it('should return the sum of two numbers', function() {
        assert.strictEqual(a_plus_b(1, 2), 3);
        assert.strictEqual(a_plus_b(-1, 1), 0);
    });
});

describe('compare', function() {
    const keymap = 'value';
    
    it('should return -1 if first object is less than second', function() {
        const a = {value: 1};
        const b = {value: 2};
        assert.strictEqual(compare(keymap, a, b), -1);
    });

    it('should return 1 if first object is greater than second', function() {
        const a = {value: 2};
        const b = {value: 1};
        assert.strictEqual(compare(keymap, a, b), 1);
    });

    it('should return 0 if both objects are equal', function() {
        const a = {value: 2};
        const b = {value: 2};
        assert.strictEqual(compare(keymap, a, b), 0);
    });
});

describe('sqlite', function() {
    it('should execute a query on db and call callback for each row', function(done) {
        const db = { serialize: sinon.stub(), each: sinon.stub() };
        const query = 'SELECT * FROM table';
        const callback = sinon.spy();
        
        db.each.yields();
        sqlite(db, query, callback);

        assert(db.serialize.calledOnce);
        assert(db.each.calledWith(query, callback));
        assert(callback.calledOnce);
        done();
    });
});
