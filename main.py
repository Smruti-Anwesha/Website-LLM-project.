from planner import plan_website
from generator import generate_code
from executor import save_files

user_prompt = input("Enter website description: ")

layout = plan_website(user_prompt)

html, css = generate_code(layout)

save_files(html, css)

print("Done!")