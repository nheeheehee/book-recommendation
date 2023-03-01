from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "book-recommendation"
AUTHOR_NAME = "nheeheehee"
LIST_OF_REQUIREMENTS = ["streamlit", "numpy", "scikit-learn"]

setup(
    name=REPO_NAME,
    version="0.0.1",
    author=AUTHOR_NAME,
    description="Simple application for Book Recommendation",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
    )
