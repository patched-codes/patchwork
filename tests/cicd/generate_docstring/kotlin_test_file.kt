package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numeric values of type Number and returns the result as a Double.
 * This function accepts generic types constrained to Number, allowing it to 
 * handle various numeric types like Int, Double, Float, etc., and converts 
 * them to Double for precision.
 *
 * @param a The first numeric value to be added.
 * @param b The second numeric value to be added.
 * @return The sum of the two numeric values as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on a provided database connection and returns the results.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query to execute on the database.
 * @return A list of lists, where each inner list represents a row of the result set, 
 *         and each element in the inner list is a column value from the row.
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
 * Compares two items based on the values obtained by applying a key mapping function to each item.
 * The comparison is done using natural ordering of the mapped values.
 * 
 * @param keyMap A function that extracts a comparable key from the items.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer value: -1 if the first item's key is less than the second item's key, 
 *         1 if the first item's key is greater than the second item's key, 
 *         or 0 if both keys are equal.
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
 * The string consists of uppercase and lowercase English letters.
 * 
 * @param length The number of characters in the generated string.
 * @return A string composed of random alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}