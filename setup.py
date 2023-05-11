setup(
    name="fitz",
    version="0.1.0",
    description="A CLI tool for interacting with GPT",
    author="Seth Beckett",
    author_email="sethvbeckett@gmail.com",
    url="https://github.com/sethbeckett/fitz",
    license="GPLv3",
    packages=find_packages(),
    install_requires=[
        "openai",
        # other dependencies...
    ],
    entry_points={
        "console_scripts": [
            "fitz=fitz.main:main",
        ],
    },
)
