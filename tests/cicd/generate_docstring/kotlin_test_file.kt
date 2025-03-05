package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numeric values and returns the result as a Double.
 * This function accepts two parameters of any type that extends the Number class,
 * converts them to doubles, and returns their sum.
 * 
 * @param a The first numeric value to be added. Must be a type that extends Number.
 * @param b The second numeric value to be added. Must be a type that extends Number.
 * @return The sum of the two numeric values as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a provided SQL query on the given database connection and retrieves the results as a list of rows, 
 * where each row is a list of column values. This method assumes that the caller is responsible for 
 * managing the database connection lifecycle.
 * 
 * @param db The Connection object representing the database connection to be used for executing the query.
 * @param query A string containing the SQL query to be executed.
 * @return A list of rows, with each row being a list of column values. Each column value is of type Any?, 
 * representing the result of the corresponding column in the query.
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
 * Compares two items based on the specified keymapping function, returning an integer indicating their order.
 * The function `keyMap` extracts a comparable key from each item, and the comparison is made on these keys.
 * 
 * @param T the type of the items to compare
 * @param R the type of the comparable keys, which must be a `Comparable`
 * @param keyMap a function that maps an item of type `T` to a comparable key of type `R`
 * @param item1 the first item to be compared
 * @param item2 the second item to be compared
 * @return -1 if the key of `item1` is less than the key of `item2`; 
 *         1 if the key of `item1` is greater than the key of `item2`; 
 *         0 if the keys are equal
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
 * The string includes both uppercase and lowercase alphabets.
 * 
 * @param length The desired length of the resulting random string.
 * @return A string consisting of randomly selected uppercase and lowercase alphabets.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}