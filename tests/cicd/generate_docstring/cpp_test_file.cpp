#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two values of the same type.
 * 
 * @param a The first operand in the sum.
 * @param b The second operand in the sum.
 * @return The result of adding the two operands, of the same type as the input parameters.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on a given SQLite database and retrieves the results as a vector of string vectors.
 * Each inner vector represents a row in the result set, with each string representing a column value.
 *
 * @param db A pointer to the SQLite database connection object.
 * @param query A constant reference to the SQL query string to be executed.
 * @return A vector of vectors of strings where each inner vector represents a row from the result set.
 *         Returns an empty vector if the SQL query preparation fails or there are no results.
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
 * Compares two items using a key mapping function and returns an integer
 * indicating whether the first item is less than, equal to, or greater 
 * than the second item based on the value returned by the key_map function.
 * 
 * @param key_map A function that accepts an item of type T and returns 
 *                a value that is used for comparing items.
 * @param item1 The first item of type T to compare.
 * @param item2 The second item of type T to compare.
 * @return An integer: -1 if item1 is less than item2, 1 if item1 is 
 *         greater than item2, and 0 if they are equal based on the key_map value.
 */

int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of alphabetic characters (both uppercase and lowercase).
 * 
 * @param length The length of the random string to be generated.
 * @return A random string of the specified length composed of alphabetic characters.
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