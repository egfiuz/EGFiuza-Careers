from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      return jobs   


@app.route("/")
def hello_egfiuza():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                        jobs=jobs,
                        company_name='EGFiuza')
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)