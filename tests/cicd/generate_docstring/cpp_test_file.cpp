#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two values.
 * 
 * This function takes two parameters of the same type and returns their sum.
 * It uses the addition operator to compute the result.
 * 
 * @param a The first value of the sum.
 * @param b The second value of the sum.
 * @return The sum of the input parameters.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the provided SQLite database and returns the results.
 * 
 * This function prepares and steps through the results of an SQL query on the given database,
 * collecting each row of the result set into a vector of strings. Each row is represented as 
 * a vector of strings where each string corresponds to a column value. If a column value is NULL, 
 * an empty string is added in its place. The results are compiled into a vector of vectors representing 
 * all the rows retrieved by the query.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query The SQL query string to be executed on the database.
 * @return A vector of vectors of strings containing the results of the query, where each inner vector 
 *         represents a row and each string within the row represents a column value.
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
 * Compares two items based on a key derived by a provided mapping function.
 * 
 * @param key_map A function that maps an item of type T to a comparable value.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer: -1 if item1 < item2, 1 if item1 > item2, 0 if both are equal based on the key_map.
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
 * The string contains a mix of lowercase and uppercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A string containing randomly selected alphabetic characters, 
 *         with a length equal to the specified parameter.
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