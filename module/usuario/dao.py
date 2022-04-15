import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO USUARIO(nome, senha, idade) values(%s, %s, %s) returning id'
SCRIPT_SQL_SELECT = 'SELECT * FROM USUARIO'


class UsuarioDao:
  def __init__(self, connectDataBase):
    self.connectDataBase = connectDataBase

  def save(self, usuario):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_INSERT, usuario.get_values_save())
    id = cursor.fetchone()[0]
    self.connectDataBase.connect.commit()
    cursor.close()
    usuario.set_id(id)

    return usuario
  

  def get_allUsers(self):
    usuarios = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT)
    columns_name = [column[0] for column in cursor.description]
    usuario_cursor = cursor.fetchone()
    while usuario_cursor:
      usuario = dict(zip(columns_name, usuario_cursor))
      usuario_cursor = cursor.fetchone()
      usuarios.append(usuario)
    cursor.close()

    return usuarios