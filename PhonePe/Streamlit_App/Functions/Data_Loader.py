
from Functions.config import *

env_path = r"C:\Users\nagan\OneDrive\Desktop\Guvi\Project\PhonePe\.env"
load_dotenv(env_path)

def sql_query_runner(query,param=None):

    ## setting up the connection
    #connectin details
    host=os.getenv("my_sql_host")
    # 'localhost'

    # print(host)
    user=os.getenv("my_sql_user")
    # 'root'
    # 
    # print(user)

    password=os.getenv("my_sql_password")
    # 'Narasimha21'
    # 
    port=3306
    database='phonepe_pulse'
    # if not password:
    #   raise ValueError("Missing 'my_sql_password' in environment variables or .env file.")
    password = quote_plus(password)


    # print(password)
    ## creating engine and connecting to it
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
    
    with engine.connect() as conn:
        if param is None:
            result=conn.execute(text(query))
        else:
            result=conn.execute(text(query),param)
        rows=result.fetchall()
        cols=result.keys()
    df=pd.DataFrame(rows,columns=cols)
    # display(df.head)
    engine.dispose()

    return df
    # return password
