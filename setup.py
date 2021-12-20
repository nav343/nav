from distutils.core import setup
setup(
    name='nav_snmlogic',
    packages=['nav-tts'],
    version='0.1',
    license='MIT',
    description='A module which simplifies stuff related to voice',
    author='Navaneeth K',
    author_email='snmlogic111@gmail.com',
    url='https://github.com/SnmLogic/nav',
    download_url='https://github.com/SnmLogic/nav/archive/refs/tags/version_0.1.tar.gz',
    keywords=['Voice', 'Nav', 'TTS'],
    install_requires=[
        'pyttsx3',
        'speech_recognition',
        'pyaudio'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
