#Bottle vmesnik python

import bottle
import model

bottle.TEMPLATE_PATH.insert(0, 'C:\\Users\\jakak\\Desktop\\Git\\Projekt_UVP\\views')

igra_xo = model.Igra_xo()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/igra/')
def nova_igra():
    id_igre = igra_xo.nova_igra()
    bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    return bottle.template('igra.tpl', 
    igra = igra_xo.igre[id_igre] ,
    naslednja = igra_xo.mreza_naslednja_2(id_igre),
    slaba = igra_xo.slaba_fun(id_igre), 
    zmaga = igra_xo.zmaga(id_igre),
    id_igre = id_igre) 

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    mreza = bottle.request.forms.get("mreza")

    if mreza is None : # če je mreža že določena
        mreza = igra_xo.mreza_naslednja_2(id_igre) 
    else:
        pass

    vrsta = bottle.request.forms.get("vrsta")
    stolpec = bottle.request.forms.get("stolpec")
    igra_xo.poteza_db_sl(id_igre, int(mreza), int(vrsta), int(stolpec)) #napaka int mreza , pomoje da prazno vrednost
    bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.post('/navodila/')
def pojdi_navodila():
    'Stran z navodili.'
    bottle.redirect('/navodila/')

@bottle.get('/navodila/')
def navodila():
    return bottle.template('navodila.tpl') #še naredi
    

@bottle.error(404)
def error404(error):
    return 'Nothing here, sorry'

# @bottle.get('/igra/<id_igre:int>/')
# def pokazi_igro(id_igre):
#     return bottle.template('igra.tpl', 
#     igra = vislice.igre[id_igre][0],
#     id_igre = id_igre,
#     poskus = vislice.igre[id_igre][1])


bottle.run(reloader=True, debug=True)