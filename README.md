# Covid_News (CoVBOT) 
A simple interface for viewing local and recent covid news, articles and local cases based on zipcode for state of Virginia.

## Team Drunk Bits :
* **Jeffrey Smith** > Github: [jsmith1031](https://github.com/jsmith1031)
Email: [jeffreysmith@vt.edu](mailto::jeffreysmith@vt.edu)

* **Saketh Vegesna** >  Github: [CozySocks12](https://github.com/CozySocks12)
Email: [sakethv@vt.edu](mailto::sakethv@vt.edu)

* **Bibek Sharma** > Github: [bs2626](https://github.com/bs2626)
Email: [bibek99@vt.edu](mailto::bibek99@vt.edu)


# Tkinter Based GUI for CoVBOT
- Tkinter based gui is created for the bot. This allows BOT to be interactive with users and at the same time provide users with all the necessary infromation related to the COVID-19 Pandemic.
- This BOT can be used to fetch news, articles and daily COVID-19 cases in each county based on the zipcode provided for the state of VA.
- The main program is located in the directory **gui-tkinter** along with all the dependent code and program files.




## Dependencies

* Flutter
* Python 3.0 or newer
* * BeautifulSoup
* * pyttsx3
* * tkinter

<br></br>
## Build Instructions

```
flask run
```
\
then (in another terminal)
```
flutter run
```


### Setting up Flutter

Following this tutorial: [codelabs](https://codelabs.developers.google.com/codelabs/flutter#1\
Download the flutter SDK  [here](https://docs.flutter.dev/get-started/install)\
Since flutter is almost 3GB, I suggest moving the directory location before adding to enviroment path variables. Also know when the flutter install location is,because if you are debugging in chrome, you will probably need to add '--disable-web-security' to the launch arguments to connect to a local flask server.\
Once you have flutter installed, if you're using Visual Studio Code, download the Flutter extension from the marketplace. If not, there are tools for using Flutter with other IDEs  [here](https://docs.flutter.dev/get-started/test-drive?tab=terminal)

