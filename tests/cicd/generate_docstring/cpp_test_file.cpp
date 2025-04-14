#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type.
 * 
 * @param a The first value to add.
 * @param b The second value to add.
 * @return The sum of the two values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a given SQL query on the provided SQLite database and retrieves the results.
 * 
 * The function prepares and executes the SQL query using the provided database connection.
 * It processes each row of the result, storing column data as strings in a vector of strings, and
 * collects these rows into a vector of vector of strings which represents the entire result set.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query The SQL query to be executed as a string.
 * @return A vector of vector of strings, where each inner vector represents a row of the query result.
 *         Returns an empty result if the query preparation failed or if no rows are returned.
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
 * Compares two items using a key mapping function and returns an integer based 
 * on their values. This function leverages a key mapping function to extract 
 * comparable values from the provided items, enabling a generic comparison 
 * mechanism.
 * 
 * @param key_map A function or callable object that extracts a comparable value 
 *                from an item of type T. This function must take a single 
 *                argument of type T and return a value that can be compared 
 *                using the relational operators.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer: returns -1 if the value of item1 is less than the value 
 *         of item2; returns 1 if the value of item1 is greater than the value 
 *         of item2; returns 0 if both values are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of alphabetic characters.
 * The string includes both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string of specified length containing alphabetic characters.
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