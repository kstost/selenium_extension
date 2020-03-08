import sqlite3
class EasySQLite:
    def __init__(self,file=None):
        self.__sqlite3 = sqlite3
        if not file:
            self.__con = self.__sqlite3.connect(':memory:')
        else:
            self.__con = self.__sqlite3.connect(file)
        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
        self.__con.row_factory = dict_factory
        super().__init__()

    def close(self):
        self.__con.close()
        
    def get_cursor(self):
        return self.__con.cursor()

    def tables(self):
        tables = self.query("SELECT name FROM sqlite_master WHERE type='table';")
        lst = []
        for table in tables:
            lst.append(table['name'])
        return lst

    def query(self, sql, data=None):
        cur = self.get_cursor()
        if data:
            data_type = type(data)
            if data_type == tuple or data_type == dict:
                cur.execute(sql, data)
            elif data_type == list:
                cur.executemany(sql, data)
        else:
            cur.execute(sql)
        if not (sql.strip().lower().find('select ') == 0):
            # case of DML(Data Manipulation Language)
            self.__con.commit()
            return cur
        else:
            result = []
            for row in cur.fetchall():
                result.append(dict(row))
            return result
if __name__ == '__main__':
    pass