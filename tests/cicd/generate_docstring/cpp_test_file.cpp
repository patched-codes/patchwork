#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two generic elements of the same type and returns their sum.
 * 
 * @param a The first element to be added.
 * @param b The second element to be added.
 * @return The sum of the two input elements.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on a given SQLite database and returns the results
 * as a vector of vectors of strings, where each inner vector represents a row
 * and each string in that vector represents a column value.
 * 
 * @param db A pointer to the SQLite database instance to execute the query on.
 * @param query A SQL query string to be executed on the database.
 * @return A vector of vectors of strings containing the queried data from the database.
 *         Each inner vector represents a row with column values as strings.
 *         Returns an empty vector if the query cannot be prepared or executed.
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
 * Compares two items using a specified key mapping function and returns an integer based on their comparison.
 * 
 * @param key_map A callable object (function, lambda, functor) that maps an item of type T to a comparable value.
 * @param item1 The first item of type T to compare.
 * @param item2 The second item of type T to compare.
 * @return An integer: -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, 
 *         or 0 if both keys are equal.
 */

int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of alphabetic characters only, 
 * both uppercase and lowercase.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string consisting of the specified number of alphabetic characters.
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