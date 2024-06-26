

![image](https://github.com/atsoc1993/Algorand_Discord_Bots_Tutorial_Series/assets/144640214/d307bf03-bdae-4f25-b179-89501095433e)

## What does this code do?

This is a basic react front-end and python back-end for educational purposes that:
- Displays a button at the top left corner 
- The button has the text "Get Last Block Info" on it
- Clicking the button, when the backend.py file is running, will obtain from the backend in a dictionary format the: last round number and all transaction ID's for the last round

The front-end then iterates through the dictionary, where the key is the last round number
and the value is a list of all transaction ID's, and displays them onto the webpage.


## How do I use it?

Assuming you have react setup on your PC already, use the terminal line command below to create a basic new react application:

```npx create-react-app nameYourAppHere```

Then copy and paste the contents of App.js into the default App.js that comes with the react app in the /src folder

Use the following command to start the app, you must be in the directory of the project:

```npm start```

Make sure the backend.py file is running!

Install Python here, and MAKE SURE TO SELECT THE "ADD PYTHON TO PATH" option at the bottom of the installer, otherwise none of your python code will ever work:

https://www.python.org/downloads/

In visual studio code, in the terminal line, copy and paste this terminal command to install needed packages, this only needs to be done once and you have access to them across any python project you create thereafter:

```pip install requests Flask flask-cors```

Create a new file and name it backend.py

Copy and paste the contents of backend.py in this github to your backend.py

You may now go to the top of visual studio code task bar, select "Run without debugging" and select the Python Interpreter if prompted.
In the Episode 1 folder, there is a more in-depth guide to python installation as well as a video guide.
Make sure to also install the extensions in visual studio code, like intellisense for syntax errors/color coding

Upon running the file you should see something like this in the console:

![image](https://github.com/atsoc1993/Algorand_Discord_Bots_Tutorial_Series/assets/144640214/50567547-2025-46e5-97bb-cd9cfecaac69)

## You should now be able to click the button and see all the block transaction IDs pour in and display on your front-end with every button click!


