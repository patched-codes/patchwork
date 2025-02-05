#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type together.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the provided SQLite database and returns the result set.
 * 
 * This function prepares and executes a given SQL query on an SQLite database,
 * iterating over the resulting rows and columns to collect the data into a 
 * vector of vectors of strings. Each sub-vector represents a row from the result
 * set, with each string element representing a column value.
 * 
 * @param db A pointer to the SQLite database on which the query is to be executed.
 *           Must be a valid, open SQLite database connection.
 * @param query A string containing the SQL query to execute.
 * 
 * @return A vector of vectors where each nested vector contains strings
 *         representing the values of a single row from the result set. If
 *         an error occurs during query preparation, an empty vector is returned.
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
 * Compares two items using a key mapping function and returns an integer 
 * indicating the relative ordering of the items.
 * 
 * @param key_map A function that maps an item of type `T` to a comparable type.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer indicating the ordering: -1 if `item1` is less than `item2`, 
 *         1 if `item1` is greater than `item2`, and 0 if they are equal.
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
 * The string contains a mix of uppercase and lowercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A std::string containing random alphabetical characters of the specified length.
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