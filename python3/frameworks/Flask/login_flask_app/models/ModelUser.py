from .adm.User import User



class ModelUser():
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.cursor()
            query = """SELECT id, username, password, fullname FROM user 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(query)
            row = cursor.fetchone()
            #si hay un usuario con ese nombreuser
            if row != None:
                #si hay valido el password con el de la base de datos y retorno el usuario logeado
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            
            #si no retorno Nulo
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    #obtener usuario no por nombreuser si no por id 
    @classmethod
    def user_por_id(self, db, id):
        try:
            cursor = db.cursor()
            query = "SELECT id, username, fullname FROM user WHERE id = {}".format(id)
            cursor.execute(query)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
