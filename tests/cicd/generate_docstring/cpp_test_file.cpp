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
 * Executes a SQL query using the provided SQLite database connection and returns the results.
 * 
 * @param db A pointer to the SQLite database connection object.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors, where each inner vector contains the values of a single row from the query result,
 *         represented as strings. If the query preparation fails, an empty vector is returned.
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
 * Compares two items based on their mapped values using a key mapping function.
 * 
 * This function applies a provided key mapping function to two items and compares
 * their mapped values. It returns -1, 0, or 1 depending on whether the mapped value
 * of the first item is less than, equal to, or greater than the mapped value of the second item.
 * 
 * @param key_map A function that returns the key value for comparison from an item.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the comparison result: 
 *         -1 if the mapped value of item1 is less than that of item2,
 *          0 if they are equal,
 *          1 if the mapped value of item1 is greater than that of item2.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of uppercase and lowercase alphabets with a specified length.
 * 
 * @param length The length of the random string to generate.
 * @return A random string of the specified length composed of uppercase and lowercase alphabets.
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