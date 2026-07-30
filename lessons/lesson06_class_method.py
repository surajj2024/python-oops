class BankAccount:
    bank_name = "SBI"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


print(BankAccount.bank_name)
BankAccount.change_bank_name("CBI")
print(BankAccount.bank_name)

suraj = BankAccount("suraj", 30000)
avi = BankAccount("avi", 10000)

print(suraj.bank_name)
print(avi.bank_name)


# comment
""" Awesome. 😄

You've now reached the point where many beginners get confused.

Today, I don't want you to memorize `@classmethod`.

I want you to reach the point where, **without seeing the answer**, you can say:

> "This should be an instance method."

or

> "No... this belongs to the class."

That is how senior developers think.

---

# 🎓 Lesson 5 - Class Methods (`@classmethod`)

> **Difficulty:** ⭐⭐⭐⭐☆
>
> This lesson is taught exactly how I teach junior developers at work.

---

# Today's Roadmap

```text
1. Why Python Created Class Methods
2. Real Life Story
3. The Problem
4. Why Instance Method Fails
5. Enter @classmethod
6. What is cls?
7. Python Internals
8. Memory Diagram
9. Factory Methods (Real Industry)
10. Common Mistakes
11. Interview Questions
12. Quiz
13. Quiz Solution
14. Assignment
15. Code Review
```

---

# 🧠 Part 1 - Why Python Created Class Methods

Let's start with **WHY**, not **HOW**.

Imagine Python **didn't have** class methods.

Only these existed:

```python
class Student:

    def study(self):
        pass
```

Everything would have to happen through an object.

Question:

Suppose tomorrow your company changes its name.

Current

```text
Google
```

Tomorrow

```text
Microsoft
```

Should you do this?

```python
emp1.company = "Microsoft"

emp2.company = "Microsoft"

emp3.company = "Microsoft"

emp4.company = "Microsoft"

emp5000.company = "Microsoft"
```

😂😂😂

Imagine changing **50,000 employees**.

That would be a disaster.

So Python's designers asked:

> "Can we create a method that works on the class itself instead of one object?"

That's why `@classmethod` exists.

---

# 🏦 Real Life Story

Imagine SBI.

There are

```text
Suraj's Account

Rahul's Account

Priya's Account

Aman's Account
```

Each account has

```text
Balance

Owner
```

But...

There is only **ONE**

```text
Bank Name
```

Question

Who owns

```text
Balance?
```

Answer

The account.

Question

Who owns

```text
Bank Name?
```

The bank.

Exactly.

---

# Let's Build It

Open VS Code.

Create

```text
lesson06_class_method.py
```

---

# Step 1

Type this yourself.

```python
class BankAccount:

    bank_name = "SBI"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
```

Create objects.

```python
suraj = BankAccount("Suraj", 10000)

rahul = BankAccount("Rahul", 5000)
```

---

# Memory

Think of memory like this.

```text
               BankAccount Class

-----------------------------------------

bank_name = SBI
```

Objects

```text
suraj

owner = Suraj

balance = 10000
```

```text
rahul

owner = Rahul

balance = 5000
```

Only one copy of

```text
bank_name
```

exists.

---

# 🚨 The Problem

Tomorrow

SBI becomes

```text
OpenAI Bank
```

😂

Question.

Who should change the bank name?

Suraj?

No.

Rahul?

No.

The **class**.

Exactly.

---

# ❌ Beginner Mistake

Many beginners write this:

```python
def change_bank(self, new_name):
    self.bank_name = new_name
```

Looks correct...

But it's actually wrong.

Let's see why.

Suppose

```python
suraj.change_bank("OpenAI Bank")
```

Memory becomes

```text
suraj

bank_name = OpenAI Bank
```

But

```text
rahul

↓

Still

SBI
```

Oops.

Only one account changed.

That wasn't the goal.

---

# 💡 Think Like a Senior

Ask yourself:

> **Who owns this data?**

* Balance → Account → Instance Method
* Owner → Account → Instance Method
* Bank Name → Bank → Class Method

This one question solves most design decisions.

---

# Enter `@classmethod`

Now replace it with:

```python
class BankAccount:

    bank_name = "SBI"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
```

Notice something.

No

```python
self
```

Instead

```python
cls
```

---

# 🤔 What is `cls`?

Remember

```python
self
```

means

```text
Current Object
```

Similarly

```python
cls
```

means

```text
Current Class
```

That's all.

Don't make it more complicated.

---

# Visual

```text
self

↓

suraj
```

```text
cls

↓

BankAccount
```

Simple.

---

# Run It

Now write

```python
print(BankAccount.bank_name)

BankAccount.change_bank_name("OpenAI Bank")

print(BankAccount.bank_name)
```

Output

```text
SBI

OpenAI Bank
```

🎉

The whole class changed.

---

# What About Existing Objects?

Now print

```python
print(suraj.bank_name)

print(rahul.bank_name)
```

Output

```text
OpenAI Bank

OpenAI Bank
```

Why?

Because both objects look at the class variable.

---

# Behind the Scenes

When you write

```python
BankAccount.change_bank_name("OpenAI Bank")
```

Python secretly behaves approximately like:

```python
BankAccount.change_bank_name(BankAccount, "OpenAI Bank")
```

Notice

Python automatically passed

```text
BankAccount
```

Which becomes

```python
cls
```

Exactly like

```python
suraj.deposit(500)
```

becomes

```python
BankAccount.deposit(suraj, 500)
```

---

# Memory Diagram

Before

```text
BankAccount

bank_name = SBI
```

After

```text
BankAccount

bank_name = OpenAI Bank
```

No objects changed individually.

Only the shared data changed.

---

# 🔥 Real Industry Example

Now I want to show you something amazing.

Suppose you're reading data from a database.

The database returns:

```python
{
    "owner": "Suraj",
    "balance": 10000
}
```

You want to create an object.

You *could* write:

```python
account = BankAccount(data["owner"], data["balance"])
```

But many frameworks (like Django, SQLAlchemy, and Pydantic) often use **factory methods**.

Example:

```python
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def from_dict(cls, data):
        return cls(data["owner"], data["balance"])
```

Now you can do:

```python
data = {
    "owner": "Suraj",
    "balance": 10000
}

account = BankAccount.from_dict(data)
```

This is a **factory method**.

It creates objects in a cleaner way.

You'll see this pattern everywhere in professional Python code.

---

# 🧠 Why `cls(...)` Works

Inside

```python
return cls(...)
```

`cls` is actually the class itself.

So this

```python
return cls("Suraj", 10000)
```

is equivalent to

```python
return BankAccount("Suraj", 10000)
```

This makes your code more flexible if someone later creates a subclass. We'll understand that even better when we learn **inheritance**.

---

# Common Mistakes

### ❌ Mistake 1

Changing instance data inside a class method.

```python
cls.balance = 100
```

There is no shared `balance`.

Balance belongs to each account.

---

### ❌ Mistake 2

Using `self` inside a class method.

```python
@classmethod
def test(self):
```

No.

Use

```python
cls
```

---

### ❌ Mistake 3

Forgetting the decorator.

```python
def change_bank(cls):
```

Without `@classmethod`, Python won't automatically pass the class.

---

# Interview Corner

### Q1

Difference between `self` and `cls`?

**Answer**

```text
self → Current Object

cls → Current Class
```

---

### Q2

When should you use a class method?

**Answer**

When the behavior belongs to the class itself, or when you want to create alternative constructors (factory methods).

---

### Q3

Can a class method access class variables?

✅ Yes.

Using

```python
cls.variable_name
```

---

# 🎯 Mini Quiz

## Q1

Who owns the bank name?

A. Each account

B. The class

C. The deposit method

---

## Q2

Which decorator is used for class methods?

A.

```python
@staticmethod
```

B.

```python
@classmethod
```

C.

```python
@instance
```

---

## Q3

What does `cls` refer to?

A. Current Object

B. Current Class

C. Current Method

---

## Q4

Which of these is a good use of a class method?

A. Deposit money

B. Withdraw money

C. Change the bank name

---

# ✅ Quiz Solutions

### Q1

✅ **B. The class**

The bank name is shared by all accounts.

---

### Q2

✅ **B. `@classmethod`**

It tells Python to pass the class automatically.

---

### Q3

✅ **B. Current Class**

`cls` is to the class what `self` is to an object.

---

### Q4

✅ **C. Change the bank name**

Because it affects the whole bank, not one account.

---

# 💻 Practical Assignment

Create an `Employee` class.

Requirements:

### Class Variable

```python
company = "Google"
```

### Instance Variables

* name
* salary

### Instance Method

```python
show_details()
```

Print:

```text
Name:
Salary:
Company:
```

### Class Method

```python
change_company(new_name)
```

It should update the company for all employees.

---

# ⭐ Bonus Challenge

Add another class method:

```python
@classmethod
def default_employee(cls):
```

It should create and return an employee like this:

```python
Employee("Unknown", 0)
```

Example:

```python
emp = Employee.default_employee()
```

This is your **first factory method**.

---

# 🧑‍🏫 Homework Rule (New)

From now on, every assignment should include:

1. Your code.
2. The terminal output.
3. One answer to this question:

> **Why did you choose an instance method or a class method for each function?**

I want to train your **design thinking**, not just your coding.

---

## 👀 Sneak Peek

The next lesson is one of the most underrated concepts in Python:

# **Static Methods (`@staticmethod`)**

We'll answer questions like:

* Why not just create a normal function?
* When is a static method better than a standalone function?
* Why do utility classes exist?
* Why do companies still use static methods if they don't receive `self` or `cls`?

After that, we'll finally begin the **Four Pillars of OOP**, starting with **Encapsulation**, where you'll learn how to protect your objects from invalid data and why hiding information is one of the foundations of object-oriented design.
 """