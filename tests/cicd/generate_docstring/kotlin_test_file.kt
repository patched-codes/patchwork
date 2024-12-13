package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers, converting them to double.
 * This function takes two numbers as input parameters and returns their sum as a double.
 *
 * @param a The first number to be added, constrained to be a subtype of Number.
 * @param b The second number to be added, constrained to be a subtype of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given database connection and retrieves the results as a list of rows, 
 * where each row is represented as a list of column values.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query string to be executed on the database.
 * @return A list containing rows of the result set, where each row is a list of column values.
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
 * Compares two items using a keyMap function to extract the comparable keys.
 * Returns an integer indicating the order of the two items.
 * 
 * @param T The type of the items to be compared.
 * @param R The type of the comparable key extracted from the items.
 * @param keyMap A function that extracts the key from an item, which is used for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return Int Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of uppercase and lowercase alphabetic characters.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string of the specified length containing alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}