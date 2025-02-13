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
 * @return The result of adding the two input values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on a SQLite database and retrieves the results.
 * 
 * This function prepares a SQL statement from the given query, executes it on the provided
 * SQLite database, and retrieves the resulting data into a two-dimensional vector of strings,
 * where each inner vector represents a row of the query result.
 * 
 * @param db A pointer to the SQLite database connection object.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors of strings representing the rows and columns
 *         of the result set of the query. Each inner vector represents a row. 
 *         If the query execution fails, an empty vector is returned.
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
 * Compares two items using a specified key mapping function and returns an integer indicating
 * their relative order. The comparison is based on the values obtained by applying the key_map 
 * function to each item. 
 * 
 * @param key_map A function or functor that maps an item to a key value to be compared.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer: -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if 
 *         they are equal based on the key values.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of alphabetic characters.
 *
 * This function creates a random string of the specified length
 * using both lowercase and uppercase English alphabetic characters.
 * 
 * @param length The length of the random string to be generated.
 * @return A string containing random alphabetic characters of the specified length.
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