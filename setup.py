from setuptools import setup, find_packages

setup(
    name='simple_chatbot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai>=1.0.0'
    ],
    author='Dhiraj Kumar',
    author_email='dhiraj7kr@gmail.com.com',
    description='A simple chatbot wrapper for OpenAI GPT models',
    url='https://github.com/dhiraj7kr/simple_chatbot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
