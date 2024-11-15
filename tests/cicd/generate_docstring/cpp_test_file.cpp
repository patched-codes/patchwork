#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two values.
 * 
 * @param a The first operand.
 * @param b The second operand.
 * @return The sum of the two operands.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the given SQLite database and returns the results as a 2D vector of strings.
 * Each inner vector represents a row in the result set, with each string being a column value.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query The SQL query to be executed.
 * @return A 2D vector of strings containing the query results. If the query fails, an empty vector is returned.
 */

std::vector<std::vector<std::string>> sqlite(sqlite3* db, const std::string& query) {
    std::vector<std::vector<std::string>> results;
    sqlite3_stmt* stmt;

    if (sqlite3_prepare_v2(db, query.c_str(), -1, &stmt, nullptr) != SQLITE_OK) {
        return results;
    }

    while (sqlite3_step(stmt) == SQLITE_ROW) {
        std::vector<std::string> row;
        for (int i = 0; i < sqlite3_column_count(stmt); i++) {
            const unsigned char* text = sqlite3_column_text(stmt, i);
            if (text) {
                row.push_back(std::string(reinterpret_cast<const char*>(text)));
            } else {
                row.push_back("");
            }
        }
        results.push_back(row);
    }

    sqlite3_finalize(stmt);
    return results;
}


template<typename T, typename F>
/**
 * Compares two items using a key-mapping function and returns an integer 
 * indicating their order. The function applies the provided key mapping 
 * function to both items and compares the resulting keys.
 * 
 * @param key_map A function that takes an item of type T and returns a value 
 *                that can be compared. This key is used for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer that is:
 *         -1 if the key of item1 is less than the key of item2,
 *          1 if the key of item1 is greater than the key of item2,
 *          0 if the keys of both items are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of lowercase and uppercase alphabets.
 * 
 * @param length The desired length of the random string.
 * @return A random string of specified length composed of alphabetic characters.
 */
std::string random_alphabets(int length) {
    static const std::string chars =
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    static std::random_device rd;
    static std::mt19937 generator(rd());
    static std::uniform_int_distribution<> distribution(0, chars.size() - 1);

    std::string result;
    result.reserve(length);

    for (int i = 0; i < length; ++i) {
        result += chars[distribution(generator)];
    }

    return result;
}