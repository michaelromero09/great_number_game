from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = 'beccas_face'

def randomNumber():
  session['randomNumber'] = random.randrange(0,101)
  print session['randomNumber']

@app.route('/')
def index():
  print session['randomNumber']
  return render_template('index.html')

"""@app.route('/guess', methods=['get'])
def guess():
  num = request.form['num']
  #if request.form['num'] < session['randomNumber']:
  if 4 < num:
    print 'too low'
  return redirect('/')"""

app.run(debug=True)