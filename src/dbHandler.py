import sqlite3 as sql
import config


def open_connection() -> sql.Connection | Exception:
    try: return sql.connect(config.DB_FILE, 3000)
    except Exception as err: print(err.with_traceback())

def close_connection(db: sql.Connection) -> None:
    db.close()


def init() -> None:
    db = open_connection()
    cursor = db.cursor()

    try:
        print('Setting up database ...')
        cursor.execute('''CREATE TABLE IF NOT EXISTS Games (
            game_id INTEGER PRIMARY KEY,
            time INTEGER,

        )''') # setup players table
        cursor.execute('') # setup games table
        db.commit()

    except Exception as err:
        print(err.with_traceback())
        raise

    finally:
        db.commit()
        cursor.close()
        close_connection(db)


def create_new_game(db) -> int:
    '''creates new game inside the group chat,
    cant create more than 1'''
    pass


def delete_game(db) -> bool:
    '''Deletes a game inside the group chat,
    returns False if no game found and True otherwise'''
    pass