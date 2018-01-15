from app.api.rest.events.event import Event
import os
from urllib import parse
import psycopg2
import psycopg2.extras

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

events = []

def get_db_connection():
    return psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port)

def insertupdate(query):
    connection = None
    cursor = None
    result = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        connection.commit()        
        result = cursor.fetchone()
    except:
        result = None
        if connection != None:
            connection.rollback()
    finally:
        if cursor != None:
            cursor.close()
        if connection != None:
            connection.close()
    return result

def read(query,all= True):
    connection = None
    cursor = None
    result = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        if all is True:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
    except Exception as e:
        result = None
        if connection != None:
            connection.rollback()
        raise e
    finally:
        if cursor != None:
            cursor.close()
        if connection != None:
            connection.close()
    return result

def load_data():
    #Squiry Picks
    events.append(Event('EDM Night, Saarang IIT Madras','EDM Night','IIT Madras','https://static.wixstatic.com/media/46cd01_ee81122358e542a38bf1ddc51b92bd90~mv2.jpg/v1/fill/w_880,h_444,q_85,usm_0.66_1.00_0.01/46cd01_ee81122358e542a38bf1ddc51b92bd90~mv2.jpg','2000','party','Jan 12, 2018 at 8:30pm - 10:00pm IST').__dict__)        
    events.append(Event('Rock Show, IIT Madras','Rock Show, IIT Madras','IIT Madras','https://static.wixstatic.com/media/46cd01_15c254ee61b8469c8c342836c3b3d56b~mv2.jpg/v1/fill/w_880,h_458,q_85,usm_0.66_1.00_0.01/46cd01_15c254ee61b8469c8c342836c3b3d56b~mv2.jpg','2000','party','Jan 13, 2018 at 6:30pm - 10:00pm IST').__dict__)
    events.append(Event('LOL with Daniel Fernandes, Kunal Kamra','LOL with Daniel Fernandes, Kunal Kamra','Phoenix Market City','https://static.wixstatic.com/media/46cd01_8686affe41294664913523f7cb1a7ebb~mv2.jpg/v1/fill/w_828,h_315,q_85,usm_0.66_1.00_0.01/46cd01_8686affe41294664913523f7cb1a7ebb~mv2.jpg','2000','party','Jan 13, 2018 at 7:00pm - 9:00pm IST').__dict__)
    events.append(Event('Learn Surfing | Kayaking | Stand up Paddle - ECR','Learn Surfing | Kayaking | Stand up Paddle - ECR','Kovalam beach','https://static.wixstatic.com/media/46cd01_572c4d79a9054d769d639039aa1a9b94~mv2_d_2048_1360_s_2.jpg/v1/fill/w_880,h_584,q_85,usm_0.66_1.00_0.01/46cd01_572c4d79a9054d769d639039aa1a9b94~mv2_d_2048_1360_s_2.jpg','2000','party','Jan 14, 2018 at 7:30am - 11:00am IST').__dict__)
    events.append(Event('Jungle Camping - Munnar','Jungle Camping - Munnar','Munnar','https://static.wixstatic.com/media/46cd01_561af5ab82fb40419f7c9ad95592b63f~mv2_d_2048_1365_s_2.jpg/v1/fill/w_880,h_587,q_85,usm_0.66_1.00_0.01/46cd01_561af5ab82fb40419f7c9ad95592b63f~mv2_d_2048_1365_s_2.jpg','2000','party','Jan 27 - 28, 2018 at 9:00am - 4:00pm IST').__dict__)
    #top events
    events.append(Event('Karthik Kumars Blood Chutney','Karthik kumars Blood Chutney','Museum Theatre, No 406, Pantheon Road, Egmore, Chennai','https://static.wixstatic.com/media/46cd01_42eed1bba2db4cfe8bb42e08d8878316~mv2.jpg/v1/fill/w_880,h_495,q_85,usm_0.66_1.00_0.01/46cd01_42eed1bba2db4cfe8bb42e08d8878316~mv2.jpg','2000','comedy','Feb 10, 2018 at 7:00pm - 9:00pm IST').__dict__)        
    events.append(Event('Roadtrip & Backpacking to Himachal','Roadtrip & Backpacking to Himachal','IIT Madras','https://static.wixstatic.com/media/46cd01_ea55e20e3c1146209c96fddd5b09ef05~mv2.jpg/v1/fill/w_728,h_528,q_85,usm_0.66_1.00_0.01/46cd01_ea55e20e3c1146209c96fddd5b09ef05~mv2.jpg','2000','adventure','Feb 12 - 18, 2018 at 9:00am - 7:00pm IST').__dict__)
    events.append(Event("Women's Only Yelagiri Weekend Getaway","Women's Only Yelagiri Weekend Getaway",'Yelagiri','https://static.wixstatic.com/media/46cd01_3fee78763ff44bc08e93ed824d0bee74~mv2_d_2048_1365_s_2.jpg/v1/fill/w_880,h_587,q_85,usm_0.66_1.00_0.01/46cd01_3fee78763ff44bc08e93ed824d0bee74~mv2_d_2048_1365_s_2.jpg','2000','adventure','Jan 20 - 21, 2018 at 10:00am - 1:00pm IST').__dict__)
    events.append(Event('The Boarding Das Tour by Vir Das','The Boarding Das Tour by Vir Das','Phoenix MarketCity (Chennai)','https://static.wixstatic.com/media/46cd01_6b7aafb2d7964767a94c65e7fb313b8b~mv2.jpg/v1/fill/w_880,h_495,q_85,usm_0.66_1.00_0.01/46cd01_6b7aafb2d7964767a94c65e7fb313b8b~mv2.jpg','2000','standup','Jan 14, 2018 at 7:00pm - 10:00pm IST').__dict__)
    events.append(Event('RaGa Live For Bharathi Vidyalaya','RaGa Live For Bharathi Vidyalaya','Bharathi Vidyalaya Senior Secondary School','https://static.wixstatic.com/media/46cd01_719391c03b434f39b32c6419567805f4~mv2.jpg/v1/fill/w_384,h_216,q_85,usm_0.66_1.00_0.01/50cd01_719391c03b434f39b32c6419567805f4~mv2.jpg','2000','Concert','Jan 9, 2018 at 5:00pm - 7:00pm IST').__dict__)
    events.append(Event('Backpacking Roadtrip to Hampi','Backpacking Roadtrip to Hampi','Hampi, Karnataka','https://static.wixstatic.com/media/46cd01_3482dc2a4090413f8b0cb19d5860bc34~mv2.jpg/v1/fill/w_384,h_216,q_85,usm_0.66_1.00_0.01/46cd01_3482dc2a4090413f8b0cb19d5860bc34~mv2.jpg','2000','adventure','Jan 27 - 28, 2018 at 9:00am - 3:00pm IST').__dict__)        

def get_data(start_index,end_index):
    result = []
    for index in range(len(events)):
        if index >= start_index and index <= end_index:
            result.append(events[index])
    return result

load_data()