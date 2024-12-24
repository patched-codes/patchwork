package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns their sum as a Double.
 * 
 * @param a The first number to be added, which must be a subtype of Number.
 * @param b The second number to be added, which must be a subtype of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the given database connection and returns the results.
 *
 * @param db The database connection used to execute the query.
 * @param query The SQL query to be executed.
 * @return A list of lists where each inner list represents a row retrieved from the database and each element in the row corresponds to a column value.
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
 * Compares two items based on a key derived from each item using a key mapping function.
 *
 * @param keyMap A function that maps an item of type T to a comparable key of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the result of the comparison: 
 *         -1 if the key of item1 is less than the key of item2,
 *          1 if the key of item1 is greater than the key of item2,
 *          0 if the keys of item1 and item2 are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with the given length.
 * The string includes both uppercase and lowercase letters.
 * 
 * @param length The length of the random alphabet string to generate.
 * @return A random string consisting of alphabetic characters with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}