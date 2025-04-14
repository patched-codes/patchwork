#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type and returns the result.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two input values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the given SQLite database connection and retrieves the results.
 * Each row of the result is stored as a vector of strings, and the collection of all rows is 
 * returned as a vector of vectors of strings.
 * 
 * @param db Pointer to the SQLite database connection.
 * @param query The SQL query string to be executed on the database.
 * @return A vector of vector of strings, where each inner vector represents a row of the query 
 *         result, with each element being a column value in string format. Returns an empty 
 *         vector if the query fails to prepare or execute properly.
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
 * Compares two items based on their mapped values.
 * 
 * This function takes a key mapping function and two items of the same type. It applies the 
 * key mapping function to each item to obtain comparable values, and returns an integer to 
 * indicate their comparative order. If the first item's mapped value is less than the second's, 
 * it returns -1. If greater, it returns 1. If both values are equal, it returns 0.
 * 
 * @param key_map A function that takes an item of type T and returns a value of a type 
 *                that supports comparison (e.g., int, float, etc.).
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if the mapped value of item1 is less than that of item2, 
 *         1 if greater, and 0 if they are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of alphabets (both uppercase and lowercase).
 *
 * @param length The desired length of the generated string.
 * @return A randomly generated string of the specified length consisting of alphabet characters.
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