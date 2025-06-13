# AI platform/Coding environment
For the AI platform I chose Gemini. And I chose Google Colab.

# Diverse prompts
## Prompt 1: What is machine learning? Explain with a sample.
Machine learning (ML) is a subset of artificial intelligence (AI) that empowers computer systems to "learn" from data without being explicitly programmed for every specific task. Instead of providing a rigid set of instructions, you feed an ML model a large amount of data, and it identifies patterns, builds models, and uses those models to make predictions or decisions on new, unseen data.


## Prompt 2: What day it was three days ago
Today is Friday, June 5, 2025.

Here's how to figure out what day it was three days ago:

One day ago: Thursday, June 4, 2025
Two days ago: Wednesday, June 3, 2025
Three days ago: Tuesday, June 2, 2025
Therefore, three days ago was Tuesday.


## Prompt 3: I need a Python code that tells if an integer is a prime or not.
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 測試
num = int(input("輸入一個整數："))
print("是質數" if is_prime(num) else "不是質數")
```
