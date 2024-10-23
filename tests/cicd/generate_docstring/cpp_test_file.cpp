#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of type T together.
 * 
 * @param a The first value to be added
 * @param b The second value to be added
 * @return The sum of a and b
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the given SQLite database and returns the results.
 * 
 * This function prepares and executes the provided SQL query using the SQLite C API.
 * It fetches all rows from the result set and returns them as a vector of string vectors.
 * Each inner vector represents a row, with its elements corresponding to column values.
 * 
 * @param db Pointer to the SQLite database connection
 * @param query The SQL query string to execute
 * @return A vector of vectors containing the query results as strings.
 *         Each inner vector represents a row of the result set.
 *         Returns an empty vector if the query fails to prepare or execute.
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
 * Compares two items based on a key mapping function.
 * 
 * This method applies a key mapping function to two items and compares the results.
 * It determines the relative order of the items based on their mapped values.
 * 
 * @param key_map A function object that maps an item to a comparable value
 * @param item1 The first item to compare
 * @param item2 The second item to compare
 * @return -1 if item1 is less than item2, 1 if item1 is greater than item2, 0 if they are equal
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabetic characters.
 * 
 * This function creates a string of specified length containing random
 * uppercase and lowercase alphabetic characters (A-Z, a-z).
 * It uses a static random number generator for efficiency.
 * 
 * @param length The desired length of the random string
 * @return A string of random alphabetic characters of the specified length
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