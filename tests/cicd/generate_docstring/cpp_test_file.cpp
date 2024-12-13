#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two variables.
 * 
 * @param a The first variable to add.
 * @param b The second variable to add.
 * @return The sum of the two variables.
 */

T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on a SQLite database and returns the results.
 *
 * This function prepares an SQL statement to be executed against the provided
 * SQLite database object. It iterates through the resulting rows of the query,
 * storing each column's text in a nested vector of strings, where each inner
 * vector represents a single row.
 *
 * @param db A pointer to the SQLite database (sqlite3*) on which the query should be executed.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors, with each inner vector containing strings representing the data from each row of the SQL query result. If the query fails to execute, an empty outer vector is returned.
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
 * indicating their order. The function extracts key values from the items 
 * using the provided key_map and then compares these key values.
 * 
 * @param key_map A function that takes an item of type T and returns a key 
 * value for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer where -1 indicates that item1 is less than item2, 1 
 * indicates that item1 is greater than item2, and 0 indicates that item1 
 * is equal to item2 based on the key values.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of alphabetical characters.
 * 
 * This function creates a string of a specified length filled with
 * random lowercase and uppercase alphabetical characters.
 * 
 * @param length The desired length of the random string.
 * @return A string of random alphabetic characters of the specified length.
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