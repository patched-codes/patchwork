#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two given values of type T.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two values, a and b.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the provided SQLite database and returns the result as a vector of string vectors.
 * Each sub-vector corresponds to a row in the query result, with each string representing a column value.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors of strings, where each inner vector represents a row from the query result. 
 *         Returns an empty vector if the query fails or if there are no results.
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
 * Compares two items using a provided key mapping function and returns an integer 
 * indicating their relative order based on the mapped values.
 * 
 * @param key_map A function that maps the items to comparable values.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if item1 is less than item2, 1 if item1 is greater than item2, 
 *         and 0 if item1 and item2 are equal based on the mapped values.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of uppercase and lowercase English alphabets.
 * 
 * @param length The desired length of the random string.
 * @return A string containing randomly selected alphabets of the specified length.
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