#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two operands of type T.
 * 
 * @param a The first operand of type T.
 * @param b The second operand of type T.
 * @return The result of adding the two operands, a and b, which is also of type T.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the provided SQLite database and retrieves the results.
 * 
 * This function prepares and executes the given SQL query on the specified SQLite database handle.
 * It fetches the resulting rows as a vector of strings, where each inner vector represents a row
 * from the result set, and each string within the inner vector represents a column value in that row.
 * An empty string is used for NULL or unset columns.
 * 
 * @param db Pointer to an open SQLite database object (sqlite3*) on which the query will be executed.
 * @param query A constant reference to a string representing the SQL query to be executed.
 * @return A vector of vectors containing the query result set with each inner vector representing a row,
 *         and each string within the inner vector representing a column value.
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
 * This function applies the provided key mapping function to each of the two items,
 * and then compares the resulting values. It returns -1 if the first item's mapped
 * value is less than the second item's mapped value, 1 if it is greater, and 0 if 
 * they are equal.
 * 
 * @tparam F The type of the key mapping function.
 * @tparam T The type of the items to compare.
 * @param key_map A function that maps an item to a comparable value.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the result of the comparison: -1 if the 
 *         first item's mapped value is less, 1 if it is greater, and 0 if they are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of uppercase and lowercase alphabets with the specified length.
 * 
 * @param length The length of the random string to be generated.
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