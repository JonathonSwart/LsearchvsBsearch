# LsearchvsBsearch
Increases the length of an array until binary search algorithm is faster than linear search algorithm

# How to run it
The test code is built into the main part of the script. So by opening up the code and running it will output the sizes of the k list where binary search is faster.

# How it works
It creates a big list that the search algorithms have to search through and a small list with values that the search algorithms have to check for in the big list. The small list increases each time linear search runs faster. My code checks how long it takes for linear search to check all the values in the small list and then compares it to how long it takes for the binary search to check all the values in the small list. The size of the small list increases until the binary search checks all the values quicker than the linear search does. The small list tries to have half its values in the big list and half that are not in the big list. But when the list is at an odd size it will have one more value that is not in the big list. Once the small list is big enough where binary search checks all values quicker than linear search the code will terminate and output the size of the small list.
