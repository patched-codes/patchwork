#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two values of the same type.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the given SQLite database and returns the results as a vector of vectors of strings.
 * Each sub-vector in the result represents a row of the query result with its columns as strings.
 * 
 * @param db Pointer to an SQLite database connection object.
 * @param query The SQL query in string format to be executed on the database.
 * @return A vector of vectors of strings, where each sub-vector contains the data from a single row of the query result. 
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
 * Compares two items using a specified key mapping function and returns an integer indicating their relative ordering.
 * 
 * Uses the key_map function to extract comparison keys from item1 and item2.
 * Returns -1 if the key of item1 is less than the key of item2, 1 if it's greater, and 0 if they are equal.
 * 
 * @param key_map Function object or lambda that maps an item of type T to a comparable value.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer indicating the result of the comparison: -1 if item1 < item2, 1 if item1 > item2, and 0 if item1 == item2.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of lowercase and uppercase alphabets.
 * 
 * @param length The length of the random string to generate.
 * @return A random string consisting of the specified number of random alphabets.
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