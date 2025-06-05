Absolutely! Below is the **full Markdown version** of all answers to **Lab 07**, covering probability, Bayes' theorem, joint distributions, and independence.

---

# 🧪 Lab 07 – Probability Questions (Markdown Answers)

---

## **1. Test A vs. Test B – Which test is more reliable?**

We apply **Bayes' Theorem**:

$$
P(\text{Virus} \mid \text{Positive}) = \frac{P(\text{Positive} \mid \text{Virus}) \cdot P(\text{Virus})}{P(\text{Positive})}
$$

### **Given:**

|                     | Test A     | Test B     |
| ------------------- | ---------- | ---------- |
| Sensitivity         | 95% (0.95) | 90% (0.90) |
| False Positive Rate | 10% (0.10) | 5% (0.05)  |
| Virus prevalence    | 1% (0.01)  | 1% (0.01)  |

### **Calculations:**

**Test A:**

$$
P(+A) = (0.95)(0.01) + (0.10)(0.99) = 0.0095 + 0.099 = 0.1085
$$

$$
P(V \mid +A) = \frac{0.95 \cdot 0.01}{0.1085} \approx \boxed{0.0876}
$$

**Test B:**

$$
P(+B) = (0.90)(0.01) + (0.05)(0.99) = 0.009 + 0.0495 = 0.0585
$$

$$
P(V \mid +B) = \frac{0.90 \cdot 0.01}{0.0585} \approx \boxed{0.1538}
$$

### ✅ **Conclusion:**

Test **B** is more reliable when testing positive (PPV ≈ 15.38%) vs. Test A (≈ 8.76%) because it has a lower false positive rate.

---

## **2. Rare Disease with 99% Accurate Test**

- Disease prevalence: 1 in 10,000 → $P(D) = 0.0001$
- Accuracy: $P(+|D) = 0.99$, $P(+|\neg D) = 0.01$

$$
P(+) = (0.99)(0.0001) + (0.01)(0.9999) = 0.000099 + 0.009999 = 0.010098
$$

$$
P(D \mid +) = \frac{0.99 \cdot 0.0001}{0.010098} \approx \boxed{0.0098 \text{ or } 0.98\%}
$$

### ✅ **Conclusion:**

Even with a 99% accurate test, if the disease is rare, **most positives will be false positives**.
That's why it's "good news" that the disease is rare.

---

## **3. Is it rational: P(A) = 0.4, P(B) = 0.3, P(A ∨ B) = 0.5?**

We use:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\Rightarrow 0.5 = 0.4 + 0.3 - P(A \cap B)
\Rightarrow P(A \cap B) = 0.2
$$

Since $0 \leq P(A \cap B) \leq \min(P(A), P(B))$, this is **rational**.

### ✅ **Conclusion:**

Yes, these probabilities are valid.

**Range of rational values for** $P(A \cap B)$:

$$
[0, \min(0.4, 0.3)] = [0, 0.3]
$$

---

## **4. Is it rational: P(A) = 0.4, P(B) = 0.3, P(A ∨ B) = 0.7?**

$$
P(A \cup B) = 0.4 + 0.3 - P(A \cap B) = 0.7
\Rightarrow P(A \cap B) = 0
$$

### ✅ **Conclusion:**

Yes, this is rational. It implies:

$$
P(A \cap B) = 0 \Rightarrow A \text{ and } B \text{ are mutually exclusive}
$$

---

## **5. Full Joint Distribution (Toothache, Cavity, Catch)**

Assumed table:

| Toothache | Cavity | Catch | P     |
| --------- | ------ | ----- | ----- |
| T         | T      | T     | 0.108 |
| T         | T      | F     | 0.012 |
| F         | T      | T     | 0.072 |
| F         | T      | F     | 0.008 |
| T         | F      | T     | 0.016 |
| T         | F      | F     | 0.064 |
| F         | F      | T     | 0.144 |
| F         | F      | F     | 0.576 |

### ✅ Computed Results

```markdown
| Query                          | Result |
| ------------------------------ | ------ |
| P(toothache)                   | 0.20   |
| P(cavity)                      | 0.20   |
| P(toothache ∧ cavity)          | 0.12   |
| P(toothache ∨ cavity)          | 0.28   |
| P(toothache \| cavity)         | 0.60   |
| P(cavity \| toothache ∧ catch) | 0.871  |
| P(toothache \| cavity ∧ catch) | 0.60   |
| Toothache ⫫ Catch \| Cavity?   | Yes ✅ |
```

### 📘 Explanation of Conditional Independence:

Toothache is **conditionally independent** of Catch given Cavity because:

$$
P(toothache \mid cavity, catch) = P(toothache \mid cavity) = 0.6
$$

Knowing whether there's a catch **adds no extra info** once we know the patient has a cavity.

---

Let me know if you'd like this converted to PDF or included in a report-style document.
