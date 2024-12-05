#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of type T and returns the result.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two values of type T.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on a given SQLite database and retrieves the results.
 * 
 * This method prepares and executes the specified SQL query on the provided SQLite 
 * database connection and returns the result as a vector of rows, where each row 
 * is represented as a vector of strings containing the text of each column.
 * 
 * @param db A pointer to an SQLite database object.
 * @param query A constant reference to a string representing the SQL query to be executed.
 * @return A vector of vectors of strings, where each inner vector represents a row from 
 *         the result set and each string within the inner vector represents a column's
 *         text. If the query execution fails, an empty vector is returned.
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
 * Compares two items using a key-mapping function and returns an integer
 * indicating the ordering of the two items.
 * 
 * This function applies a key-mapping function to both items, and then
 * compares the resulting values to determine the relative order of the
 * two input items. It returns -1 if the first item's key is less than
 * the second item's key, 1 if the first item's key is greater, and 0 if
 * both keys are equal.
 * 
 * @param key_map A function or callable that takes an object of type T
 *                and returns a comparable key. This function is used to
 *                extract a sorting key from each input object.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return int Returns -1 if the key of item1 is less than the key of item2,
 *             1 if the key of item1 is greater than the key of item2, 
 *             and 0 if their keys are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets with specified length. The function
 * uses both uppercase and lowercase English letters to form the random string.
 * 
 * @param length The length of the random string to generate.
 * @return A string consisting of randomly chosen alphabetic characters of the specified length.
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