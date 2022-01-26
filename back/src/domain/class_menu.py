import sqlite3


class Menu:
    def __init__(self, id, desc):
        self.id=id
        self.desc= desc

    def to_dict(self):
        return {"id": self.id, "desc": self.desc}


class MenuRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists menu_dia (
                id varchar,
                desc varchar
            )
        """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from menu_dia"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        dict_menu = []
        for item in data:
            menu_class = Menu(
                id= item["id"], desc=item["desc"]
            )
            dict_menu.append(menu_class)
        return dict_menu

    def save(self, menu):
        sql = """insert into menu_dia (id, desc) values (
            :id, :desc
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, menu.to_dict())
        conn.commit()
