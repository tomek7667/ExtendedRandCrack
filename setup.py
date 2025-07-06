from setuptools import setup

with open("README.md", "r", encoding="utf-16") as fh:
    long_description = fh.read()

setup(
    name='extendedrandcrack',  # Updated package name
    packages=['extendedrandcrack'],  # Package folder name
    version='1.0.0',  # Starting stable version
    license='MIT',
    description="Predict Python's random module outputs, extended with 64-bit support and state rewind/advance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='tomek7667',
    author_email='tomek7667@cyber-man.pl',
    url='https://github.com/tomek7667/ExtendedRandCrack',  # Recommend updating this if it's a fork
    keywords=[
        'random', 'mersenne-twister', 'security', 'cryptography',
        'prng', 'predictor', 'cracker', 'random-crack', 'python-random'
    ],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
