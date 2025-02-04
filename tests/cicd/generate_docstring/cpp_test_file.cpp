#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * This function takes two parameters of the same type and returns their sum.
 * 
 * @param a First operand of the addition.
 * @param b Second operand of the addition.
 * @return The sum of the two operands.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the given SQLite database and returns the results as a vector of string vectors.
 * Each inner vector represents a row of the result set, with each string being a column value.
 * 
 * @param db A pointer to the SQLite3 database connection object used for executing the query.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors of strings containing the query results. Each inner vector corresponds to a row from the result set.
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
 * Compares two items using a specified key mapping function.
 * 
 * @param key_map Function used to extract a comparable value from each item.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return -1 if the key value of item1 is less than that of item2,
 *         1 if the key value of item1 is greater than that of item2,
 *         0 if the key values are equal.
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
 * 
 * The generated string includes both lowercase and uppercase alphabets.
 * 
 * @param length The desired length of the generated random string.
 * @return A random string composed of lowercase and uppercase alphabets
 *         of the specified length.
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