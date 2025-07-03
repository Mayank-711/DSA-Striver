'''
────────────────────────────────────────────────────────────
📘 Question: Highest Occurring Element in an Array
💡 Level: Easy
🎯 Task:
    Given an array of `n` integers, find the **most frequent element**.
    If there are multiple with same max frequency, return the **smallest**.

────────────────────────────────────────────────────────────

📥 Examples:

Input : arr = [1, 2, 2, 3, 3, 3]
Output: 3
🧾 Explanation:
    3 occurs 3 times, more than any other number.

Input : arr = [4, 4, 5, 5, 6]
Output: 4
🧾 Explanation:
    4 and 5 both appear twice, but 4 is smaller.

────────────────────────────────────────────────────────────
🧠 Approach Hints:
    ✅ Use a dictionary/hashmap to count frequencies.
    ✅ Traverse dictionary to find:
       - max frequency
       - smallest element with that frequency

📦 Optional Tools:
    - Python’s `collections.Counter`
    - Use `min()` when frequencies are equal

🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''
class Solution:
    def highFrequencies(self, nums):
        # Your code goes here
        n = {}
        for i in nums:
            if i not in n:
                n[i] = 1
            else:
                n[i]+=1
        max_num=(max(n.values()))
        for j in n:
            if n[j]== max_num:
                return j
    
sol = Solution()
# nums = [1, 2, 2, 1, 3]
nums = [5, 5, 5, 5]
print(sol.highFrequencies(nums))