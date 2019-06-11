import sqlite3

class Sqlite3ORM:
    fields = []
    dbpath = ""
    dbtable = ""
    create = ""

    def __init__(self):
        raise NotImplementedError
    
    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()

    @classmethod
    def _create_insert(cls):
        columnlist = ", ".join(cls.fields)
        qmarks = ", ".join("?" for val in cls.fields)
        SQL = """ INSERT INTO {tablename} ({columnlist})
        VALUES ({qmarks}) """
        return SQL.format(tablename=cls.dbtable, columnlist=columnlist, qmarks=qmarks)

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            SQL = self._create_insert()
            propvals = [getattr(self, propname) for propname in self.fields]

            cur.execute(SQL, propvals)
            self.pk = cur.lastrowid
    
    @classmethod
    def _create_update(cls):
        columnlist = ", ".join(cls.fields)
        qmarks = ", ".join("?" for val in cls.fields)
        SQL = "UPDATE {tablename} SET ({columnlist}) WHERE pk=?"
        return SQL.format(tablename=cls.dbtable, columnlist=columnlist, qmarks=qmarks)
    
    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            SQL = self._create_update()
            propvals = [getattr(self, propname) for propname in self.fields]
            cur.execute(SQL, propvals, self.pk)

    #     """ TODO: IMPLEMENT THIS. Execute the update statement. Remember that
    #     you will also have to provide self.pk for that ? in addition to the
    #     field values. """