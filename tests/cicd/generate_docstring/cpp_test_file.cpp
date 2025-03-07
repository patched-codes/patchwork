#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two elements of type T.
 * 
 * @param a The first element of type T to add.
 * @param b The second element of type T to add.
 * @return The sum of the two elements of type T.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on a given SQLite database and returns the results.
 * The function prepares and executes a query, retrieving the result rows
 * as a vector of vectors of strings, where each inner vector represents
 * a row from the result set.
 * 
 * @param db A pointer to the SQLite database connection object.
 * @param query The SQL query to be executed on the database.
 * @return A vector of vectors of strings, containing the results of the query.
 *         Each inner vector corresponds to a row from the result set, with
 *         columns represented as strings.
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
 * Compares two items using a provided key mapping function.
 * 
 * This function applies the key mapping function to both items,
 * compares the resulting keys, and returns -1, 0, or 1 depending 
 * on whether the first key is less than, equal to, or greater 
 * than the second key.
 *
 * @param key_map A function that takes an item of type T and returns a key of any comparable type.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer indicating the comparison result: -1 if the key of item1 is less than the key of item2,
 *         1 if the key of item1 is greater than the key of item2, and 0 if they are equal.
 */

int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of uppercase and lowercase alphabets.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string of the specified length composed of alphabets.
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