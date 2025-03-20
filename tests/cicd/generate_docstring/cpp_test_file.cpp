#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two values.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two values of type T.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on a given SQLite database and retrieves the results.
 * This function prepares and executes a provided SQL query using the SQLite API.
 * Each row of the query result is stored as a vector of strings, which is then added to the results vector.
 * If the query preparation fails, it returns an empty set of results.
 * 
 * @param db The SQLite database connection pointer.
 * @param query The SQL query to execute against the database.
 * @return A 2D vector containing the results of the query, where each inner vector represents a row of the result set.
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
 * Compares two items using a key extraction function and returns an integer indicating their order.
 * 
 * @param key_map A function or functor that extracts a key from the items for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
 */

int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets with the specified length.
 * The string is composed of both lowercase and uppercase English letters.
 * 
 * @param length The length of the desired random alphabet string.
 * @return A string containing random alphabetic characters of specified length.
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