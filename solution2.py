# Solution 2 : Sort and Compare
#
# Sort each string alphabetically and end up with the same string if the original two strings are anagrams. 
#
import time
def anagram_detect (string1 ,string2):
	"""anagram detection by sort and compare method"""	
	start = time.time()
	# sort strings
	string1 = list(string1)
	string1.sort()
	string2 = list(string2)
	string2.sort()
	end = time.time()
	# compare
	if string1 == string2:
		return True, end-start
	else:
		return False, end-start

## Sample inputs
print anagram_detect('abcd','adbc')
print anagram_detect('abcd','abde')
print anagram_detect('earth','heart')
print anagram_detect('abcdefgh','adghcbfe')

