package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type T that is a subclass of Number and returns the result as a Double.
 * 
 * @param a The first number to add, of type T which extends Number.
 * @param b The second number to add, also of type T which extends Number.
 * @return The sum of 'a' and 'b', converted to a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on a provided SQLite database connection and returns the results.
 * 
 * The function uses the provided database connection to create a statement, executes the query,
 * and processes the resulting data into a list of rows, where each row is represented as a list of 
 * column values.
 * 
 * @param db The SQLite database connection to be used for executing the query.
 * @param query The SQL query string to be executed on the database.
 * @return A list of lists, where each sublist represents a row in the result set, and each element
 *         in the row is a column value. The elements are of type Any? to accommodate the various
 *         kinds of data types that might be present in a database table.
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
 * Compares two items using a key map to determine the order based on their comparable key.
 * 
 * @param keyMap a function that maps an item of type T to a key of type R, which is comparable
 * @param item1 the first item to compare
 * @param item2 the second item to compare
 * @return an integer; -1 if the key of item1 is less than the key of item2, 1 if greater, and 0 if equal
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
 * 
 * @param length The desired length of the random alphabetic string.
 * @return A string composed of random alphabetic characters (both uppercase and lowercase).
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}