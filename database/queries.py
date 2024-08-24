class Queries:
    saving_survey_results = """
        CREATE TABLE IF NOT EXISTS review_dialog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone_number TEXT,
            visit_date  INTEGER,
            food_rating INTEGER, 
            cleanliness_rating INTEGER,
            extra_comments TEXT
        )
    """

    create_table_categories = """
    CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    UNIQUE(name)
    )
    """

    create_table_dishes = """
    CREATE TABLE IF NOT EXISTS dishes (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     title TEXT,
     price INTEGER,
     photo TEXT,
     category_id INTEGER,
     FOREIGN KEY (category_id) REFERENCES category(id),
     UNIQUE(title)
     )
    """

    insert_into_categories = """
    INSERT OR IGNORE INTO categories(name) VALUES 
    ('drinks'), ('roast'), ('soup')
    """

    insert_into_dishes = """
    INSERT OR IGNORE INTO dishes(title,price,photo,category_id) VALUES ('Курдак', '210', 'images/kurdak.jpg', 2),
    ('Гороховый суп', '160', 'images/pea_soup.jpg', 3),
    ('Смузи', '100', 'images/cmuzy.jpg', 1),
    """
