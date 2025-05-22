# 🧮 Bubble Sort Visualizer (Python)

This project contains **two Python scripts** that demonstrate the **Bubble Sort** algorithm with step-by-step visual output in the terminal. Both scripts sort a list of integers in ascending order and print the internal comparisons for each sorting pass.

---

## 📜 Versions

### 1. `Bubblesort(nsp).py`
- Accepts **a single string of digits without spaces** (e.g., `723691485`).
- Converts each character to an integer before sorting.
- Best suited for quick digit-based sorting demonstrations.

### 2. `Bubblesort(wsp).py`
- Accepts **a list of numbers separated by spaces** (e.g., `72 36 91 48 5`).
- Converts the input into a list of integers using `split()` and `map()`.
- More user-friendly for standard number lists.

---

## 🔍 Features

- Step-by-step visualization of:
  - Indexes being compared.
  - Swaps made (if any).
  - Output of the array after each pass.
- Early stopping if the array becomes sorted before completing all passes.
- Uses clear print statements for educational purposes.

---

## ▶️ How to Use

1. Open your terminal.
2. Run either script using Python:

```bash
python bubblesort_nospace.py
# or
python bubblesort_withspace.py
```

3. Enter your input when prompted:
   - **For `nospace` version:** type digits without spaces (e.g., `91243`)
   - **For `withspace` version:** type numbers separated by spaces (e.g., `91 24 3`)

---

## 📦 Sample Output (withspace version)

```
Masukkan angka-angka yang ingin diurutkan (pisahkan dengan spasi): 5 3 8 2
Langkah 1:
  Membandingkan indeks 0 dan 1: [3, 5, 8, 2]
  Membandingkan indeks 1 dan 2: [3, 5, 8, 2]
  Membandingkan indeks 2 dan 3: [3, 5, 2, 8]
  Hasil setelah Langkah 1: [3, 5, 2, 8]

Langkah 2:
  Membandingkan indeks 0 dan 1: [3, 5, 2, 8]
  Membandingkan indeks 1 dan 2: [3, 2, 5, 8]
  Membandingkan indeks 2 dan 3: [3, 2, 5, 8]
  Hasil setelah Langkah 2: [3, 2, 5, 8]
...
```

---

## 🧠 Educational Purpose

These scripts are designed for **beginners learning sorting algorithms**. They allow you to:
- Observe how Bubble Sort works internally.
- Understand the concept of comparing adjacent elements.
- Learn about optimization with early exit (`tukar` flag).
