#from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
#from django.shortcuts import render_to_response
import MySQLdb

def get_game_name(request,game_name):
    conn = MySQLdb.connect(host = "boardspot.mysql.pythonanywhere-services.com",
            user = "boardspot",
            passwd = "kyleandnick",
            db = "boardspot$boardsp0t")
    cursor = conn.cursor()
    cursor.execute("SELECT real_name,youtube,number_of_players,suggested_age,ept,genre,description FROM game WHERE game_name = '" +game_name+"'")
    if cursor.rowcount == 0:
        cursor.execute("SELECT real_name FROM game") #added
        row = cursor.fetchall() #added
       # html = "<html><body>There is no game names %s</body></html>"%game_name
        t = get_template('notfound.html') #added
        c = Context({'gname': game_name, 'real_name': row[0]}) #added
        html = t.render(c) #added
    else:
        row = cursor.fetchone()
       # html = "<html><body>The Game name is %s.</body></html>"%row[0]
        t = get_template('gname.html')
        #t = get_template('Game name is {{game_name}}.') #can delete
        c = Context({'real_name': row[0], 'youtube': row[1], 'nop': row[2], 'suggage': row[3],'ept': row[4],'genre': row[5],'descrip':row[6]})
        html = t.render(c)
    return HttpResponse(html)


