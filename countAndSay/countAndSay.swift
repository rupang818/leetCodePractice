class Solution {
    func countAndSay(_ n: Int) -> String {
        if n == 1 { return "1" }
        let termToSay = getTheNthTerm(n)
        // print("Term to say: \(termToSay)")
        if termToSay == "" { return termToSay }
        
        // get first character, count how many time(s) it repeats, 
        var termToSayString = String(termToSay)
        var currentChar = String(termToSayString.prefix(1))
        var outputStr = "", count = 0
        
        while termToSayString != "" {
            if termToSayString.hasPrefix(currentChar) { 
                // print("prefix match")
                count += 1 
            } else {
                // print("prefix does not match")
                let inserToString = String(count) + currentChar
                // print("Appending this to the beginning of the string: \(inserToString)")
                outputStr.append(String(count) + currentChar)
                
                currentChar = String(termToSayString.prefix(1))
                count = 1
            }
            // print("Before: \(termToSayString)")
            termToSayString.remove(at: termToSayString.startIndex)
            // print("After: \(termToSayString)")
        }
        
        outputStr.append(String(count) + currentChar)
        // print("outputStr: \(outputStr), count: \(count), n: \(n), currentChar: \(currentChar)")
        return outputStr
    }
    
    func getTheNthTerm(_ n: Int) -> String {
        if n < 1 { return "" }
        else if n == 1 { return "1"}
        else {
            return countAndSay(n - 1)
        }
    }
}
