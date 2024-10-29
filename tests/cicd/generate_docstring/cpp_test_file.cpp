#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two elements.
 * 
 * @param a The first element to be added.
 * @param b The second element to be added.
 * @return The sum of the two elements.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a given SQL query on a SQLite database and retrieves the results.
 * 
 * @param db A pointer to the SQLite database connection object.
 * @param query A string containing the SQL query to be executed.
 * @return A two-dimensional vector of strings, where each inner vector represents a row of results from the query, and each string in the inner vector represents a column value.
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
 * Compares two items using a key mapping function and returns an integer indicating their relative order.
 * 
 * @param key_map A function object that, when given an item, returns a value to be used for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the order: -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets with a specified length.
 * The string consists of both uppercase and lowercase English letters.
 * 
 * @param length The desired length of the random string.
 * @return A random string of alphabets of the specified length.
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