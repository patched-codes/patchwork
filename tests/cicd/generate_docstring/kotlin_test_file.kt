package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns the result as a Double.
 * 
 * @param a The first number to be added, constrained to be a subtype of Number.
 * @param b The second number to be added, constrained to be a subtype of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the result as a list of rows.
 * Each row is represented as a list of column values.
 * 
 * @param db The database connection to use for executing the SQL query.
 * @param query The SQL query to be executed on the database.
 * @return A list of lists, where each inner list represents a row from the query result set, and each element
 *         in the inner list is a column value from that row, which can be of any type or null.
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
 * Compares two items using a specified key mapping function and returns an integer representing their order.
 * 
 * The comparison is based on the results of the keyMap function applied to the items, using natural ordering.
 * 
 * @param <T> The type of the items being compared.
 * @param <R> The type of the key extracted from the items. This type must be comparable.
 * @param keyMap A function that takes an item of type T and returns a key of type R that is comparable.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the order of the items:
 *         - Returns -1 if item1's key is less than item2's key.
 *         - Returns 1 if item1's key is greater than item2's key.
 *         - Returns 0 if both keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of alphabetic characters.
 * 
 * This function creates a string of random letters with the specified length,
 * using both lowercase and uppercase alphabetic characters.
 *
 * @param length The number of characters in the generated string.
 * @return A randomly generated string of the specified length composed of alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}