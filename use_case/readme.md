# Use Case 

- As per the behaviour of our project, it provides news headlines along with a short summary and a link to further read on.
- abc_news.py provides news from ABC news website.
- covid_numbers.py provides real time COVID-19 cases in a given zipcode.

# Use Case Example and Running

1. **abc_news.py**
- This use case can be run by simply running the program and does not needs any parameters to be given.
- The sample output from this program will involve headline followed by summary and a link to the news.
- Example output:
  - H1: COVID COVERAGE FOR ALL DRIES UP EVEN AS HOSPITAL COSTS RISE
  - Summary: The U.S. came close to providing health care for all for the first time.
  - Link: https://abcnews.go.com/Business/wireStory/covid-coverage-dries-hospital-costs-rise-84536249
  ------------------------------------------------------------------------------------------------
  - H2: COVID-19 HOSPITALIZATIONS AND DEATH EXPECTED TO RISE
  - Summary: The FDA announced a limit on the Johnson & Johnson vaccine to people 18 and older who don’t otherwise have access to a different vaccine.         Also, the use of COVID-19 treatment Paxlovid has risen.
  - Link: https://abcnews.go.com/WNT/video/covid-19-hospitalizations-death-expected-rise-84530458

2. **covid_numbers.py**
- This use case accepts one parameter that is any ZipCode of Virginia State and displays the COVID-19 cases in that county.
- The input for example can be 24060
- Example output:
  - Cases for montgomery county: 
  - Today's Cases:  26
  - Today's Deaths:  0
  - 7 DAY AVERAGE
  - Cases :  28
  - Hospitalized:  15
  - Death:  <1 
