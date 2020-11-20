# Blink Detection and Modeling
#### Imaging Science Senior Project
#### Jared Gregor (jmg2586@rit.edu)

### Why Blinks?
“Deep neural networks for video-based eye tracking have demonstrated
resilience to noisy environments, stray reflections, and low-resolution eye
imagery. However, to train these networks, a large number of manually
annotated images are required. To alleviate the cumbersome process of
manual labeling, computer graphics rendering is employed to automatically
generate a large corpus of annotated eye images under various conditions.” (1)
This imagery depicts a synthetic eye looking in a known gaze direction, as
reported by an eye tracker. These images are useful when training models to
track features on the pupil and the iris – a step necessary for improving upon
conventional algorithms for gaze estimation.
 A future aim of eye tracking algorithms is to accurately estimate gaze
around a blink, when pupil and iris features are temporarily occluded. This aim
is difficult because blinks cause a failure in the process of gaze estimation that
is required to generate this synthetic imagery, and this results in unnatural
synthetic eye images throughout the blink. My role in this project is to focus on
creating a mathematical model that is capable of modeling and rendering
synthetic blinks for the neural network’s training data. By training with blink
imagery the network will be more robust to get information across blinks and is
more resembling of what might be seen in real eye tracking video.
(1) Nair, N., Chaudhary, A. K., Kothari, R. S., Diaz, G. J., Pelz, J. B., Bailey, R., “RIT-Eyes: realistically rendered
eye images for eye-tracking applications,” Symposium on Eye Tracking Research and Applications (2020). 
