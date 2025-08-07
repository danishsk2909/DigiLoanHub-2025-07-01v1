from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Using ExploreP.html as main page

@app.route('/exploreproduct')
def exploreproduct():
    return render_template('ExploreP.html')

@app.route('/loans')
def loans():
    return render_template('loans.html')

# Handle the static HTML file routes from your original code
@app.route('/accounts')
def accounts():
    return "<h1>Accounts Page - Coming Soon!</h1><a href='/'>Back to Home</a>"

@app.route('/deposits')
def deposits():
    return "<h1>Deposits Page - Coming Soon!</h1><a href='/'>Back to Home</a>"

@app.route('/cards')
def cards():
    return "<h1>Cards Page - Coming Soon!</h1><a href='/'>Back to Home</a>"


@app.route('/investments')
def investments():
    return "<h1>Investments Page - Coming Soon!</h1><a href='/'>Back to Home</a>"

@app.route('/home-loan')
def home_loan():
    return render_template('home_loan_form.html')

@app.route('/personal_loan')
def personal_loan():
    return render_template('Loan_personal.html')

@app.route('/Business_loan')
def Business_loan():
    return render_template('Business_Loan.html')

@app.route('/explore-products')
def explore_products():
    return render_template('ExploreP.html')


# >>> Siddhi <<<

# Your Investments page (renders your provided template)
@app.route("/invest")
def invest():
    # Keep the filename as provided by you: investement.html
    return render_template("invest.html")

# >>> ADD THIS <<<
@app.route("/pfinvest")
def pfinvest():
    return render_template("pfinvest.html")

@app.route('/pfinvestregister')
def pfinvestregister():
    return render_template('pfinvestregister.html')  # Make sure this file exists


# >>> Bharath <<<

@app.route('/cards_main')
def cards_main():
    return render_template('cards_main.html')

@app.route('/creditcard')
def creditcard():
    return render_template('creditcard.html')

@app.route('/debitcard')
def debitcard():
    return render_template('debitcard.html')

@app.route('/prepaid')
def prepaid():
    return render_template('prepaid.html')

@app.route('/cardapply')
def cardapply():
    return render_template('cardapply.html')


@app.route('/comparecards')
def comparecards():
    return render_template('comparecards.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

# >>> Rajeev <<<

@app.route('/forex')
def forex():
    return render_template('forex.html')

@app.route('/travel_forex')
def travel_forex():
    return render_template('travel_forex.html')

@app.route('/travel_forex_form')
def travel_forex_form():
    return render_template('travel_forex_form.html')

@app.route('/send_money_abroad')
def send_money_abroad():
    return render_template('send_money_abroad.html')

@app.route('/send_money_abroad_form')
def send_money_abroad_form():
    return render_template('send_money_abroad_form.html')

@app.route('/send_money_india')
def send_money_india():
    return render_template('send_money_india.html')  

@app.route('/send_money_india_form')
def send_money_india_form():
    return render_template('send_money_india_form.html')    

@app.route('/currency_exchange')
def currency_exchange():
    return render_template('currency_exchange.html')

@app.route('/currency_exchange_form')
def currency_exchange_form():
    return render_template('currency_exchange_form.html')


if __name__ == '__main__':
    # Use host='0.0.0.0' if you want to access from your LAN/device
    app.run(debug=True)