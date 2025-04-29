package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numeric values of type Number and returns the result as a Double.
 * 
 * This generic function takes two parameters of any type that is a subclass of Number and converts them to Doubles
 * before performing the addition. This ensures that the addition operation can be performed regardless of the 
 * numeric type provided, and the result is consistently returned as a Double.
 * 
 * @param a The first numeric value to be added. Must be a subtype of Number.
 * @param b The second numeric value to be added. Must be a subtype of Number.
 * @return The result of adding the two provided numbers, returned as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given database connection and returns the results.
 * 
 * @param db The database connection to execute the query on.
 * @param query The SQL query string to be executed.
 * @return A list of lists representing the rows and columns of the query result, 
 *         where each inner list corresponds to a row and contains objects for each column.
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
 * Compares two items of type T based on the values they map to using a provided keyMap function.
 * The comparison is done using natural ordering of these mapped values.
 * 
 * @param keyMap A function that takes an item of type T and returns a Comparable value of type R used for comparison.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer result of the comparison: negative if item1 < item2, positive if item1 > item2, and zero if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of uppercase and lowercase alphabets.
 *
 * @param length The desired length of the random string.
 * @return A string of the specified length consisting of randomly selected alphabets.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}