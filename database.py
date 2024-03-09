import aiosqlite
DB_NAME = 'quiz_bot.db'

async def create_table():
    # Создаем соединение с базой данных (если она не существует, она будет создана)
    async with aiosqlite.connect(DB_NAME) as db:
        # Создаем таблицу
        await db.execute('''CREATE TABLE IF NOT EXISTS quiz_state (user_id INTEGER PRIMARY KEY, question_index INTEGER)''')
        await db.execute('''CREATE TABLE IF NOT EXISTS top_score (user_id INTEGER PRIMARY KEY, top INTEGER, user_name VARCHAR(50))''')
        # Сохраняем изменения
        await db.commit()
async def alter_table():
    # Создаем соединение с базой данных (если она не существует, она будет создана)
    async with aiosqlite.connect(DB_NAME) as db:
        # Создаем таблицу
        #await db.execute('''CREATE TABLE IF NOT EXISTS quiz_state (user_id INTEGER PRIMARY KEY, question_index INTEGER)''')
        await db.execute('''ALTER TABLE top_score ADD user_name VARCHAR(50);''')
        # Сохраняем изменения
        await db.commit()
async def delete_table():
    # Создаем соединение с базой данных (если она не существует, она будет создана)
    async with aiosqlite.connect(DB_NAME) as db:
        # Создаем таблицу
        #await db.execute('''CREATE TABLE IF NOT EXISTS quiz_state (user_id INTEGER PRIMARY KEY, question_index INTEGER)''')
        await db.execute('''DELETE TABLE top_score;''')
        # Сохраняем изменения
        await db.commit()
async def get_quiz_index(user_id):
     # Подключаемся к базе данных
     async with aiosqlite.connect(DB_NAME) as db:
        # Получаем запись для заданного пользователя
        async with db.execute('SELECT question_index FROM quiz_state WHERE user_id = (?)', (user_id, )) as cursor:
            # Возвращаем результат
            results = await cursor.fetchone()
            if results is not None:
                return results[0]
            else:
                return 0

async def get_top_index(user_id):
     async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT top FROM top_score WHERE user_id = (?)', (user_id, )) as cursor:
            results = await cursor.fetchone()

            if results is not None:
                return results[0]
            else:
                return 0

async def get_top_score():
     async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT user_name, top FROM top_score ORDER BY top DESC LIMIT 5') as cursor:
            results = await cursor.fetchall()
            results=str(results)
            #print(results)
            if results is not None:
                return results
            else:
                return 0


async def update_quiz_index(user_id, index):
    # Создаем соединение с базой данных (если она не существует, она будет создана)
    async with aiosqlite.connect(DB_NAME) as db:
        # Вставляем новую запись или заменяем ее, если с данным user_id уже существует
        await db.execute('INSERT OR REPLACE INTO quiz_state (user_id, question_index) VALUES (?, ?)', (user_id, index))
        # Сохраняем изменения
        await db.commit()
async def update_top_index(user_id, index, user_name):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('INSERT OR REPLACE INTO top_score (user_id, top, user_name) VALUES (?, ?, ?)', (user_id, index, user_name))
        await db.commit()
