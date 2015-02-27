# Solution 1 : Count and Compare
#
# Count the number of times each character occurs (for each a-z character)
# If the two strings have identical counters for each character, the strings must be anagrams
#

import time
def anagram_detect (string1 ,string2):
	"""anagram detection by count and compare method"""	
	start = time.time()
	# Set character list
	ch_set1 = [0]*26
	ch_set2 = [0]*26	
 	
 	# Count character 
 	for char in list(string1):
 	    pos = ord(char) - ord('a')
 	    ch_set1[pos] = ch_set1[pos] + 1
 	
 	for char in list(string2):
 	    pos = ord(char) - ord('a')
 	    ch_set2[pos] = ch_set2[pos] + 1
 	    
 	end = time.time()
 	
	# compare
	if ch_set1 == ch_set2:
		return True, end-start
	else:
		return False, end-start
	
		
## Sample inputs
print anagram_detect('abcd','adbc')
print anagram_detect('abcd','abde')
print anagram_detect('earth','heart')
print anagram_detect('abcdefgh','adghcbfe')
