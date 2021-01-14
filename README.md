# Automate ISC Online Classes

We all are in a great pendemic right now. The noble Corona Virus has almost eaten the world. During this time, almost all 
schools & colleges are taking classes Online.

As I am a student of Ideal School & College, I have to attend the online classes. But I feel bored when I go to the 
home page of ISC classes, gve my ID and password, press Login, wait, scroll down,
look if any class has been started, if not so then reload the page for several times,
after that press the button, open zoom meeting......

These make me feel bored. So as a little programmer, I think of something new. Something that will automate this stuff.
So I wrote a simple Python code which does this all stuf automatically. All I ahave to do is, Press "Connect" and wait.
It does everything itself. It moves my mouse, writes my ID clicks Login.... All!

If you are a student of ISC and you are simillar with me, then you can download this repository & make everything AUTO.

In order to do that, you have to install python from the link bellow:
https://www.python.org/downloads/

After that, you have to install some third party modules. For this, click on
1. Start button
2. Type CMD
3. Press Enter. You will get a black window.
4. Then type the following command and press enter

```bash
$ pip install pyautogui keyboard requests
```

After all packages get installed, run the System.py file.
Then you open the main.py file.
Find these lines and type your BDS ID and password,
ID = "" # enter your ID
DOF = "" # enter your password

Now run the main.py file, press connect and enjoy. Don't touch anything during the files run.
