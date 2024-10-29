#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two given inputs.
 * 
 * @param a The first operand.
 * @param b The second operand.
 * @return The result of adding a and b.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on a SQLite database and retrieves the results.
 * 
 * This function takes a SQLite database connection and an SQL query as parameters, 
 * executes the query, and returns the results as a two-dimensional vector, where each 
 * sub-vector represents a row of the resulting data, and each string in the sub-vector 
 * represents a column in that row.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors of strings, containing the query results. Each sub-vector 
 *         represents a row and each string within a row represents a column value. 
 *         An empty vector is returned if the query fails.
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
 * Compares two items based on a key extracted through a mapping function.
 * 
 * @param key_map A function or functor that extracts a comparable key from each item.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return -1 if the key of item1 is less than the key of item2,
 *         1 if the key of item1 is greater than the key of item2,
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
 * Generates a random string of alphabetic characters of a specified length.
 * Utilizes both lowercase and uppercase English alphabets to form the string.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string consisting of alphabetic characters with the specified length.
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