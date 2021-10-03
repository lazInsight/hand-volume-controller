# Volume Hand Controller
## Practical work with library MediaPipe
[MediaPipe](https://mediapipe.dev/){:target="_blank"} is open-source library from [Google](https://github.com/google){:target="_blank"} which allow use API`s for create cross-platform DIY projects.\
Usage [Hand Detection](https://solutions.mediapipe.dev/hands) for create **HandTrackingModule**. This module allows work with static and streaming media.\
Used libraries:
* [MediaPipe](https://mediapipe.dev/){:target="_blank"}
* [CV2](https://opencv24-python-tutorials.readthedocs.io/_/downloads/en/stable/pdf/){:target="_blank"}
* [time](https://docs.python.org/3/library/time.html){:target="_blank"}
* [math](https://docs.python.org/3/library/math.html){:target="_blank"}
* [subprocess](https://pythonspot.com/python-subprocess/){:target="_blank"}
### MediaPipe
Used for the detecting hand and landmarks on it. Getting the coordinates **x** and **y** of landmark to calculate the length between them and
percentage for volume value.
### CV2
Used for get real-time media.
### math
Used for calculate length between landmark.
### subprocess
Used for management OS Linux processes.\
\
\
***This work was carried out to explore the possibilities of the language and open source libraries, as well as for practical work in programming.***
