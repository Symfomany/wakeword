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

* des contrôles du volume par application5 ;
* une architecture de plugin extensible avec support de modules pouvant être chargés ;
* la compatibilité avec de nombreuses applications audio populaires ;
* le support de multiples sources et collecteurs audioN 1 ;
* une architecture mémoire zero-copy (en) pour une gestion efficace des ressources processeur ;
* une interface en ligne de commande avec possibilité d'utiliser un langage de script ;
* un daemon audio avec possibilité de reconfiguration en ligne de commande ;
* la conversion intégrée de samples et des possibilités de ré-échantillonnage ;
* la faculté de combiner de multiples cartes son en une seule ;
* la faculté de synchroniser de multiples flux de lecture.






