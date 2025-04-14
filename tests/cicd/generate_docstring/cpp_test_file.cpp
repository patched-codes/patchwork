#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Calculates the sum of two values.
 * 
 * @param a First value to be added.
 * @param b Second value to be added.
 * @return The sum of the first and second values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on a SQLite database and retrieves the result set.
 * 
 * This function prepares and executes a SQL query provided as a string on the given SQLite database
 * and returns the results as a two-dimensional vector of strings, with each inner vector representing
 * a row of the result set.
 * 
 * @param db A pointer to the SQLite database on which the query should be executed.
 * @param query The SQL query string to execute.
 * @return A vector of vectors, where each inner vector contains the column data of a row from the result set.
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
 * Compares two items using a key mapping function.
 *
 * This function applies a key mapping function to two items and then compares 
 * the resulting values. It returns -1 if the value mapped from the first item 
 * is less than that of the second, 1 if greater, and 0 if they are equal.
 * 
 * @param key_map A function or functor that takes an item of type T and returns 
 *                a comparable value.
 * @param item1   The first item to be compared, of type T.
 * @param item2   The second item to be compared, of type T.
 * @return int    Returns -1 if item1 is less than item2, 1 if item1 is greater than 
 *                item2, and 0 if they are equal.
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
 * The string contains both uppercase and lowercase English letters.
 * 
 * @param length The length of the random string to generate.
 * @return A random string consisting of uppercase and lowercase alphabets of the specified length.
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