from sqlalchemy import select
from core import user_table

result = select([user_table])
result2 = select([user_table]).where(user_table.c.nome == 'daniel')

for x in result.execute():
    print(x)

# print([x for x in result2.execute()])
# # print([x for x in result.execute()])

# print([x for x in select([user_table]).execute()])