#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Calculates the sum of two values of the same type.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The result of adding the two values.
 */

T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the provided SQLite database and returns the result as a vector of string vectors.
 * 
 * This function prepares the SQL statement, steps through each row returned by the query, and collects the
 * data into a two-dimensional vector. Each outer vector represents a row, and each inner vector represents
 * the columns of that row. If any column value is `null`, it is represented as an empty string in the result.
 * 
 * @param db A pointer to the SQLite database on which the query is to be executed.
 * @param query A string representing the SQL query to be executed.
 * @return A vector of vectors, where each inner vector represents a row from the query result, with each
 *         element being a string representation of the column value.
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
 * Compares two items using a key extraction function and returns an integer 
 * indicating their relative order.
 * 
 * @param key_map Function that extracts the key from the items to be compared.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if the first item's key is less than the second's, 
 *         1 if greater, or 0 if equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets with the given length.
 * The string contains a mix of lowercase and uppercase letters.
 * 
 * @param length The desired length of the random string.
 * @return A string composed of randomly selected alphabetic characters with the specified length.
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