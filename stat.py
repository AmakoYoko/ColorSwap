from pymysql.converters import conversions
import pymysql
from header import *



client = Bot(command_prefix=BOT_PREFIX)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):


    db = pymysql.connect(host='',
                     user='',
                     passwd='',
                     db='',
                     charset='',
                     conv=conversions
                    )

    cursor = db.cursor()

    content = message.content.encode('utf8')
    author = str(message.author)
    authorid = message.author.id.encode('utf8')
    server = str(message.server)
    serverid = message.server.id.encode('utf8')


    print(content)
    print(author)
    print(authorid)
    print(server)
    print(serverid)



    sql= ("""INSERT INTO stats(content, author, authorid, server, serverid) VALUES (%s, %s, %s, %s, %s)""", (content, author, authorid, server, serverid))

    cursor.execute(*sql)
    cursor.close()
    db.commit()

    db.close()


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            db = pymysql.connect(host='',
                                 user='',
                                 passwd='',
                                 db='',


                                )

            cursor = db.cursor()

            servername = str(server.name)
            server = str(server.id)
            #sql= ("""INSERT INTO server(servername, serverid) VALUES (%s, %s)""", (servername, server))
            #cursor.execute(*sql)


            selectsql= ("""SELECT serverid FROM `server` WHERE serverid = %s""", (server))
            cursor.execute(*selectsql)

            rows = cursor.fetchall()

            try:
                rowtest = str(rows[0])
            except:
                rowtest = "00000000000000000"


            print(rowtest[2:20])
            if rowtest[2:20] == server:
                print("ok")
            else:

                try:

                    sqlsdel= ("""DELETE FROM `server` WHERE `serverid` = %s""", (server))
                    cursor.execute(*sqlsdel)
                    db.commit()
                except:

                    print("ajout")
                    sqlsadd= ("""INSERT INTO server(servername, serverid) VALUES (%s, %s)""", (servername, server))
                    cursor.execute(*sqlsadd)
                    db.commit()
            db.close()



        await asyncio.sleep(1)


client.loop.create_task(list_servers())

client.run(TOKEN)
