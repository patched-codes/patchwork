#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two elements of the same type and returns the result.
 * This function can work with any type that supports the addition operator.
 * 
 * @param a The first element to add.
 * @param b The second element to add.
 * @return The sum of the two elements.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the given SQLite database and returns the results.
 *
 * This function prepares a SQL statement, executes it on the provided SQLite
 * database, and retrieves the results as a vector of rows, where each row is
 * a vector of strings representing the column values.
 *
 * @param db A pointer to the SQLite database connection.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors of strings, where each inner vector represents
 *         a row of the query result set. Each string in the row vector is the
 *         textual representation of a column value. If the query preparation
 *         fails, an empty vector is returned.
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
 * Compares two items based on a specific key value derived from a mapping function.
 * 
 * This function utilizes a key mapping function to extract comparable values
 * from the two given items. It then compares these values to determine the 
 * relative ordering of the items.
 * 
 * @param key_map A function that extracts the key value from an item. 
 *                It takes an item of type T as an input and returns a 
 *                comparable value.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the comparison result: 
 *         -1 if item1 should come before item2, 
 *          1 if item1 should come after item2, 
 *          0 if they are considered equal.
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
 * @param length The length of the random string to be generated.
 * @return A random string of specified length, composed of characters from 'a-z' and 'A-Z'.
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