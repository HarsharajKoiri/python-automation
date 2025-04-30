# Day 5 - Password Tool

A Python-based utility to **check the strength of passwords** or **generate strong passwords** with customizable length. This is part of my **Python Automation Journey**.

---

##  Features

-  Check password strength (based on character variety and length)
-  Generate strong passwords (customizable length)
-  Smart feedback on password strength: Very Weak → Very Strong

---

##  Sample Run

### 1. Checking Password Strength

```bash 
Choose (1 or 2): 1
Enter your password: Zoro@123
✅ Strength: 5/5 → Very Strong
```
### 2. Generating a Password
```bash
Choose (1 or 2): 2
Enter desired length: 12
🔑 Generated Password: z8$AbP!1Kr@Q
```

Flow:

          +--------------------------+
          |    Start Tool (Main)     |
          +-----------+--------------+
                      |
          +-----------v------------+
          | 1. Check Strength?     |<----------------+
          | 2. Generate Password?  |                 |
          +-----------+------------+                 |
                      |                              |
          +-----------v------------+         +-------v---------+
          |    Input Password      |         | Input Length    |
          +-----------+------------+         +-------+---------+
                      |                              |
              +-------v---------+        +-----------v-----------+
              | Check rules via |        | Generate random chars |
              | regex & length  |        | using string module   |
              +-------+---------+        +-----------+-----------+
                      |                              |
              +-------v---------+        +-----------v-----------+
              | Print strength  |        | Display generated pwd |
              +-------+---------+        +-----------+-----------+
                      |                              |
                    + v +                          + v +
                    | End |                        | End |
                    +---+                          +---+
