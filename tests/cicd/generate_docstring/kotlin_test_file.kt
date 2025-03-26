package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns their sum as a Double.
 * 
 * @param a First number to add, extends Number.
 * @param b Second number to add, extends Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given database connection and retrieves the results.
 * 
 * @param db The database connection to use for executing the query.
 * @param query The SQL query string to be executed.
 * @return A list of lists, where each sublist represents a row of the query result
 *         with its columns. Each element in a sublist corresponds to the column 
 *         value of that row which can be of any type or null.
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
 * Compares two items based on a key extracted from each item using a given key mapping function.
 * This function applies the key map to both items and returns -1 if the first item is less than the second,
 * 1 if the first is greater, and 0 if they are equal.
 * 
 * @param keyMap A function that extracts a comparable key from each item.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the comparison result: -1 if the first item is less, 1 if greater, and 0 if equal.
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
 * The string contains both uppercase and lowercase letters.
 * 
 * @param length The length of the random alphabet string to generate.
 * @return A randomly generated string of alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}