# Solution 1 : check off
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
	# String length comparison
	if len(string1) != len(string2):
		print "Strings length should be equal... !!"
	else:	
		# Character split
		string1 = list(string1)
		string2 = list(string2)
		string1_pos = 0
		string1_found = True
		# For each character in string1
		while (string1_pos < len(string1) and string1_found ==True) :
			string2_pos =0
			string2_found = False
			# For each character in string 2
			while (string2_pos < len(string2) and string2_found == False):
				# checkoff
				if (string1[string1_pos] == string2[string2_pos]):
					string2[string2_pos] == None
					string2_found = True
				else :
					string2_pos = string2_pos + 1								
			if string2_found == True:
				string1_pos = string1_pos + 1		
			else:
				string1_found = False	
		end = time.time()
        # Result
		if string1_found == True:
			print "Strings are anagrams !!\t\tTime taken = ", end-start		
		else:
			print "Strings are not anagrams !!\t\tTime taken = ", end-start	
		
## Sample inputs
anagram_detect('abcd','adbc')
anagram_detect('abc','adbc')
anagram_detect('abcd','abde')
anagram_detect('earth','heart')
