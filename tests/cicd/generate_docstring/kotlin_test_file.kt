package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a generic type that extends from Number and returns the result as a Double.
 * 
 * @param a The first number to add. Must be of a type that is a subtype of Number.
 * @param b The second number to add. Must be of a type that is a subtype of Number.
 * @return The sum of the provided numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given database connection and returns the results.
 *
 * @param db The connection to the SQLite database.
 * @param query The SQL query to be executed.
 * @return A list of lists representing the query result, where each inner list is a row and 
 *         each element is a column value of any data type.
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
 * Compares two items based on a given key mapping function that maps
 * each item to a comparable value.
 * 
 * @param keyMap A function that takes an item of type T and returns a comparable value of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return -1 if the key of item1 is less than the key of item2, 
 *         1 if the key of item1 is greater than the key of item2,
 *         0 if the keys of item1 and item2 are equal.
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
 * The string consists of both uppercase and lowercase letters.
 * 
 * @param length The desired length of the generated string.
 * @return A string composed of random alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}