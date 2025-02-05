package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns the result as a Double.
 * 
 * @param a The first number to be added, constrained to be a type of Number.
 * @param b The second number to be added, constrained to be a type of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes an SQL query against the provided database connection and returns the result as a list of rows.
 * Each row is represented as a list of column values.
 * 
 * @param db The database connection to be used for the query.
 * @param query The SQL query to be executed.
 * @return A list of rows, where each row is a list of column values obtained from the query result.
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
 * Compares two items based on a specified derived key obtained from a mapping function.
 * 
 * @param keyMap A lambda function that maps an item of type T to a comparable key of type R.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer representing the comparison result: -1 if the key of item1 is less than item2's key,
 *         1 if it is greater, and 0 if they are equal.
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
 * The string contains both uppercase and lowercase alphabets.
 * 
 * @param length The length of the random string to generate.
 * @return A random string consisting of uppercase and lowercase alphabets.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}