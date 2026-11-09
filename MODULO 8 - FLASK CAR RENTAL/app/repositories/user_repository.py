# This repository handles all database operations related to users.
# Before: SQL queries were written directly inside the route endpoints.
# Now: The route only receives the request and calls this repository.
# This follows the separation of concerns principle (routes = waiter, repository = kitchen).

from app.database import get_connection

def create_user(name, email, username, password, birth_date, account_status="active"):
    """
    Inserts a new user into the database and returns the created user.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO lyfter_car_rental.users 
                (name, email, username, password, birth_date, account_status)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id, name, email, username, birth_date, account_status;
        """, (name, email, username, password, birth_date, account_status))

        user = cur.fetchone()
        conn.commit()

        return {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "username": user[3],
            "birth_date": str(user[4]),
            "account_status": user[5]
        }

    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def get_users(filters=None):
    """
    Returns a list of users. Can receive optional filters.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
            SELECT id, name, email, username, birth_date, account_status 
            FROM lyfter_car_rental.users
        """
        values = []
        conditions = []

        allowed_columns = ["id", "name", "email", "username", "birth_date", "account_status"]

        if filters:
            for column, value in filters.items():
                if column in allowed_columns:
                    conditions.append(f"{column} = %s")
                    values.append(value)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY id"

        cur.execute(query, values)
        rows = cur.fetchall()

        users = []
        for row in rows:
            users.append({
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "username": row[3],
                "birth_date": str(row[4]),
                "account_status": row[5]
            })

        return users

    except Exception as e:
        raise e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def update_user_status(user_id, new_status):
    """
    Updates the account_status of a user.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE lyfter_car_rental.users
            SET account_status = %s
            WHERE id = %s
            RETURNING id, name, account_status;
        """, (new_status, user_id))

        user = cur.fetchone()

        if not user:
            return None

        conn.commit()

        return {
            "id": user[0],
            "name": user[1],
            "account_status": user[2]
        }

    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def flag_user_as_delinquent(user_id):
    """
    Sets the user account_status to 'delinquent'.
    """
    return update_user_status(user_id, "delinquent")