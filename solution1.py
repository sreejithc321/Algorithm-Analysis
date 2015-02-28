# Solution 1 : Check off
#
# Check to see that each character in the first string actually occurs in the second. 
# If it is possible to checkoff each character, then the two strings must be anagrams. 
# Checking off a character will be accomplished by replacing it with None value. 
# Each character from the first string can be checked against the characters and if found, checked off by replacement. 
#

import time
def anagram_detect (string1 ,string2):
	"""anagram detection by checkoff method"""	
	start = time.time()
	# Character split
	string1 = list(string1)
	string2 = list(string2)
	pos1 = 0
	found1 = True
	# For each character in string1
	while (pos1 < len(string1) and found1) :
		pos2 =0
		found2 = False
		# For each character in string 2
		while (pos2 < len(string2) and not found2):
			# checkoff
			if (string1[pos1] == string2[pos2]):
				found2 = True
			else :
				pos2 = pos2 + 1								
		if found2:
			string2[pos2] == None
		else:
			found1 = False	
		pos1 = pos1 + 1		
	end = time.time()
	return found1, end-start
		
## Sample inputs
print anagram_detect('abcd','adbc')
print anagram_detect('abcd','abde')
print anagram_detect('earth','heart')
print anagram_detect('abcdefgh','adghcbfe')
