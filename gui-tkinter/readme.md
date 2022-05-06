# Tkinter based GUI for BOT

- We have created a tkinter based graphic user interface for COVIDBOT. 
- The **gui.py** file is the main application file where we create a chatbot using tkinter, take inputs from the user and make call to get_response.py to get the BOT response.
- **get_response.py** makes call to webscrapper programs to get the data (news, article and COVID-19 cases).
- **tkHyperlink.py** files is used to create hyperlink inside tkinter text widget.
- Webscrapper folder consists of webscrapping programs to fetch data.

# Running the main program and interacting with BOT

- As gui.py is the main program once we run this python file it will create a chatbot and users will be able to access it.
- Users can provide input like "help me" to know what the bot does.
- Users can directly enter the news website name either abc,cnn,fox,nbc to access the news from the respective websites.
- Users can also directly enter the 5 digit ZipCode to get the COVID-19 cases in their locality. Please not the zipcode needs to be of Virginia state.
- Also, users have an option to ask for articles by simply typing articles to access the latest updated articles about COVID-19.

**Please Note that get_response.py program calls functions located inside webscrapper directory, so inorder to run the program they need to be in the same directory.**
