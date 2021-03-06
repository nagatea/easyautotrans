from setuptools import setup, find_packages

setup(
    name="easyautotrans",
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "pyperclip",
        "googletrans",
        "termcolor"
    ],
    entry_points={
        "console_scripts": [
            "easy-auto-trans = easyautotrans.easyautotrans:main"
        ]
    }
)
