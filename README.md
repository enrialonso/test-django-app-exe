# Portable Django APP
Why not use web interface to generate desktop app, this small project shows how to build a desktop app with Django and UI of any browser.

On the backend use Django for manage the core of the app and render templates localy and send the UI to the browser and all is posible to build one .exe file to group all files and make one file app based on desktop app.

Its simple, the app.py raise the server of the Django framework and on the terminal display the local IP:PORT to connect with the browser and interact with the local app.

For build the .exe file use pyinstaller with this command:

```sh
pyinstaller -y -F --add-data "<PATH_TO_FOLDER>/test-django-app-exe/core";"core/" --add-data "<PATH_TO_FOLDER>/test-django-app-exe/venv";"venv/"  "<PATH_TO_FOLDER>/test-django-app-exe/app.py"
```

Is necesary include core Django project and virtual environment for correct operation of the app. feel free to report issues!

To share the app need copy the app.exe and db folder to another location an you are ready to share with anyone you want.

If you want test the app, have an exe app to test and play with then, when you reload the index web add a random string to the database to check the app.