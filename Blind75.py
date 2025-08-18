# Blind 75
from collections import defaultdict
from typing import List


# Contains Duplicates
# given an array of numbers if there is a duplicate in the array of numbers return True
# if the array once has the same number once and we have gone through out all the array
# then we will return false
class Duplicates:
    def hasDuplicates(self, nums: List[int]) -> bool:

        hashset = set()  # we are making this hashset to put in the numbers in the array
        for (
            n
        ) in nums:  # we are going throught each number of the array and checking them
            if n in hashset:  # if the number is already then we founf a duplicate
                return True  # therefore return true
            hashset.add(
                n
            )  # if its not in the hashset then we add it on and we go back around to complet going through the array
        return False  # once the array has been completed and there is no repetition in the array return false


solution = Duplicates()

test_case_1 = [1, 2, 3, 4]
test_case_2 = [5, 6, 6, 7, 10]


print(f"Testing {test_case_1}:{solution.hasDuplicates(test_case_1)}")
print(f"Testing {test_case_2}:{solution.hasDuplicates(test_case_2)}")


# Valid Anagram
# Given two strings s and t return true if the two strings are anagrams of each other. otherwise return false


class Anagram:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(
            t
        ):  # This is a pre-condition check to make sure they are the same lenght
            return False  # if they are not the same len then return false

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


result = Anagram()


# Test cases
s1, t1 = "racecar", "carrace"

# Printing Results
print(f"Is'{s1}' the anagram to '{t1}'? ->{result.isAnagram(s1,t1)}")


# Two sum is going throught an array and finding two numbers that equal to the target
# we return the index to the numbers in the array
class Sum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i, n in enumerate(
            nums
        ):  # enumerate makes a tuple and puts all the intergers in n and gives them an index number
            diff = (
                target - n
            )  # we whant to know the difference between the target and n
            if (
                diff in num_to_index
            ):  # if the difference between both numbers is in the dictionary num_to_index then we want to return both index
                return [
                    num_to_index[diff],
                    i,
                ]  # this returns the difference number and the index associated with it both
            num_to_index[n] = (
                i  # n becomes the key in the dictionary and i becomes the value associated with the key
            )
            # num_to_index acts like a memoization step


two_summer = Sum()


test_cases = [([2, 7, 11, 15], 9)]

print("Tests")
for nums, target in test_cases:
    actual_output = two_summer.twoSum(nums, target)

    print(f"\nInputs: nums{nums},target{target}")
    print(f"Output:{actual_output}")
print("\n Test completed")

# Group Anagram
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order


class GroupAnagram:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # automatically creates a key if the key doesnt exists
        for s in strs:
            count = [0] * 26  # This is to count each letter of the alphabet
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())


grouper = GroupAnagram()  # making an instance of the class

testing = [["eat", "tea", "ate", "bat", "sat"]]

for strs in testing:
    output = grouper.groupAnagrams(strs)

    print(f"Output:{output}")
