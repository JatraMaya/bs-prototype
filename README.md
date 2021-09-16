# bs-prototype
Simple prototype of Beautiful Soup 4 and flask

After you clone the repo, cd to the project directory then run 

```
pip install -r requirements.txt
python app.py
```

or if you have pipenv installed, just run

```
pipenv install
python app.py
```

to use this web app simply provide a website url you want to check as a parameter

example:
```localhost:5000/https://google.com/
```
it'll then send a response in a json format, weather the url you provided contains Facebook pixel script in their body tag.

