# ANLP_Jinja_Task (Dynamic Prompt Generation for Product Review Classification)

## 1. The Task/Domain
The domain of this project is **E-commerce Product Review Classification**. The objective is to dynamically generate structured prompts for a Large Language Model (LLM) to analyze customer reviews, classify their sentiment (Positive, Neutral, Negative), and extract key product features. 

## 2. What the Jinja Template Does
The Jinja template (`prompt_template.j2`) acts as a flexible blueprint for the LLM prompt. It dynamically:
* Injects the specific product category into the system instructions.
* Toggles the requested output format (JSON vs. Bullet points) using an `if/else` statement.
* Iterates over a list of historical few-shot examples using a `for` loop, dynamically creating the few-shot context.
* Uses the `default()` filter to handle missing review titles gracefully.
* Injects conditional system notes based on metadata (e.g., whether the reviewer is a "verified buyer").

## 3. Why Jinja is Appropriate for this Problem
Jinja is vastly superior to simple Python f-strings or string concatenation for this NLP task. Building this prompt with standard Python string formatting would result in a messy, hard-to-maintain script filled with conditional `if` blocks and loop concatenations just to build a single text string. 

Specifically, Jinja natively handles:
1. **Loops (`{% for %}`):** Easily injecting a variable number of few-shot examples without needing an external string builder loop in Python.
2. **Conditional Logic (`{% if %}`):** Cleanly swapping out entire paragraphs of instructions based on variables like `output_format` or `is_verified_buyer`.
3. **Graceful Fallbacks (`| default()`):** Handling missing data (like an empty review title) directly in the presentation layer without needing extra Python logic.

By separating the prompt structure (Jinja) from the data processing (Python script), the prompt engineering process becomes much more readable, modular, and maintainable.