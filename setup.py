from setuptools import setup, find_packages # install --upgrade setuptools wheel

setup(
    name='cli_pyassist',
    version='1.0',
    description='The program allows the user to manage data in an address book, including tasks such as adding, deleting, exporting, and importing records. It also features the capability to export and import data in CSV format. Additionally, the program facilitates file sorting on the computer. It provides error handling and a user-friendly command-line interface for easy of use.',
    url='https://github.com/Szumapman/PyAssist',
    author=('Beata Chrząszcz', 'Jakub Szymaniak', 'Julia Macha', 'Paweł Szumański', 'Sabina Limmer',),
    author_email='',
    packages=['cli_pyassist'],
    install_requires=[
        'SpeechRecognition',
        'pyttsx3',
        'pyaudio',
        'pyfiglet',
        'cowsay',
        'prompt_toolkit',
    ],
    entry_points={'console_scripts': ['cli_pyassist = pyassist.cli_pyassist:main']}
)