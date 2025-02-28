package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers and returns the result as a Double.
 * 
 * @param a The first number to add, a number of type T, where T is a subtype of Number.
 * @param b The second number to add, a number of type T, where T is a subtype of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on a provided SQLite database connection
 * and returns the result as a list of rows, where each row is a list of column values.
 * 
 * @param db The Connection object representing the SQLite database connection.
 * @param query The SQL query string to be executed.
 * @return A list of lists where each inner list represents a row from the query result set,
 *         and each element in the inner list represents a column value in the row.
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
 * Compares two items based on a key extracted using a provided key-mapping function.
 * 
 * This function applies the keyMap function to both items to extract a key,
 * then compares the keys using their natural ordering.
 * 
 * @param keyMap A lambda function that extracts a comparable key from an item.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the result of the comparison: 
 *         -1 if the key of item1 is less than the key of item2,
 *         1 if the key of item1 is greater than the key of item2,
 *         0 if both keys are equal.
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
 * The string is composed of both uppercase and lowercase letters.
 * 
 * @param length The desired length of the generated string.
 * @return A random string containing only alphabetical characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}