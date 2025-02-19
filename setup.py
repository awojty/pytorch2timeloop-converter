from setuptools import setup, find_packages

setup(name='pytorch2timeloop',
        version='0.2',
        url='https://github.com/Accelergy-Project/pytorch2timeloop-converter',
        license='MIT',
        install_requires=["torch==1.7", "torchvision==0.8", "numpy==1.19", "pyyaml==5.3"],
        python_requires='>=3.6',
        include_package_data=True,
        packages=find_packages())
