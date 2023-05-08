from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://xq4wuo764lx8pkxvhkul:pscale_pw_L4eeg1Prcb1KQiqSuttY7g2Uc1z6WWReIrojdGIjtiV@aws.connect.psdb.cloud/egfiuzacareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      return jobs   


