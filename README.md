# Automate ISC Online Classes

যেহেতু এই করোনা মহামারীর সময় স্কুল কলেজের ক্লাসগুলো সব অনলাইনে চলছে, তাই একজন IDEAL School & College এর Student হওয়ার খাতিরে প্রতিদিন নির্দিষ্ট Website এ গিয়ে ID এবং Password দিয়ে login করে scroll করে নিচে নেমে সঠিক টাইম অনুযায়ী নির্দিষ্ট Link এ ক্লিক করে Zoom এ ক্লাস ওপেন করব এত সময় তার ধৌর্য আমার নাই।

তাই একজন Programmer হওয়ার এডভ্যান্টেজ নিয়ে Python এ একটা Automate Programme লিখে ফেলাটা একটা Challenge ছিল বৈকি। তবে শেষ পর্যন্ত তিন দিনের পরিশ্রমে আমি একটা প্রোগ্রাম লিখে ফেললাম যা অটোমেটিক সব করে ফেলে।

ব্যাপারটাকে আরো smooth করার জন্য Tkinter দিয়ে একটা GUI বানিয়ে ফেলাম। 
এই সফটওয়্যার টা Auto মাউস মুভমেন্ট করে আমার কাজটা সহজে করে দেয়। প্রতিদিন সকালে তাই ঘুম থেকে উঠে Laptop না গুতিয়ে আমার প্রোগ্রাম টা রান করে আমি ফ্রেশ হয়ে আসতে পারি। এটা আমার ২০২০ এর সেরা প্রজেক্টের মধ্যে একটা। 

এই প্রজেক্ট টা করার জন্য আমি যেসকল Third Party Module ব্যবহার করেছি তা হল:

* PyAutoGUI
* Tkinter
* Keyboard
* Webbrowser
* Requests

আমার এই প্রজেক্ট যদি কেউ নিজে চালিয়ে দেখতে চান তাহলে নিচের কমান্ড গুলো টার্মিনালে রান করতে হবে। তবে তার জন্য PC তে git ইনস্টল করা থাকতে হবে:

```git
$ git clone https://github.com/TahcinMycin/Automate_ISC_Online_Classes.git
```
```console
$ cd Automate_ISC_Online_Classes
```

এই module গুলো ইনস্টল করতে নিচের command গুলো Terminal এ বা Command Prompt এ রান করতে হবে:

```console
$ pip install pyautogui
$ pip install keyboard
$ pip install requests
```

যদি pip কমান্ড টি কাজ না করে বিশেষ করে MacOS এ তাহলে নিচের command গুলো রান করতে হবে:

```console
$ pip3 install pyautogui
$ pip3 install keyboard
$ pip3 install requests
```

কারো কারো যদি কোনোটাই কাজ না করে তাহলে এটা লিখলে কাজ হতে পারে:

```console
$ python -m pip install pyautogui
$ python -m pip install keyboard
$ python -m pip install requests
```

এতকিছু না করে যদি একেবারে সব ইনস্টল করতে ইচ্ছে হয়, তাহলে আমি install.py নামে একটা ফাইল তৈরি করে রেখেছি। ফাইলটা রান করতে লিখতে হবে:

```console
$ python install.py
```

এতে করে সবগুলো module একেবারে ইন্সটল হয়ে যাবে। পরের স্টেপ হচ্ছে main.py ফাইল এর নিচের লাইন গুলো পরিবর্তন করা:
```python
    ID = "" # Enter your BDSMAKE ID
    DOF = "" # Enter your Date of Birth(day-month-year)
```

এখানে ID এর জায়গায় নিজের BDSMAKE ID এবং DOF এর জায়গায় নিজের Date of birth দিতে হবে। IDEAL এর ছাত্র হলে তোমার কাছে ID  থাকার কথা। আর Date of birth দিতে হবে dd/mm/yyyy format এ।

বাকি সব একই রকম থাকবে। এখন main.py ফাইল টি রান করতে নিচের কমান্ড টি রান করতে হবে:

```bash
$ python main.py
```

ফাইল টি রান করলে নিচের মতো একটা window ওপেন হবে:


![alt text](https://github.com/TahcinMycin/Automate_ISC_Online_Classes/blob/main/shot.JPG)

এখন শুধু Connect বাটনে ক্লিক করে অপেক্ষা করতে হবে আর দেখতে হবে মজা!!!
কানেক্ট করা মাত্র ওয়েব ব্রাউজার এ লিংক টি ওপেন হবে। অটোমেটিক মাউস নড়ে ID এবং Date of Birth দিয়ে login এ ক্লিক করে লগইন করবে, তারপর স্ক্রল ডাউন করে নির্দিষ্ট সময়ের ক্লাস এর লিংক এ সে অটোমেটিক ক্লিক করে দিবে। তারপর পেজ লোড হলে Zoom এ ক্লাস ওপেন করে দিবে।

চাইলে এর জন্য একটা Executable ফাইল তৈরি করা যায়। এর জন্য প্রথমে PyInstaller মডিউল টা ইনস্টল করতে হবে নিচের কমান্ডার মাধ্যমে:
```bash
$ pip install pyinstaller
```

তারপর সেটআপ ফাইল তৈরি করতে টার্মিনালে লিখতে হবে:
```bash
$ pyinstaller main.py --name AutoISC --icon icon.png --onefile --noconsole
```
এতে করে dist নামক folder এর ভিতরে AutoISC.exe নামে ফাইল তৈরি হয়ে যাবে। একটা আইকন সহ। 

কোনো কোনো কম্পিউটারে স্ক্রিন রেজুলেশন এর জন্য ঝামেলা করতে পারে। Other than that, এটা পুরা একটা প্রজেক্ট। হবে Code টি Android চালিত মোবাইলে কাজ করবে না! তাই আমার পরবর্তী প্রজেক্ট হচ্ছে তা মোবাইল ফোনে ব্যবহেরের জন্য তৈরি করা। এর জন্য আমি ব্যবহার করবো Kivy মডিউল। সবাইকে ধন্যবাদ!
