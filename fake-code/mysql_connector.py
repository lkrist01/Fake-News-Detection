import mysql.connector
from simhash import Simhash
class DBConnector:
    """
    Default DB constructor
    """
    def __init__(self,host,user,passwd,db):
        self._host=host
        self._user=user
        self._passwd=passwd
        self._db=db

    """
    Updates class conn variable with an open connection
    """
    def connect(self):
        mydb = mysql.connector.connect(
          host=self._host,
          user=self._user,
          passwd=self._passwd,
          database=self._db
        )
        self._conn = mydb

    def getHashes(self):
        mycursor = self._conn.cursor()
        mycursor.execute("SELECT id,hash FROM url")
        myresult = mycursor.fetchall()
        #returned in the correct format for Simhash()
        return [(str(item[0]),Simhash(int(item[1]))) for item in myresult if not item[1] is None]
    """
    Inserts the url and hash in the database
    :param url The url to be inserted
    :parma hash The hash of the url
    :return the id of the new record or None if nothing inserted
    """
    def insertHash(self,url,hash=None):
        mycursor = self._conn.cursor()
        mycursor.execute("SELECT COUNT(*) FROM url WHERE url= %s",(url,))
        if mycursor.fetchone()[0]>0:#return if we have already have this record in the db
            return None
        if not hash is None:
            sql = "INSERT INTO url(hash,url) VALUES(%s,%s)"
            val = (hash,url)
        else:
            sql = "INSERT INTO url(url) VALUES(%s)"
            val = (url,)
        mycursor.execute(sql,val)
        self._conn.commit()
        return mycursor.lastrowid

    """
    Updates the database with the duplicates
    :param articleUrl the url of the duplicate article
    :param urlID the url found in our databases matching
    """
    def insertDuplicates(self,articleUrl,urlID):
        newArticleID = self.insertHash(articleUrl)
        if newArticleID is None:
            return
        mycursor = self._conn.cursor()
        query = "SELECT COUNT(*) FROM duplicate_url WHERE url_id=%s and duplicate_url_id=%s"
        # import pdb;pdb.set_trace()
        mycursor.execute(query,(newArticleID,int(urlID)))
        if newArticleID==urlID or mycursor.fetchone()[0]>0:#to avoid any kind of duplicates
            return
        query = "INSERT INTO duplicate_url(url_id,duplicate_url_id) VALUES(%s,%s)"
        mycursor.execute(query,(newArticleID,int(urlID)))
        self._conn.commit()
