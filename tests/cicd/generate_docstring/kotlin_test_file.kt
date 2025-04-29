package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers together, which can be of any numeric type, and returns the result as a Double.
 * 
 * @param a The first number to be added; must be a subtype of Number.
 * @param b The second number to be added; must be a subtype of Number.
 * @return The sum of the two numbers, converted to a Double.
 */

fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the results as a list of rows, 
 * where each row is represented as a list of any nullable type.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query string to be executed.
 * @return A list of rows with each row being a list of nullable objects representing the query results.
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
 * Compares two items of type T based on a key extracted by the keyMap function, where the key must be comparable.
 * The comparison result is an integer that indicates the relative order of the items.
 * 
 * @param keyMap A function that extracts a comparable key from an item of type T.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer result of the comparison: -1 if item1 is less than item2, 1 if item1 is greater than item2,
 *         and 0 if they are equal based on their comparable keys.
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
 * The string contains both lowercase and uppercase letters.
 * 
 * @param length The length of the random string to generate.
 * @return A random string of alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}