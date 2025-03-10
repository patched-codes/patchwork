package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numeric values of type T and returns their sum as a Double.
 * This function converts the input parameters to Double before performing the addition,
 * ensuring the operation is valid for any numeric subtype of Number.
 * 
 * @param a The first numeric value of type T to be added.
 * @param b The second numeric value of type T to be added.
 * @return The sum of a and b as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the specified SQLite database connection and returns the results 
 * as a list of lists, where each inner list represents a row of the query result, and each element 
 * in the inner list corresponds to a column value.
 * 
 * @param db The database connection through which the SQL command is executed.
 * @param query The SQL query string to be executed on the database.
 * @return A list of lists containing the query result data. Each inner list represents a row and 
 *         contains column values as elements. The elements can be of any type as returned by 
 *         the SQL query.
 */
fun sqlite(db: Connection, query: String): List<List<Any?>> {
    db.createStatement().use { statement ->
        statement.executeQuery(query).use { resultSet ->
            val results = mutableListOf<List<Any?>>()
            val columnCount = resultSet.metaData.columnCount

            while (resultSet.next()) {
                val row = mutableListOf<Any?>()
                for (i in 1..columnCount) {
                    row.add(resultSet.getObject(i))
                }
                results.add(row)
            }
            return results
        }
    }
}


/**
 * Compares two items of type T using a mapping function that extracts a Comparable key from each item.
 * The result of this comparison can be -1, 0, or 1 indicating less than, equal to, or greater than, respectively.
 * 
 * @param keyMap A function that maps an item of type T to a Comparable key of type R for comparison.
 * @param item1 The first item of type T to compare.
 * @param item2 The second item of type T to compare.
 * @return An integer result of the comparison: -1 if item1 is less than item2, 1 if item1 is greater than item2, 
 *         or 0 if they are considered equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with the specified length.
 * The string includes both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to generate.
 * @return A string composed of randomly selected alphabets of the given length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}