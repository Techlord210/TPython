from setuptools import setup

with open('README.md', 'r') as f:
    ld = f.read()
version = '0.4'

if __name__ == '__main__':
    setup(
    name='TPython',
    version=version,
    description='A better python REPL',
    long_description=ld,
    long_description_content_type='text/markdown',
    url='https://github.com/Techlord210/TPython',
    author='Techlord210',
    author_email='techlord210@gmail.com',
    license='MIT', 
    classifiers=[
            "Development Status :: 4 - Beta",
            'Environment :: Console',
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Other Audience",
            "Programming Language :: Python :: 3.6",
            "License :: OSI Approved :: MIT License"
        ],
    keywords='interactive,python,better,repl,tpython',
    install_requires=[
        'colorama'
        ],
    entry_points={
        'console_scripts':[
            'tpy = main:main'
            ]
        }
    )