from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': ' Brasil, São Paulo/São Sebastião',
    'salary': 'R$ 1.500,00'
  },

  {
    'id': 2,
    'title': 'Developer',
    'location': ' Brasil, São Paulo/São Sebastião',
    'salary': 'R$ 1.500,00'
    
  },

  {
    'id': 3,
    'title': 'Front Enginieer',
    'location': 'Remote',
    'salary': 'R$ 1.500,00'
    
  }, 

  {
   'id': 4,
    'title': 'System Analyst',
    'location': ' Remote',
    
  },

   {
    'id': 5,
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