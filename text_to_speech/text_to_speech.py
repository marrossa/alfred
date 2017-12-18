import pyttsx3

name="Testing"
engine = pyttsx3.init()
engine.say(name);
engine.setProperty('rate',100)
engine.runAndWait();
