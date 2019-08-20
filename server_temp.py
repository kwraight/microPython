# Complete project details at https://RandomNerdTutorials.com

def web_page(dicts):
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
                .button2{background-color: #4286f4;}</style></head><body> <h1>buttons</h1>"""
                    
    for d in dicts:
        html+="""<p><strong>""" + d['name'] + """, state: """+d['state']+"""</strong> ! </p>
            
            <p><a href="/?led="""+d['name']+""""><button class="button">"""+d['name']+"""</button></a></p>"""
                    
    html+="""</body></html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

dicts=[]
dicts.append({'name':"toggle",'state':'off'})

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

