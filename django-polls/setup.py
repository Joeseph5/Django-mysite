from setuptools import find_packages, setup
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

    # allow setup.py to be run from any path
    os.chdir(os.path.normpath(os.path.join(
        os.path.abspath(__file__), os.pardir)))

    setup(
        name='django-polls',
        version='0.1',
        packages=find_packages(),
        include_package_data=True,
        license='BSD License',  # example license
        description='A simple Django app to conduct Web-based polls.',
        long_description=README,
        url='https://www.pepperexp.com/',
        author='Joe',
        author_email='joe.hyhznx@gmail.com',
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',  # example license
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.5',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',

        ],

    )
