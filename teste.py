print('Primeiro programa Python 2')


def update_or_create_company(self, company):
        cursor = self.connection.cursor()
        sql = f"""
            INSERT INTO FILIAIS_ALFA
            VALUES (
                DEFAULT,
                '{company.cnpj}',
                '{company.nome}',
                '{company.cidade}',
                '{company.estado}'
            )
            ON CONFLICT (cnpj)
                DO
                UPDATE SET
                    nome = '{company.nome}',
                    cidade = '{company.cidade}',
                    estado = '{company.estado}'
        """

        try:
            cursor.execute(sql)
            self.connection.commit()
          print(
                f'O CNPJ {company.cnpj} foi inserido com sucesso na base de dados!'
            )
        cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
    print("Error: %s" % error)
    self.connection.rollback()
    cursor.close()