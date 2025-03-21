# Walking Through Unpickling: Understanding Pickle Opcodes, Memo, Stack, and the Pickle Virtual Machine (PVM)

When you unpickle a file in Python, the **Pickle Virtual Machine (PVM)** executes a stack-based deserialization process. Each **opcode** (operation code) tells the PVM what to do, whether it’s creating objects, storing them, or reconstructing a data structure.

---

## **Step-by-Step Unpickling of Pickle Data**

### **1. The Pickle Header**

```plaintext
    0: \x80 PROTO      4
    2: \x95 FRAME      58
```

- `PROTO 4`: Specifies that this Pickle file uses **protocol version 4**. This determines which serialization techniques are allowed.
- `FRAME 58`: Introduced in protocol 4, `FRAME` marks the start of a data frame of **58 bytes**.

---

### **2. Creating an Empty Dictionary**

```plaintext
   11: }    EMPTY_DICT
   12: \x94 MEMOIZE    (as 0)
```

- `EMPTY_DICT`: Pushes an **empty dictionary** onto the stack.
- `MEMOIZE (as 0)`: Stores this dictionary in the **memo table** at index `0`. The memo table helps reconstruct objects that appear multiple times.

At this point, the **stack** looks like:

```plaintext
Stack: [{}]
Memo: {0: {}}
```

---

### **3. Adding Key-Value Pairs to the Dictionary**

```plaintext
   13: (    MARK
   14: \x8c     SHORT_BINUNICODE 'name'
   20: \x94     MEMOIZE    (as 1)
   21: \x8c     SHORT_BINUNICODE 'John'
   27: \x94     MEMOIZE    (as 2)
```

- `MARK`: Acts as a **checkpoint**. This helps when adding multiple items at once.
- `SHORT_BINUNICODE 'name'`: Pushes the **string** onto the stack.
- `MEMOIZE (as 1)`: Stores `"name"` in the memo table.
- `SHORT_BINUNICODE 'John'`: Pushes `"John"` onto the stack.
- `MEMOIZE (as 2)`: Stores `"John"` in the memo table.

Stack now:

```plaintext
Stack: [{}, MARK, "name", "John"]
Memo: {0: {}, 1: "name", 2: "John"}
```

---

### **4. Continuing Key-Value Pairs**

```plaintext
   28: \x8c     SHORT_BINUNICODE 'age'
   33: \x94     MEMOIZE    (as 3)
   34: K        BININT1    30
```

- `"age"` is pushed onto the stack and stored in memo index `3`.
- `BININT1 30`: Pushes the integer **30** onto the stack.

Stack now:

```plaintext
Stack: [{}, MARK, "name", "John", "age", 30]
Memo: {0: {}, 1: "name", 2: "John", 3: "age"}
```

---

### **5. Handling the List**

```plaintext
   36: \x8c     SHORT_BINUNICODE 'courses'
   45: \x94     MEMOIZE    (as 4)
   46: ]        EMPTY_LIST
   47: \x94     MEMOIZE    (as 5)
```

- `"courses"` is pushed and stored in **memo index 4**.
- `EMPTY_LIST`: Pushes an **empty list** onto the stack.
- `MEMOIZE (as 5)`: Stores the list at **memo index 5**.

Stack now:

```plaintext
Stack: [{}, "name", "John", "age", 30, "courses", []]
Memo: {0: {}, 1: "name", 2: "John", 3: "age", 4: "courses", 5: []}
```

---

### **6. Populating the List**

```plaintext
   48: (        MARK
   49: \x8c         SHORT_BINUNICODE 'Math'
   55: \x94         MEMOIZE    (as 6)
   56: \x8c         SHORT_BINUNICODE 'Science'
   65: \x94         MEMOIZE    (as 7)
   66: e            APPENDS    (MARK at 48)
```

- `MARK`: Signals the start of multiple elements being added to a list.
- `"Math"` is pushed and stored in **memo index 6**.
- `"Science"` is pushed and stored in **memo index 7**.
- `APPENDS`: Pops `"Math"` and `"Science"` from the stack and appends them to the list.

Stack now:

```plaintext
Stack: [{}, MARK, "name", "John", "age", 30, "courses", ["Math", "Science"]]
Memo: {0: {}, 1: "name", 2: "John", 3: "age", 4: "courses", 5: ["Math", "Science"], 6: "Math", 7: "Science"}
```

---

### **7. Completing Dictionary Construction**

```plaintext
   67: u        SETITEMS   (MARK at 13)
```

- `SETITEMS`: Pops key-value pairs from the stack and adds them to the dictionary.

Final Dictionary:

```python
{
    "name": "John",
    "age": 30,
    "courses": ["Math", "Science"]
}
```

Stack after `SETITEMS`:

```plaintext
Stack: [{"name": "John", "age": 30, "courses": ["Math", "Science"]}]
Memo: {0: {"name": "John", "age": 30, "courses": ["Math", "Science"]}, ...}
```

---

### **8. Ending the Unpickling Process**

```plaintext
   68: .    STOP
```

- `STOP`: Signals the end of the unpickling process. The final dictionary is returned.

---

## **Summary of Key Concepts**

### **1. The Memo Table**

The memo table stores references to objects to avoid duplication. This is useful for **recursive objects** or **repeated values**.

### **2. The Stack**

Pickle uses a **stack-based execution model**, meaning data is pushed onto the stack and then popped when needed.

### **3. The **(** Opcode**

`MARK` is a **checkpoint** used to collect multiple elements (like a list or dictionary items) before applying an operation.

### **4. Pickle Virtual Machine (PVM)**

The PVM reads opcodes one by one, modifying the stack and memo table until the final object is reconstructed.

---

## **Final Takeaways**

- **Pickle is not just data storage—it’s a mini execution environment.**
- **Unpickling reconstructs objects by executing a sequence of opcodes.**
- **Since Pickle can execute arbitrary code, it’s dangerous to unpickle untrusted data!**

