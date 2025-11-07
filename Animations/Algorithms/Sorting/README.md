# 🌀 Sorting Algorithm Visualizer

An interactive **Sorting Visualizer** built with pure **HTML, CSS, and JavaScript**, designed to help anyone understand how sorting algorithms work step-by-step — visually, intuitively, and with explanations in plain English.

---

[![View Demo](https://img.shields.io/badge/View-Live%20Demo-blue?style=for-the-badge&logo=github)](https://vkmathew.github.io/sorting-visualizer/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#license)

*(Click the blue button above to open the live demo once hosted via GitHub Pages.)*

---

## 🎨 Features

- Visualizes multiple algorithms:
  - Bubble Sort  
  - Insertion Sort  
  - Merge Sort  
  - Quick Sort  
  - Heap Sort  
- Adjustable **array size** and **animation speed**
- Shuffle and stop controls
- Explanations include:
  - Algorithm logic and intuition  
  - Big O notation explained with real-world analogies  
  - Performance, stability, and memory characteristics  
- Works fully **offline**
- Built for clarity, learning, and simplicity

---

## 🧠 How It Works

Each algorithm is implemented as an **asynchronous JavaScript function**, allowing smooth real-time animation of comparisons and swaps.  
The bars represent array elements, and their movement reflects how the algorithm reorders data internally.

The app dynamically updates an **information panel** below the animation to explain:
- The algorithm’s step-by-step theory
- Its time and space complexity (Big O)
- Real-world use cases and analogies

---

## 🚀 Getting Started

### Option 1 — Run Locally (Offline)

1. Clone or download this repository:
   ```bash
   git clone https://github.com/vkmathew/sorting-visualizer.git
   cd sorting-visualizer
2. Open the file:
sorting_visualizer.html

Option 2 — View Online (GitHub Pages)

Once deployed, access it at:
👉 https://vkmathew.github.io/sorting-visualizer/

To publish:

Go to Settings → Pages in your GitHub repo.

Choose:

Source: Deploy from branch

Branch: main

Folder: / (root)

Save — the site will be live in 30–60 seconds.




🧮 Big O Notation Overview

Big O notation describes how an algorithm’s time or space usage grows with input size (n).
It focuses on the rate of growth, not actual runtime.

Example:
If Bubble Sort takes 1 second for 100 elements (O(n²)), it’ll take roughly 4 seconds for 200 elements because 200² is 4× larger than 100².
In contrast, Merge Sort (O(n log n)) would only take about 2.3 seconds — showing why efficiency matters at scale.

📊 Performance Summary
Algorithm	Best Case	Average Case	Worst Case	Space	Stability	Real-world Use
Bubble	O(n)	O(n²)	O(n²)	O(1)	✅ Stable	Educational purposes
Insertion	O(n)	O(n²)	O(n²)	O(1)	✅ Stable	Small/natural datasets
Merge	O(n log n)	O(n log n)	O(n log n)	O(n)	✅ Stable	External sorting
Quick	O(n log n)	O(n log n)	O(n²)	O(log n)	❌ Not stable	In-memory sort
Heap	O(n log n)	O(n log n)	O(n log n)	O(1)	❌ Not stable	Priority queues
🧑‍💻 Author

Vinu Mathew
Principal Systems Development Engineer @ Dell Technologies
Driven by curiosity, clarity, and the joy of turning complex systems into simple visuals.

📫 LinkedIn
💻 GitHub