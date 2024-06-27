from setuptools import setup, find_packages

setup(
    name='music_recommendation_system',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'flask',
        'pandas',
        'numpy',
        'scikit-learn',
        'scipy',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'music_recommendation_system=main:main',
        ],
    },
)
