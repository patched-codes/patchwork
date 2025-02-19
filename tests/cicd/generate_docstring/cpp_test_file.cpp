#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type together.
 * 
 * @param a The first value of type T.
 * @param b The second value of type T.
 * @return The sum of the two values of type T.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the given SQLite database and returns the results as a vector of string vectors. Each inner vector represents a row and contains the row's column values as strings.
 * 
 * @param db The SQLite database connection object.
 * @param query The SQL query string to be executed.
 * @return A vector of string vectors, where each vector represents a row from the query result, and each element in the vector is a string representation of a column value. If the query execution fails, an empty vector is returned.
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
 * Compares two items based on their mapped values through a key mapping function.
 * 
 * This function utilizes a provided key mapping function to obtain comparable 
 * values from two items and determines their order. It returns -1 if the first 
 * item should precede the second, 1 if it should follow, or 0 if they are equal.
 *
 * @param key_map A function or callable object that extracts a comparable value 
 *                from an item of type T.
 * @param item1   The first item of type T to compare.
 * @param item2   The second item of type T to compare.
 * @return        An integer indicating the order: -1 if item1 < item2, 
 *                1 if item1 > item2, and 0 if item1 == item2.
 */

int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of specified length using alphabetic characters.
 * The generated string contains only upper and lowercase alphabetic characters.
 * 
 * @param length The desired length of the random string.
 * @return A random string consisting of alphabetic characters with the specified length.
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