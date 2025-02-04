package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns the result as a Double.
 * 
 * @param a The first number to be added. Must be a subclass of Number.
 * @param b The second number to be added. Must be a subclass of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes an SQL query on the provided database connection and returns the result as a list of rows.
 * Each row is represented as a list of objects.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query to be executed.
 * @return A list of rows, where each row is a list of objects representing the column values in the result set.
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
 * Compares two items based on a key derived from the items using the provided key mapping function.
 * The comparison result is based on the natural ordering of the keys.
 *
 * @param T the type of the items to compare.
 * @param R the type of the key derived from the item, which must be comparable.
 * @param keyMap a function that takes an item of type T and returns a comparable key of type R.
 * @param item1 the first item to compare.
 * @param item2 the second item to compare.
 * @return -1 if item1's key is less than item2's key, 1 if item1's key is greater than item2's key, and 0 if the keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with a specified length.
 * The generated string includes both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string composed of alphabetical characters with the given length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}