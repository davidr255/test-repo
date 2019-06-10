## GENERIC SQL STATEMENTS

def create_delete(tablename):
	return "DELETE FROM {} WHERE pk = ?".format(tablename)

def create_insert(tablename, columnnames):
	return "INSERT INTO {} (columnnames) VALUES (?);".format(tablename)

    """ RETURN the SQL string you would pass to cursor.execute, including ?s
in the right places. """

def create_update(tablename, columnames):
	return "UPDATE {} SET columnnames WHERE pk = ?".format(tablename)

    """ RETURN the SQL string you would pass to cursor.execute, including ?s
in the right places. Assume this update is updating a row with pk=?"""
