import sqlite3
from .orm import Sqlite3ORM
from .position import Position
from .trade import Trade
from .util import get_price
import bcrypt
import random
import string

class InsufficientFundsError(Exception):
    pass

class InsufficientSharesError(Exception):
    pass


class User(Sqlite3ORM):

    fields = ['username', 'password', 'realname', 'balance', 'api_key']
    dbtable = "user_info"
    dbpath = "trader.db"

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.realname = kwargs.get('realname')
        self.balance = kwargs.get('balance', 0.0)
        self.api_key = kwargs.get('api_key')

    def hash_password(self, password):
        """ someuser.hash_password("somepassword") sets someuser's self.password
        to a bcrypt encoded hash """
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def generate_api_key(self):
        key = string.ascii_letters + string.digits
        self.api_key = ''.join(random.choice(key)for i in range(20))

    @classmethod
    def api_authenticate(cls, api_key):
        user = cls.one_where("api_key=?", (api_key, ))
        if user is None:
            return None
        if api_key == user.api_key:
            return user
        return None

    @classmethod
    def login(cls, username, passworde):
        """ search for the user with the given username (use one_where) and then
        use bcrypt's checkpw() to verify that the credentials are correct
        return None for bad credentials or the matching User instance on a
        successful login """
        user = cls.one_where("username=?", (username, ))
        if user is None:
            return None
        if bcrypt.checkpw(passworde.encode(), user.password):
            return user
        return None

    def all_positions(self):
        """ return all Positions for this user as a list """
        positions = Position.many_where("user_info_pk=?", (self.pk, ))
        return positions

    def position_for_stock(self, ticker):
        """ return a user's position in one stock or None """
        position = Position.one_where("user_info_pk=? AND ticker=?",
                                      (self.pk, ticker))
        return position

    def buy(self, ticker, amount):
        # TODO: make a trade (volume=amount), price = price of 1 share
        """ buy a stock. if there is no current position, create one, if there is
        increase its amount. no return value """
        if amount < 0:
            raise ValueError
        price = get_price(ticker)
        cost = price * amount
        if self.balance < cost:
            raise InsufficientFundsError
        self.balance -= cost
        current_position = self.position_for_stock(ticker)
        if current_position is None:
            current_position = Position(ticker=ticker,
                                        amount=0,
                                        user_info_pk=self.pk)
        trade = Trade(user_info_pk=self.pk,
                      ticker=ticker.lower(),
                      price=price,
                      volume=amount)
        current_position.amount += amount
        current_position.save()
        trade.save()
        self.save()

    def sell(self, ticker, amount):
        # TODO, make a trade (volume=-amount) price = price of 1 share
        if amount < 0:
            raise ValueError
        price = get_price(ticker)
        cost = price * amount
        position = self.position_for_stock(ticker)
        if position is None or amount > position.amount:
            raise InsufficientSharesError
        position.amount -= amount
        self.balance += cost
        trade = Trade(user_info_pk=self.pk,
                      ticker=ticker.lower(),
                      volume=-amount,
                      price=price)
        if position.amount == 0:
            position.delete()
        else:
            position.save()
        trade.save()
        self.save()

    def all_trades(self):
        """ return a list of Trade objects for every trade made by this user
        arranged oldest to newest """
        return Trade.many_where("user_info_pk=? ORDER BY time ASC",
                                (self.pk, ))

    def trades_for(self, ticker):
        """ return a list of Trade objects for each trade of a given stock for
        this user, arranged oldest to newest """
        return Trade.many_where(
            "user_info_pk=? AND ticker=? ORDER BY time ASC",
            (self.pk, ticker.lower()))

    @classmethod
    def richest(cls):
        return cls.many_where('ORDER BY balance DESC')[0] 