import os
from jinja2 import Environment, FileSystemLoader

def main():
    # Set up the Jinja2 environment and load the template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('prompt_template.j2')

    # Define standard context variables (Few-shot examples)
    few_shot_examples = [
        {"text": "The battery life is amazing, but it gets a bit warm.", "sentiment": "Positive"},
        {"text": "Completely broken out of the box, do not buy.", "sentiment": "Negative"}
    ]

    # Define 3 example inputs (Target Reviews)
    target_reviews = [
        {
            # Example 1: Verified buyer, JSON output request
            "product_category": "Consumer Electronics",
            "output_format": "json",
            "target_review": {
                "title": "Great sound, clunky app",
                "text": "The audio quality of these headphones is top-notch. The noise cancellation works perfectly on airplanes. However, the companion mobile app is very unintuitive and keeps crashing.",
                "rating": 4,
                "is_verified_buyer": True
            }
        },
        {
            # Example 2: Unverified buyer, text output request, missing title
            "product_category": "Home Appliances",
            "output_format": "text",
            "target_review": {
                "title": "", # Testing the default filter in Jinja
                "text": "It blends smoothies okay, but the motor smells like burning plastic when I try to crush ice. I expected better for this price point.",
                "rating": 2,
                "is_verified_buyer": False
            }
        },
        {
            # Example 3: Verified buyer, JSON output request, highly positive
            "product_category": "Fitness Equipment",
            "output_format": "json",
            "target_review": {
                "title": "Sturdy and quiet",
                "text": "Assembly took about an hour but the instructions were clear. The treadmill is incredibly quiet, which is great because I live in an apartment. Highly recommend!",
                "rating": 5,
                "is_verified_buyer": True
            }
        }
    ]

    # Generate and print the prompts
    print("=== GENERATED PROMPTS ===\n")
    for i, data in enumerate(target_reviews, 1):
        # Combine the common few-shot examples with the specific review data
        render_data = {
            "few_shot_examples": few_shot_examples,
            **data
        }
        
        # Render the template
        prompt = template.render(render_data)
        
        print(f"--- Prompt {i} ---")
        print(prompt)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
