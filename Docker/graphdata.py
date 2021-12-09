# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from neo4j import GraphDatabase #ademas del oficial tambien estan: py2neo y neomodel

def chekConecction(session):
    try:
        session.run("Match () Return 1 Limit 1")
        print('ok')
        return True
    except Exception:
        print('not ok')
        return False

def showAllData(session):
    graph=session.run("MATCH (node) RETURN node LIMIT 20")
    for node in graph:
        print(node)

def main():
    #time.sleep(10)

    driver = GraphDatabase.driver("bolt://"+'neo4j'+":7687") #--env=NEO4J_AUTH=none para evitar la autenticación
    session = driver.session()

    tries = 0
    while not chekConecction(session) and tries<6: #darle tiempo a neo4j para que se encienda
        time.sleep(5)
        tries+=1

    #Exekutatu kontsulta
    q1="SHOW DATABASES"
    result = session.run(q1)
    #Emaitzak prosezatu
    for record in result:
        print(record['name'],record['currentStatus']) #leer estado de las bases de datos

    with open('movies.cypher', 'r') as file:
        data = file.read()

    session.run(data)
    showAllData(session)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()