from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('Home.html')

@app.route('/about')
def about():
  return render_template('About.html')

@app.route('/project')
def project():
  return render_template('Project.html')

@app.route('/p1')
def p1():
  return render_template('p1.html')

@app.route('/p2')
def p2():
  return render_template('p2.html')

@app.route('/p3')
def p3():
  return render_template('p3.html')

@app.route('/p4')
def p4():
  return render_template('p4.html')


if __name__ == '__main__':
  app.run(debug = True)