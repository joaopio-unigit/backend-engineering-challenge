from setuptools import setup, find_packages

setup(
    name="unbabel_moving_averages",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts':[
            'unbabel_moving_averages=unbabel_moving_averages.main:main'
        ]
    }
)