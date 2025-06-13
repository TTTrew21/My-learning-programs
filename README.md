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
num = int(input("Enter a number:"))
print(True if is_prime(num) else False)
```

## Prompt 4: Translate the following sentence into Traditional Chinese: "The future of artificial intelligence is both exciting and uncertain."
The future of artificial intelligence is both exciting and uncertain.
人工智慧的未來既令人興奮又充滿不確定性。

## Prompt 5: Please act like a math teacher and explain the reason why angle sum of triangle is 180 degrees.
Alright class, settle down, settle down! Today, we're going to tackle one of the most fundamental and beautiful truths in geometry: Why the angles inside any triangle always add up to exactly 180 degrees!

Now, I know some of you might just take this as a given, a rule you memorize. But as good mathematicians, we don't just accept rules; we seek to understand why they are true. And luckily, the reason for this 180-degree sum is quite elegant and easy to see.

Step 1: Draw your triangle.
Go ahead and sketch any triangle on your paper. Doesn't matter if it's scalene, isosceles, or equilateral, acute or obtuse. Just a good old triangle. Label its angles A, B, and C.

(Imagine me drawing a triangle on the board, labeling the angles)

Step 2: Draw a line parallel to one of the sides.
Now, this is the crucial step. Pick any one of the triangle's sides. Let's choose side BC. Now, draw a straight line through the opposite vertex (which is A in our case), and make sure this new line is parallel to BC.

...

And there you have it! We've just proven, using a simple construction and the properties of parallel lines, that the sum of the interior angles of any triangle is always 180 degrees.

This isn't just a rule to memorize; it's a logical consequence of how lines behave in Euclidean space. It's a fundamental building block for so much of geometry and trigonometry.

Any questions, class? This proof is really elegant because it shows how different geometric concepts are interconnected!

# Conclusion
## Result:
* I tested 5 prompts including the knowledges of programming, math, role play.
* The model answered me so detailed that I could understand easily.
