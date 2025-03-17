#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two elements of type T together. 
 * This function returns the sum of the two given inputs, a and b.
 * 
 * @param a First element of type T to be added.
 * @param b Second element of type T to be added.
 * @return Sum of a and b, which is also of type T.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a given SQL query on the provided SQLite database connection and returns the result as a vector of string vectors.
 * Each inner vector represents a row from the returned query, with each string representing a column value from the row.
 * 
 * @param db Pointer to the SQLite database connection.
 * @param query The SQL query to be executed on the database.
 * @return A vector of rows, where each row is represented as a vector of strings containing column values.
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
 * Compares two items using a mapping function that extracts the key used 
 * for comparison from each item. 
 * 
 * @param key_map A function or functor that takes an item and returns 
 *                the key used for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return -1 if the key of item1 is less than the key of item2, 
 *          1 if the key of item1 is greater than the key of item2,
 *          0 if the keys are equal.
 */

int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of alphabetic characters (both lowercase and uppercase).
 * 
 * @param length The desired length of the random string.
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