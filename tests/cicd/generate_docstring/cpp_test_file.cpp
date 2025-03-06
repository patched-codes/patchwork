#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two elements of the same type together and returns the result.
 * 
 * @param a The first element to add.
 * @param b The second element to add.
 * @return The result of adding the two elements together.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a given SQL query on a SQLite database and returns the results as a 2D vector of strings.
 * Each inner vector corresponds to a row from the query results.
 *
 * @param db A pointer to the SQLite database object on which the query is to be executed.
 * @param query A string representing the SQL query to execute.
 * @return A 2D vector of strings containing the results of the query execution, where each inner vector represents a row.
 *         If the query fails to prepare, an empty vector is returned.
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
 * Compares two items based on a key mapping function and returns an integer
 * indicating their relative order. This can be useful for sorting operations.
 * 
 * @param key_map A function or callable object that takes an item of type T 
 *                and returns a value that can be compared using the < and > 
 *                operators.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer: -1 if item1 is less than item2, 1 if item1 is greater 
 *         than item2, or 0 if they are equal according to the key_map.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets with the specified length.
 * The generated string includes both lowercase and uppercase letters.
 * 
 * @param length The length of the random string to generate.
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