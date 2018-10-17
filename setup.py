from distutils.core import setup

setup(
    name='wordgenerator',
    version='0.3.3',
    author='Håkon Hukkelås',
    author_email='haakohu@stud.ntnu.no',
    packages=['wordgenerator'],
    url='https://github.com/hukkelas/RandomWordGenerator',
    license='LICENSE.txt',
    long_description_content_type="text/markdown",
    long_description=open('README.txt').read(),
    include_package_data=True
)