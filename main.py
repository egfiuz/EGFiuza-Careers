from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': ' Bengaluru, India',
    'salary': 'R$ 1.500,00'
  },

  {
    'id': 2,
    'title': 'Data Scientist',
    'location': ' Delhi, India',
    'salary': 'R$ 1.800,00'
    
  },

  {
    'id': 3,
    'title': 'Front Enginieer',
    'location': 'Remote',
    'salary': 'R$ 2.500,00'
    
  }, 

  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': ' Remote',
    
  }
  
]

@app.route("/")
def hello_jovian():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name='EGFiuza')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)