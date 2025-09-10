from setuptools import setup, find_packages

setup(
    name='cinema-booking-system',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    author='Adrien Fort',
    description='A Python project for managing cinema bookings.',
    url='https://github.com/yourusername/cinema-booking-system',
)
