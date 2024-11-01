package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns the result as a Double.
 * 
 * @param a The first number to be added. It must be of a type that extends Number.
 * @param b The second number to be added. It must be of a type that extends Number.
 * @return The sum of the two numbers, returned as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on a database connection and retrieves the results as a list of rows.
 * Each row is represented as a list of nullable objects corresponding to the column values.
 * 
 * @param db The active database connection to execute the query on.
 * @param query The SQL query string to be executed.
 * @return A list of lists where each inner list represents a row of the result set.
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
 * Compares two items using a provided key mapping function and returns -1, 0, or 1 depending on
 * whether the first item is less than, equal to, or greater than the second item, respectively.
 *
 * @param keyMap A function that maps an item of type T to a comparable key of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer indicating the comparison result: -1 if item1 is less than item2, 1 if item1
 *         is greater than item2, or 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters with the specified length.
 * This string can include both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string consisting of alphabetic characters of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}