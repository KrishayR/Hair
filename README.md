# Hair
"Hair" is a GUI application where you can experiment with different hair styles real time. It is made using open-cv and tkinter. 

# Usage
![hair](https://user-images.githubusercontent.com/75190777/181997121-18657e6a-f8e2-4cc5-91ab-fedcfaf6cb51.gif)

To use this GUI, start by running `gui.py`. You will see a starting screen that looks like this:
<img width="1193" alt="image" src="https://user-images.githubusercontent.com/75190777/181996760-93bde417-2360-4a31-9b14-04cfe28cd3af.png">
Next, click "start" and it will take you to a page where you can click on multiple buttons, each representing a certain hair style.
<img width="1202" alt="image" src="https://user-images.githubusercontent.com/75190777/181996812-ef12fc9e-d5e3-476f-b82a-52ed310d224c.png">

Fade

![fade](https://user-images.githubusercontent.com/75190777/182006956-38ed40b1-d04f-437a-a206-153831f6c2be.png) 

Mushroom cut

![mushroom](https://user-images.githubusercontent.com/75190777/182006965-d1b43f23-fcd6-466d-aa79-fdca023e8f5c.png) 

Bangs

![bangs](https://user-images.githubusercontent.com/75190777/182006977-c503b23f-aac8-464e-98d8-22eb8b199c4a.png) 

Anime

![anime](https://user-images.githubusercontent.com/75190777/182006980-3fa9aa32-7a45-457c-b6ec-d9e044610cb3.png)

Afro

![afro](https://user-images.githubusercontent.com/75190777/182006949-b6471e26-72d2-4500-88c1-f16a896762e1.png)



Once you click on a button, the camera will start and you'll get another window where you should see the hair style you selected in real time. If another person is next to you, you should see them with the hair style as well. Press esc to close this window.

Example:

![hair](https://user-images.githubusercontent.com/75190777/181997121-18657e6a-f8e2-4cc5-91ab-fedcfaf6cb51.gif)

(If you don't see the hair style, make sure your at least 2 feet from the device and be sure your lighting is decent)

# How it works

The GUI itself is pretty straightforward. In `gui.py` there is simply an image placed in the background and another image that i've made into a button. When you click this button, it goes to the next file `functionality.py` through an import `import functionality`. In `functionality.py` there are just a couple more buttons which are binded to the function `cam(hair)` which essentially imports `video.py` and calls the specific hair style selected.

Most of the magic happens in `video.py`. 
Basically, you open the camera, set the frame width and height, and then use the haarcascades model to identify where the face is in the live camera. Next, I used a pre-set x and y which I added to the default x and y values of where the face lies. In short, it detects the face, then goes up about 50 pixels (the top of the head) and places an overlay of the hair style selected.
<img width="1267" alt="image" src="https://user-images.githubusercontent.com/75190777/182006851-3e0c7436-0ea1-4968-9710-12baa1b171ce.png">


