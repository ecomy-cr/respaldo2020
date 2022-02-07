import sqlite3

mycon = sqlite3.connect('database_prueba.db')
mycur = mycon.cursor()
query = 'INSERT INTO primer_table (name, description, precio, foto, fotob) Values ( {},{},{},{},{} )'.format('Acetaminofen','Pastilla para inflamacion y infeccion','560','localhost/image/ace.png','localhost/image/ace2.png')
mycur.execute(query)
mycon.commit()
mycur = mycon.cursor()
query = 'Select * from primer_table'
mydata_products = mycur.execute(query)
#sacarlos directo
#for i in mydata_products:
    #print(i)#ver en consola para verificar
