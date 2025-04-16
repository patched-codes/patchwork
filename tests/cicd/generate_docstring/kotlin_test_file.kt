package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numeric values by converting them to Double.
 * 
 * This function accepts any type that extends Number, converts the values to Double, 
 * and returns the sum as a Double.
 * 
 * @param a The first numeric value of type T, where T extends Number.
 * @param b The second numeric value of type T, where T extends Number.
 * @return The sum of a and b as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given database connection and returns the results as a list of lists.
 * Each inner list represents a row from the result set, with each element corresponding to a column value.
 * 
 * @param db The database connection to use for executing the query.
 * @param query The SQL query to be executed on the database.
 * @return A list of rows, where each row is represented as a list of objects. Each object corresponds to a column value in the result set. Returns an empty list if no results are found.
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
 * Compares two items using a provided key mapping function, which extracts a comparable value from each item.
 * Returns -1 if the first item is less than the second, 1 if it is greater, and 0 if they are equal, based on the comparable value.
 * 
 * @param keyMap A function that maps an item of type T to a comparable value of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer result of the comparison: -1, 0, or 1.
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
 * The string includes both lowercase and uppercase English letters.
 * 
 * @param length The desired length of the randomly generated string.
 * @return A string consisting of random uppercase and lowercase alphabets.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}