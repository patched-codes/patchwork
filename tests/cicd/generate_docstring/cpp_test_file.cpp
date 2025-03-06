#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of type T and returns the result.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of a and b.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on a SQLite database and retrieves the results as a vector of string vectors.
 * Each element of the outer vector represents a row, and each inner vector contains the string
 * values of the columns in that row.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query The SQL query string to execute.
 * @return A vector of vectors containing the query results. Each inner vector corresponds to a row
 * of the result set, with each string element representing a column value in that row.
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
 * Compares two items using a key mapping function.
 * 
 * This function applies a given key mapping function to two items
 * and compares the resulting values. It returns -1 if the first 
 * item's key is less than the second item's key, 1 if the first 
 * item's key is greater, and 0 if they are equal.
 * 
 * @param key_map A function or callable that extracts a key from an item for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the comparison result: 
 *         -1 if item1 < item2, 1 if item1 > item2, and 0 if item1 == item2.
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
 * The string includes both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to generate. Must be a non-negative integer.
 * @return A random string of alphabets with the specified length.
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