#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the given SQLite database and returns the results.
 * This function prepares the SQL statement, executes it, and retrieves the rows from the result set.
 * Each row is represented as a vector of strings, and all rows are stored in a vector of vectors.
 *
 * @param db A pointer to the SQLite database connection object.
 * @param query A string representing the SQL query to be executed.
 * @return A vector of vectors of strings containing the query results. 
 *         Each inner vector represents a row, where each string is a column value.
 *         An empty vector will be returned if the query fails or if there are no results.
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
 * Compares two items based on the transformation provided by a key mapping function.
 *
 * The function applies a key_map function to both items and compares them. 
 * It returns -1 if the first transformed value is less than the second, 
 * 1 if it is greater, and 0 if they are equal.
 * 
 * @param key_map A callable that takes an item of type T and returns a comparable value.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer, where -1 indicates item1 is less than item2, 1 indicates item1 is greater than item2, 
 *         and 0 indicates they are equal when compared using the key_map function.
 */

int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets of a specified length.
 * The string includes both lowercase and uppercase characters.
 * 
 * @param length The length of the random string to generate.
 * @return A string containing random alphabetic characters with the specified length.
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