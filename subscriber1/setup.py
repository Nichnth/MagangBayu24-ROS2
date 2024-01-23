from setuptools import setup

package_name = 'subscriber1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nichnth',
    maintainer_email='nicholasaabel@gmail.com',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = subscriber1.publisher_member_function:main',
            'listener = subscriber1.subscriber_member_function:main',
        ],
    },
)
