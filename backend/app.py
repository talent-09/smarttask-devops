from flask import Flask, request, jsonify
from flask_cors import CORS

import mysql.connector

import os


app = Flask(__name__)


# Autoriser le frontend à communiquer avec le backend
CORS(app)


def get_db_connection():

    connection = mysql.connector.connect(

        host=os.getenv(
            "DB_HOST",
            "mysql"
        ),

        user=os.getenv(
            "DB_USER",
            "bamba"
        ),

        password=os.getenv(
            "DB_PASSWORD",
            "bamba"
        ),

        database=os.getenv(
            "DB_NAME",
            "db_bamba"
        )

    )

    return connection


# --------------------------------------------------
# TEST DU BACKEND
# --------------------------------------------------

@app.route("/api/health", methods=["GET"])
def health():

    return jsonify({

        "status": "OK",

        "message":
            "Backend Flask fonctionne"

    })


# --------------------------------------------------
# CONNEXION
# --------------------------------------------------

@app.route("/api/login", methods=["POST"])
def login():

    data = request.get_json()


    if not data:

        return jsonify({

            "message":
                "Aucune donnée reçue"

        }), 400


    email = data.get("email")

    password = data.get("password")


    if not email or not password:

        return jsonify({

            "message":
                "Email et mot de passe obligatoires"

        }), 400


    connection = None

    cursor = None


    try:

        connection = get_db_connection()


        cursor = connection.cursor(
            dictionary=True
        )


        query = """

            SELECT id, email

            FROM users

            WHERE email = %s

            AND password = %s

        """


        cursor.execute(

            query,

            (
                email,
                password
            )

        )


        user = cursor.fetchone()


        if user:

            return jsonify({

                "message":
                    "Connexion réussie",

                "user": {

                    "id":
                        user["id"],

                    "email":
                        user["email"]

                }

            }), 200


        return jsonify({

            "message":
                "Email ou mot de passe incorrect"

        }), 401


    except mysql.connector.Error as error:

        print(
            "Erreur MySQL :",
            error
        )


        return jsonify({

            "message":
                "Erreur de connexion à MySQL"

        }), 500


    except Exception as error:

        print(
            "Erreur :",
            error
        )


        return jsonify({

            "message":
                "Erreur interne du serveur"

        }), 500


    finally:

        if cursor:

            cursor.close()


        if connection:

            connection.close()


# --------------------------------------------------
# LANCEMENT
# --------------------------------------------------

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=False

    )
