import os

def read_code(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def compress_code(code):
    """
    Simulates LLM-based context compression.
    """
    prompt = f"""
You are an AI documentation agent.

Task:
Compress the following code while preserving:
- core functionality
- important classes and relationships
- overall system purpose

Return a concise semantic summary.

Code:
{code}
"""

    # Simulated LLM response
    compressed_summary = (
        "The code implements a student management system consisting of Student "
        "and Course entities. Students can enroll in or drop courses, while "
        "courses maintain enrolled student lists. A central management system "
        "coordinates creation and enrollment operations."
    )

    return compressed_summary


def generate_documentation(summary):
    return f"""
## Module Overview
{summary}

## Key Components
- Student: Stores student data and enrolled courses
- Course: Stores course metadata and enrolled students
- StudentManagementSystem: Coordinates students and courses

## Usage
Use this system to add students, create courses, and manage enrollments.
""".strip()

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    code_path = os.path.join(base_dir, "sample_code", "project.py")

    print("DEBUG → Looking for:", code_path)

    raw_code = read_code(code_path)
    summary = compress_code(raw_code)
    docs = generate_documentation(summary)

    print("\n=== GENERATED DOCUMENTATION ===\n")
    print(docs)

if __name__ == "__main__":
    main()
