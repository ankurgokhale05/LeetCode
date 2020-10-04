'''
The idea is we use a variable-length sliding window which is gradually applied across the string. We use two pointers: start and end to mark the sliding window. We start by fixing the start pointer and moving the end pointer to the right. The way we determine the current window is a valid one is by checking if all the target letters have been found in the current window. If we are in a valid sliding window, we first make note of the sliding window of the most minimum length we have seen so far. Next we try to contract the sliding window by moving the start pointer. If the sliding window continues to be valid, we note the new minimum sliding window. If it becomes invalid (all letters of the target have been bypassed), we break out of the inner loop and go back to moving the end pointer to the right.
'''
def found_target(target_len):
    return target_len == 0

class Solution(object):
    def minWindow(self, search_string, target):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_letter_counts = collections.Counter(target)
        print(target_letter_counts)
        start = 0
        end = 0
        min_window = ""
        target_len = len(target)        
        
        for end in range(len(search_string)):
            
    # If we see a target letter, decrease the total target letter count
            if target_letter_counts[search_string[end]] > 0:
                target_len -= 1

            # Decrease the letter count for the current letter
			# If the letter is not a target letter, the count just becomes -ve
            target_letter_counts[search_string[end]] -= 1
            
			# If all letters in the target are found:
            while found_target(target_len):
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
					# Note the new minimum window
                    min_window = search_string[start : end + 1]
                    
				# Increase the letter count of the current letter
                target_letter_counts[search_string[start]] += 1
                
				# If all target letters have been seen and now, a target letter is seen with count > 0
				# Increase the target length to be found. This will break out of the loop
                if target_letter_counts[search_string[start]] > 0:
                    target_len += 1
                    
                start+=1
                
        return min_window
        