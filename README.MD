##   Algorithm Analysis
Compare run time of different algorithms to perform Anagram Detection. 

## Anagram Detection
One string is an anagram of another if the second is simply a rearrangement of the first. 

For example : 'heart' and 'earth' are anagrams, 'python' and 'typhon' are anagrams 

### Aim : 
* Write a boolean function that will take two strings and return whether they are anagrams.
* Analyze algorithm’s efficiency in terms of execution time

### Assumption : 
* Strings are of equal length 
* Strings are made up of symbols from the set of 26 lowercase alphabetic characters. 

#### Solution 1 : Checking Off 
- Check that each character in the first string actually occurs in the second

#### Solution 2 : Sort and Compare 
- Sorting each string alphabetically, this will end up with the same string if the original two strings are anagrams

#### Solution 3 : Count and Compare 
-  First count the number of times each character occurs. Since there are 26 possible characters, we can use a list of 26 counters, one for each possible character. Each time we see a particular character, we will increment the counter at that position. In the end, if the two lists of counters are identical, the strings must be anagrams.

#### Execution time:

   * Solution 1 : O(n^2)
   * Solution 2 : O(n^2)/O(nlogn), due to sorting
   * Solution 3 : O(n)











