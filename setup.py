from distutils.core import setup

setup(
    name='wordgenerator',
    version='0.3.4',
    author='Håkon Hukkelås',
    author_email='haakohu@stud.ntnu.no',
    packages=['wordgenerator'],
    url='https://github.com/hukkelas/RandomWordGenerator',
    license='LICENSE.txt',
    long_description_content_type="text/markdown",
    long_description=open('README.txt').read(),
    package_data= {
        "wordgenerator": ["words.txt"]
    }
)