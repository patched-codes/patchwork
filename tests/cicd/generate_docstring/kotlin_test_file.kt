package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers together and returns the result as a Double.
 * 
 * @param a The first number to be added. It must be a type that extends Number.
 * @param b The second number to be added. It must be a type that extends Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes the provided SQL query on the given database connection and returns the result as a list of rows,
 * with each row represented as a list of nullable objects.
 * 
 * @param db Database connection to be used for executing the query.
 * @param query SQL query string to be executed.
 * @return A list of rows, where each row is a list of column values.
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
 * Compares two items of type T based on a key extracted by a specified key mapping function.
 * The comparison is done by evaluating the order of the keys which are derived as comparable items of type R.
 *
 * @param keyMap A function that maps an item of type T to a key of type R which is comparable.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the order difference: -1 if the key of item1 is less than the key of item2,
 *         1 if it is greater, or 0 if they are equal.
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
 * The string contains both lowercase and uppercase characters.
 * 
 * @param length The desired length of the random string to be generated.
 * @return A string consisting of randomly selected alphabet characters with the specified length.
 */

fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}