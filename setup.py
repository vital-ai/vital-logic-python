from setuptools import setup, find_packages

setup(
    name='vital-logic',
    version='0.1.0',
    author='Marc Hadfield',
    author_email='marc@vital.ai',
    description='Vital Logic',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vital-ai/vital-logic-python',
    packages=find_packages(exclude=['test_rules', 'tests', 'ergoai', 'rules', 'domain_model']),
    license='Apache License 2.0',
    install_requires=[
            'vital-ai-vitalsigns>=0.1.27',
            'six',
            'pyyaml'
        ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
