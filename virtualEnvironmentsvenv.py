# Topic of the Day: Virtual Environments (venv)
# Explanation: When you work on multiple projects, you don't want them interfering with each other (e.g., Project A needs Pandas 1.0, Project B needs Pandas 2.0).
# A Virtual Environment is a self-contained folder that holds a specific version of Python and libraries for one project.

# 1. Create the environment (named 'venv')
# Run this in your project folder
# python -m venv venv

# 2. Activate the environment
# Windows:
# venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# (You will see (venv) appear in your terminal prompt)

# 3. Install packages safely
# pip install pandas

# 4. Deactivate when done
# deactivate