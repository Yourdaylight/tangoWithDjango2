import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"BASE_DIR: {BASE_DIR}")
joined_path = os.path.join(BASE_DIR, 'test.py')
print(f"Joined path: {joined_path}")