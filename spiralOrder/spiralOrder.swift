class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        return spiralOrderHelper(matrix, [Int](), matrix[0].count, matrix.count)
    }
    func spiralOrderHelper(_ matrix: [[Int]], _ arrSoFar: [Int], _ init_col_len: Int, _ init_row_len: Int) -> [Int] {
        // First row: print all the contents and remove the row
        // 2nd to 2nd to last row: print and remove the last element
        // last row: print all the elements in reverse and remove the row
        // 2nd-to-last row to 3rd: print first element
        //
        // 2nd row: print all the contents and remove the row
        // ...
        // ==> recursion!
        // Base-case: first & last rows are nil && all other rows are length-2 => return the contentSoFar
        // case 1: first row && all rows are length => add all the contents to contentSoFar (and remove them from the row => empty row)
        // case 2: last row && first row is nil && all other rows are length-1=> add all the contents IN REVERSE to contentSoFar (and remove them from the row => empty row)
        // case 3: first row is nil && last row is not => for every rows with length, add the last element to contentSoFar (and remove it from the row)
        // case 4: first & last rows are nil => for every rows length-1, add the first element to contentSoFar (and remove it from the row)
        //
        // Note:
        // - Every row should be visited len(column) times
        // - Every column should be visited len(row) times
        //
        // Pseudo-code:
        // if first-row == nil {
        //      if last-row == nil { 
        //          "CASE 4" (for each length-1, starting from the last row, add the last element to contentSoFar - and remove it from the row)
        //          if (all rows are length-2) { "BASECASE" (return contentSoFar + nextIteration }
        //      } else { 
        //          if (len(all-other-rows) == len - 1) {
        //              "CASE 2" (add all the contents IN REVERSE to contentSoFar - and remove them from the row)
        //          } else {
        //            "CASE 3" (for each rows == len from the top, add the last element to contentSoFar - and remove it from the row)
        //          }
        //      }
        // } else {
        //      "CASE 1" (add all the contents to contentSoFar - and remove them from the row)
        //  }
        
        var col = 0, row = 0
        var intArrToReturn = [Int]()
        var matrixCopy = [[Int]]()
        matrixCopy = matrix
        
        if matrixCopy[0].count == 0 {
            if matrixCopy[init_row_len - 1].count == 0 {
                if matrixCopy[1].count == init_col_len - 2 {  // If the 2nd row is init_col_len - 2
                    // print("BASE-CASE")
                    // Remove the first/last rows of matrixCopy and recurse with sprialOrderHelper
                    // print(matrixCopy)
                    matrixCopy.remove(at: 0)
                    matrixCopy.remove(at: init_row_len-2)
                    // print(matrixCopy)
                    // reset init_col_len & init_row_len in spiralOrder
                    return arrSoFar + spiralOrderHelper(matrixCopy, intArrToReturn, matrixCopy[0].count, matrixCopy.count)
                } else {
                    // print("CASE 4")
                    // first & last rows are nil => for every rows length-1, add the first element to contentSoFar (and remove it from the row)
                    intArrToReturn = arrSoFar
                    for row in (1...(init_row_len - 2)).reversed() {
                        // print("row: \(row)")
                        intArrToReturn.append(matrixCopy[row].removeFirst())
                    }
                    // print("Sofar: \(intArrToReturn)")
                    return spiralOrderHelper(matrixCopy, intArrToReturn, init_col_len, init_row_len)
                }
            } else {
                if matrixCopy[init_row_len - 2].count == init_col_len - 1 { // If the 2nd-to-last row is init_col_len - 1
                    // print("CASE 2")
                    let lastRowReverse = Array(matrixCopy[init_row_len - 1].reversed())
                    matrixCopy[init_row_len - 1] = [Int]()
                    intArrToReturn = arrSoFar + lastRowReverse
                    // print(matrixCopy)
                    // print(intArrToReturn)
                    return spiralOrderHelper(matrixCopy, intArrToReturn, init_col_len, init_row_len)
                } else {
                    // print("CASE 3")
                    // (for each rows == len from the top, add the last element to contentSoFar - and remove it from the row)
                    intArrToReturn = arrSoFar
                    for row in 1...(init_row_len - 2) {    // Traverse from row 1 through max_row-1
                        // print(matrixCopy[row])
                        intArrToReturn.append(matrixCopy[row].popLast()!)
                        // Should be true
                        // print(matrixCopy[0].count == 0)
                        // print(matrixCopy[row].count == init_col_len - 1)
                        // print("ArrSoFar: \(intArrToReturn)")
                    }
                    return spiralOrderHelper(matrixCopy, intArrToReturn, init_col_len, init_row_len)
                }
            }
        } else {
            if matrixCopy.count == 1 { return matrixCopy[0] }
            // print("CASE 1")
            intArrToReturn = matrixCopy[0]
            matrixCopy[0] = [Int]()
            return spiralOrderHelper(matrixCopy, intArrToReturn, init_col_len, init_row_len)
        }
    }
}
