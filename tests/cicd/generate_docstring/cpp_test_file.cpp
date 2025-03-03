#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type.
 * 
 * This function takes two parameters of a generic type and returns their sum. 
 * The function assumes that the '+' operator is defined for the type T.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two input values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on a provided SQLite database connection and retrieves the results.
 * The results are stored in a vector of vectors of strings, where each inner vector represents a row.
 * 
 * @param db A pointer to the SQLite database connection object (sqlite3*).
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors of strings, with each inner vector representing a row of results.
 *         Each element of the inner vector represents a column as a string. An empty vector is returned if the query fails.
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
 * Compares two items using a key map function and returns an integer indicating their order.
 * 
 * This function applies a key map function to two items to obtain comparable values and then
 * compares these values. It returns -1 if the first item's key is less than the second item's key,
 * 1 if the first item's key is greater than the second item's key, and 0 if both keys are equal.
 * 
 * @param key_map A function or callable object that takes an item of type T and returns a comparable key.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if item1 < item2, 1 if item1 > item2, and 0 if item1 == item2.
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
 * The string consists of uppercase and lowercase English letters.
 * 
 * @param length The length of the random string to generate.
 * @return A randomly generated string containing alphabets of the specified length.
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