'''
────────────────────────────────────────────────────────────
📘 Question: Counting Frequencies of Array Elements
💡 Level: Easy
🎯 Task:
    Given an array `nums` of size `n` (may contain duplicates),
    return a list of pairs [element, frequency].

📖 Details:
    • Each element must appear only once in the output.
    • You may return the result in any order.

────────────────────────────────────────────────────────────

📥 Examples:

Input : nums = [1, 2, 2, 1, 3]
Output: [[1, 2], [2, 2], [3, 1]]
🧾 Explanation:
    - 1 → 2 times
    - 2 → 2 times
    - 3 → 1 time

Input : nums = [5, 5, 5, 5]
Output: [[5, 4]]
🧾 Explanation:
    - 5 → 4 times

────────────────────────────────────────────────────────────
🧠 Hints:
    ✅ Use dictionary/hashmap to count frequencies.
    ✅ You can use `collections.Counter` in Python.
    ✅ Loop through array and update counts manually if needed.

🛠️ Printing Syntax Reminder:
    • C++    : cout << variable_name;
    • Java   : System.out.print(variable_name);
    • Python : print(variable_name)
    • JS     : console.log(variable_name)
────────────────────────────────────────────────────────────
'''


class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        n = {}
        ans=[]
        for i in nums:
            if i not in n:
                n[i] = 1
            else:
                n[i]+=1
        for j in n:
            ans.append([j,n[j]])
        return ans

sol = Solution()
# nums = [1, 2, 2, 1, 3]
nums = [5, 5, 5, 5]
print(sol.countFrequencies(nums))