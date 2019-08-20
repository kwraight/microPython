# Complete project details at https://RandomNerdTutorials.com

def web_page(name,dicts):
    '''
    if led.value() == 1:
        gpio_state="ON"
    else:
        gpio_state="OFF"
    '''
                    
    html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
                border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
                .button2{background-color: #4286f4;}</style></head><body> <h1>Julie is gorgeous and...</h1>
                <p><strong>""" + name + """</strong> is the best 123! </p>
                    <p><a href="/?led=kene"><button class="button">Kenny</button></a></p>
                    <p><a href="/?led=juli"><button class="button">Julie</button></a></p>
                    <p><a href="/?led=madi"><button class="button">Madeleine</button></a></p>
                    <p><a href="/?led=anni"><button class="button">Annabel</button></a></p>
                    <p><a href="/?led=xavi"><button class="button">Xavier</button></a></p>
                    </body></html>"""
    html+="""<p>"""
    for d in dicts:
        html+="""{"""+d['nix']+""":"""+str(d['x'])+"""}"""
    html+="""</p>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

dicts=[]
dicts.append({'name':"Kenny",'nix':'kene','x':0})
dicts.append({'name':"Julie",'nix':'juli','x':0})
dicts.append({'name':"Madeleine",'nix':'madi','x':0})
dicts.append({'name':"Annabel",'nix':'anni','x':0})
dicts.append({'name':"Xavier",'nix':'xavi','x':0})

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    named="NYS"
    for d in dicts:
        best = request.find('/?led='+d['nix'])
        if best == 6:
            print(d['name']+' TOGGLED (by '+d['nix']+')')
            d['x']+=1
            named=d['name']
            led.value(not led.value())
            break
    response = web_page(named,dicts)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    try:
        conn.sendall(response)
    except OSError:
        print("not right now!")
    conn.close()

