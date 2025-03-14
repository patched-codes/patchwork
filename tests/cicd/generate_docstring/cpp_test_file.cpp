#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two given values of the same type.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The result of adding the two values together.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the given SQLite database and returns the results.
 * 
 * This function prepares and executes a SQL query on the provided SQLite database
 * and processes the results. Each row retrieved from the database is converted
 * into a vector of strings, with each string representing the text of the columns
 * in that row. All rows are collected into a vector that is returned as the result.
 * 
 * @param db A pointer to an SQLite database connection.
 * @param query A SQL query string to be executed on the database.
 * @return A vector of vectors, where each inner vector represents a row from the 
 *         query result, with each element being a column in that row. An empty 
 *         vector is returned if the query fails.
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
 * Compares two items using a key mapping function to determine their order.
 * 
 * This function uses the key_map function to extract comparison keys from 
 * both item1 and item2, then compares these keys. It returns -1 if the key 
 * for item1 is less than the key for item2, 1 if greater, and 0 if they 
 * are equal.
 * 
 * @param key_map A function that takes an item of type T and returns a value 
 *                that can be compared, determining the order.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return -1 if item1 < item2, 1 if item1 > item2, and 0 if they are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabetic characters with a specified length.
 * The string will contain both uppercase and lowercase letters.
 * 
 * @param length The desired length of the random string to be generated.
 * @return A std::string containing random alphabetic characters of the specified length.
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