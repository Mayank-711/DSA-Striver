'''
────────────────────────────────────────────────────────────
📘 PATTERN PRINTING (Striver's A-Z DSA Sheet)
💡 Level: Easy
🎯 Description:
    These functions implement different pattern printing problems.
    Use `n` as input to control the number of rows/columns in each pattern.

🧩 Pattern Descriptions:

1️⃣ pattern1 - Solid Square Star Pattern
   *****
   *****
   *****
   *****

2️⃣ pattern2 - Right-Angled Triangle Star Pattern
   *
   **
   ***

3️⃣ pattern3 - Right-Angled Triangle with Increasing Numbers
   1
   1 2
   1 2 3

4️⃣ pattern4 - Right-Angled Triangle with Repeating Row Numbers
   1
   2 2
   3 3 3

5️⃣ pattern5 - Inverted Right-Angled Star Triangle
   *****
   ****
   ***
   **

6️⃣ pattern6 - Inverted Number Triangle
   1 2 3 4
   1 2 3
   1 2

7️⃣ pattern7 - Pyramid Star Pattern
     *
    ***
   *****

8️⃣ pattern8 - Inverted Pyramid Star Pattern
   *****
    ***
     *

9️⃣ pattern9 - Diamond Star Pattern (Pyramid + Inverted Pyramid)

🔟 pattern10 - Full Star Triangle (increasing then decreasing)
   *
   **
   ***
   **
   *

1️⃣1️⃣ pattern11 - 0-1 Triangle
   1
   0 1
   1 0 1

1️⃣2️⃣ pattern12 - Number + Space + Reverse Number
   1     1
   12   21
   123 321

1️⃣3️⃣ pattern13 - Number Triangle (Continuous Counting)
   1
   2 3
   4 5 6

1️⃣4️⃣ pattern14 - Alphabet Triangle (Increasing)
   A
   A B
   A B C

1️⃣5️⃣ pattern15 - Alphabet Triangle (Decreasing Rows)
   A B C
   A B
   A

1️⃣6️⃣ pattern16 - Repeating Alphabet Row
   A
   B B
   C C C

1️⃣7️⃣ pattern17 - Palindromic Alphabet Pyramid
     A
    ABA
   ABCBA

1️⃣8️⃣ pattern18 - Reverse Alphabet Triangle
   E
   D E
   C D E

1️⃣9️⃣ pattern19 - Butterfly Pattern

2️⃣0️⃣ pattern20 - Symmetric Hourglass Stars

2️⃣1️⃣ pattern21 - Hollow Square Star Pattern
   *****
   *   *
   *****

2️⃣2️⃣ pattern22 - Number Spiral Square
   4444444
   4333334
   4322234
   4321234
   4322234
   4333334
   4444444

📌 Usage:
- Uncomment the desired pattern function in `main()` to test.
- Input: An integer `n` from user.
────────────────────────────────────────────────────────────
'''

class Solution:
    def pattern1(self,n):
        for i in range(n):
            print(n*"*")
        return None
    
    def pattern2(self,n):
        for i in range(n):
            print(i*'*')
        return None
    
    def pattern3(self,n):
        for i in range(1,n+1):
            for j in range(1,i):
                print(j,end='')
            print()
        print()    
        return None

    def pattern5(self,n):
        for i in range(n,0,-1):
            print(i*'*')
        return None
        
    def pattern4(self,n):
        for i in range(n):
            for j in range(i):
                print(i,end='')
            print()
        print()

    def pattern6(self,n):
        for i in range(n,0,-1):
            for j in range(i,0,-1):
                print(j ," ",end='')
            print()
    
    def pattern7(self,n):
        for i in range(1,n,2):
            spaces = n - i//2
            print(' '* spaces +  '*' * i)
    
    def pattern8(self,n):
        for i in range(n,0,-2):
            spaces = n - i//2
            print(' '*spaces + '*' * i)

    def pattern9(self,n):
        def p7(n):
            for i in range(1,n,2):
                spaces = n - i//2
                print(' '* spaces +  '*' * i)

        def p8(n):
            for i in range(n,0,-2):
                spaces = n - i//2
                print(' '*spaces + '*' * i)
        p7(n)
        p8(n)
    
    def pattern10(self,n):
        for i in range(n):
            print(i*'*')
        for j in range(i-1,0,-1):
            print(j*'*')
    
    def pattern11(self,n):
        for i in range(n):
            start = 1 if i %2 == 0 else 0
            for j in range (i):
                print(start,end='')
                start = 1 - start
            print()
        print()

    def pattern12(self,n):
        for i in range(1,n+1):
            spaces = n*2 - i*2
            for j in range(1,i+1):
                print(j,end='')
            print(' '* spaces,end='')
            for k in range(i,0,-1):
                print(k,end='')
            print()
    
    def pattern13(self,n):
        no = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(no,end='')
                no+=1
            print()
        print()

    def pattern14(self,n):
        for i in range(n):
            for ch in range(ord('A'),ord('A')+ i+1):
                print(chr(ch),end='')
            print()
    
    def pattern15(self,n):
        for i in range(n,1,-1):
            for ch in range(ord('A'),ord('A')+i - 1):
                print(chr(ch),end='')
            print()
    
    def pattern16(self,n):
        ch = ord('A') -1
        for i in range(n):
            print(chr(ch) * i)
            ch +=1
    
    def pattern17(self,n):
        for i in range(n):
            spaces = n - i -1
            print(' '*spaces,end='')
            ch= ord('A')
            for j in range(i +1):
                print(chr(ch+j),end='')
            for k in range(i-1,-1,-1):
                print(chr(ch+k),end='')
            print()
        print()

    def pattern18(self,n):
        for i in range(n):
            ch = ord('A')+n
            for j in range(i+1):
                print(chr(ch),end='')
                ch -=1
            print()
            ch = ord('A')+n
    
    def pattern19(self,n):
        for i in range(n):
            spaces = n-i*2 + n
            print('*'*i + ' '*spaces + '*'*i)
        for j in range(i,0,-1):
            spaces = n - j*2 +n
            print('*'*j + ' '*spaces + '*'*j)


    def pattern20(self,n):
        for i in range(n,0,-1):
            spaces = n - i*2 + n 
            print('*'*i+ ' '*spaces ,'*'*i)
        for j in range(n+1):
            spaces = n-j*2 + n
            print('*'*j + ' '*spaces + '*'*j)

    
    def pattern21(self,n):
        print('*'*n)
        for i in range(n+1):
            spaces = n -2
            print('*'+' '*spaces+'*')
        print('*'*n)

    def pattern22(self, n):
        size = 2 * n - 1
        for i in range(size):
            for j in range(size):
                top = i
                left = j
                right = size - 1 - j
                bottom = size - 1 - i
                min_dist = min(top, left, right, bottom)
                print(n - min_dist, end='')
            print()

        

sol = Solution()
sol.pattern1(4)
sol.pattern2(4)
sol.pattern3(4)
sol.pattern4(4)
sol.pattern5(4)
sol.pattern6(4)
sol.pattern7(9)
sol.pattern8(9)
sol.pattern9(7)
sol.pattern10(5)
sol.pattern11(7)
sol.pattern12(5)
sol.pattern13(4)
sol.pattern14(4)
sol.pattern15(5)
sol.pattern16(5)
sol.pattern17(6)
sol.pattern18(7)
sol.pattern19(5)
sol.pattern20(5)
sol.pattern21(5)
sol.pattern22(5)