from flask import Flask, request,render_template
import datetime 

app = Flask(__name__)

@app.route('/')
def getbirthday():
    return render_template('birthday.html')


@app.route('/birthday', methods = ['POST'])
def birthday():
    birthday = str(request.form['birthday'])
    birthday = birthday.split('-')
    first_number = int(birthday[2])
    second_number = int(birthday[1])
    third_number = int(birthday[0])
    birthdate = datetime.date(third_number,second_number,first_number)
    date = datetime.date.today()
    bday_this_year = datetime.date(date.year, birthdate.month, birthdate.day)
    bday_next_year = datetime.date(date.year + 1, birthdate.month, birthdate.day)
    if bday_this_year > date:
        nextbirthday = bday_this_year
    else:
        nextbirthday = bday_next_year
    days_till_next = (nextbirthday-date).days
            
    #except ValueError:
        #return 'Invalid data'
    return f'You have {days_till_next} days till your next birthday.'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)