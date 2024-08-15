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