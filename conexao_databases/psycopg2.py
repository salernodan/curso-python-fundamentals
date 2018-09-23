import psycopg2
from pprint import pprint
ip, base, user, senha = 'localhost', 'fundamentals', 'admin', '4linux'
try:
    con = psycopg2.connect(
        'host={} dbname={} user={} password={}'.format(
            ip, base, user, senha
        ))
except Exception as e:
    print("Erro:{}".format(e))
    exit()
try:
    cur = con.cursor()
    cur.execute("select * from usuarios;")
    for x in cur.fetchall():
        print('''
        ID:  {:.>10}
        Nome: {:.>9}
        Idade: {:.>8}
        '''.format(x[0], x[1], x[2]))
    # print(cur.fetchone())
    # cur.execute("update usuarios set nome='daniel' where id=1;")
    # cur.execute("insert into usuarios\
    # (nome, idade) values ('joana', 52);")

    con.commit()

    cur.close()
    con.close()
except Exception as e:
    print('Erro:{}'.format(e))
    con.rollback()