from flask import Flask, request
import datetime 

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a website!'

@app.route('/hello')
def hello():
    return f'Hello anonymous person.'

@app.route('/hello/<name>')
def greet(name):
    return f'Hello there, {name}'

@app.route('/birthday/<day>/<month>/<year>')
def add(day,month,year):
    first_number = int(day)
    second_number = int(month)
    third_number = int(year)
    if first_number and second_number and third_number:
        if 0 == 0:
            birthday = datetime.date(third_number,second_number,first_number)
            date = datetime.date.today()
            bday_this_year = datetime.date(date.year, birthday.month, birthday.day)
            bday_next_year = datetime.date(date.year + 1, birthday.month, birthday.day)
            if bday_this_year > date:
                nextbirthday = bday_this_year
            else:
                nextbirthday = bday_next_year
            days_till_next = (nextbirthday-date).days

                
        #except ValueError:
            #return 'Invalid data'
        return f'You have {days_till_next} days till your next birthday.'
    else:
        return 'No arguments detected'

@app.route('/test')
def test():
    return 

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)



