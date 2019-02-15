# Processing

1. Audio Processing includes Acoustic Echo Cancellation (AEC), Beamforming, Noise Suppression (NS), etc.
2. Keyword Spotting (KWS) detects a keyword (such as OK Google, Hey Siri) to start a conversation.
3. Speech To Text (STT)
4. Natural Language Understanding (NLU) converts raw text into structured data.
5. Knowledge/Skill/Action - Knowledge base and plugins (Alexa Skill, Google Action) to provide an answer.
6. Text To Speech

## Python
1. Use Circular Mic 6-Array and Librespeaker
Librespeaker is an audio processing library which can perform noise suppression, direction of arrival calculation, beamforming, hotword searching. It reads the microphoone stream from linux sound server, e.g. PulseAudio.

http://respeaker.io/librespeaker_doc/examples.html

First of all, as an audio processing application, we always have to *collect audio stream*. 
In librespeaker, we have 3 ways to *capture audio stream*: PulseAudio Server, ALSA API and a wav file.


*PulseAudio is a sound system for POSIX* OSes, meaning that it is a proxy for your sound applications. 
It allows you to do *advanced operations* on your sound data as it passes between your application and your hardware.

Il permet des échanges audio par le réseau entre des systèmes Linux et Microsoft Windows par exemple.

PulseAudio fonctionne sur les systèmes compatibles POSIX tels que Linux et sous Microsoft Windows. Son code source est publié selon les termes de la licence publique générale limitée GNU (GNU LGPL)3. Si la compilation intègre certaines dépendances optionnelles, le daemon et la bibliothèque serveur (libpulsecore) sont publiés selon les termes de la licence publique générale GNU (GNU GPL)4.

* des contrôles du volume par application ;
* une architecture de plugin extensible avec support de modules pouvant être chargés ;
* la compatibilité avec de *nombreuses applications audio populaires* ;
* le support de multiples sources et collecteurs audioN 1 ;
* une architecture mémoire zero-copy (en) pour une gestion efficace des ressources processeur ;
* une interface en ligne de commande avec possibilité d'utiliser un langage de script ;
* un daemon audio avec possibilité de reconfiguration en ligne de commande ;
* la conversion intégrée de samples et des possibilités de ré-échantillonnage ;
* la faculté de combiner de multiples cartes son en une seule ;
* la faculté de synchroniser de multiples flux de lecture.


PulseAudio est un serveur son, un *processus d'arrière-plan qui accepte les entrées son d'une ou plusieurs sources* (processus ou périphériques de capture) et les redirige vers un ou plusieurs collecteurs (cartes son, serveurs PulseAudio distants ou autres processus).

PulseAudio utilise un modèle dans lequel ce sont les applications qui envoient le flux audio au serveur, contrairement au serveur son JACK qui détermine quand et dans quel ordre les applications doivent le lui envoyer.

Selon un scénario d'installation typique sous Linux, l'utilisateur configure *ALSA pour utiliser un dispositif virtuel fourni par PulseAudio*. Ainsi, les applications utilisant *ALSA enverront leur sortie son vers PulseAudio, qui utilisera alors ALSA lui-même pour accéder à la vraie carte son*. PulseAudio fournit également sa propre interface native pour les applications qui veulent supporter PulseAudio directement, de même que l'ancienne interface pour les applications ESD, le rendant adapté pour remplacer ESD.

(https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Pulseaudio-diagram-fr.svg/800px-Pulseaudio-diagram-fr.svg.png)
[https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Pulseaudio-diagram-fr.svg/800px-Pulseaudio-diagram-fr.svg.png]



# Mycroft some Wake Word


https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word

Some Python virtual environment

```
    source .venv/bin/activate
```

Some dependencies


* python3-pip
* libopenblas-dev: : Optimized BLAS (linear algebra) library based on GotoBLAS2
* python3-scipy : mathematics, science, and engineering (like numpy)
* cython : compilation of Python
* libhdf5-dev : Data Format to save model (Hierarchical Data Format): les ensembles de données (datasets), qui sont des tableaux multidimensionnels contenant des données d'un même type (pré-défini ou dérivé)
* python3-h5py: HDF5 for Python
* portaudio19-dev: Portable audio I/O - documentation

https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word

## Executables

Here's a summary of all the executables:

* precise-collect - Record audio samples for use with Precise
* precise-convert - Convert wake-word model from Keras to TensorFlow
* precise-eval - Evaluate a list of models on a dataset
* precise-listen - Run a model on microphone audio input
* precise-stream - Run a model on raw audio data
* precise-test - Test a model against a dataset
* precise-train - Train a new model on a dataset
* precise-train-incremental - Train a model to inhibit activation by marking false activations and retraining







