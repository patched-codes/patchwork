#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two elements.
 * 
 * @param a The first element to be added.
 * @param b The second element to be added.
 * @return The sum of the two elements.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the provided SQLite database and returns the query result as a vector of string vectors.
 *
 * This function prepares and executes the given SQL query on the specified SQLite database. It retrieves all resulting rows 
 * and columns, stores them in a vector of vectors of strings, and returns this vector. Each inner vector represents a row, 
 * and each string within the inner vectors represents a column value.
 * 
 * @param db The SQLite database connection object.
 * @param query The SQL query string to be executed.
 * @return A two-dimensional vector where each element is a vector of strings representing a row from the query result. 
 *         If the query preparation fails, an empty vector is returned.
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
 * Compares two items by applying a transformation function to each and comparing the transformed values.
 * 
 * @param key_map A function that takes an item and returns a comparable value.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return -1 if the transformed value of item1 is less than the transformed value of item2, 
 *         1 if the transformed value of item1 is greater than the transformed value of item2,
 *         0 if both transformed values are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of alphabets, both uppercase and lowercase.
 * The length of the generated string is defined by the input parameter.
 * 
 * @param length The length of the random alphabet string to be generated.
 * @return A random string of the specified length composed of uppercase and lowercase alphabets.
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