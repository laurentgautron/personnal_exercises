import psycopg2


class Product:

    CATEGORY = ['fruits', 'légumes', 'féculents', 'viandes', 'poissons', 'boulangerie', 'patisserie', 'sucreries',
                'boissons', 'hygiène', 'entretiens', 'chats']
    SUBCATEGORY = ['pommes', 'poires', 'chocolat', 'pain', 'boeuf', 'porc', 'saumon']

    @staticmethod
    def insert_product():
        product_name = input('rentrez le nom du produit: ')
        for counter, values in enumerate(Product.CATEGORY):
            print(counter + 1, '-', values)
        product_category = input('choisir une catégorie ( ou rentrer une nouvelle si vous ne la trouvez pas dans \
                                  la liste: ')
        if Product.CATEGORY[int(product_category)] not in Product.CATEGORY:
            Product.CATEGORY.append(product_category)
        else:
            product_category = Product.CATEGORY[int(product_category)]
        for counter, values in enumerate(Product.SUBCATEGORY):
            print(counter + 1, '-', values)
        sub_category = input('choisir une sous_catégorie ( ou rentrer une nouvelle si vous ne la trouvez pas dans \
                                  la liste: ')
        if (int(sub_category) not in range(0, len(Product.CATEGORY))) and (sub_category not in Product.SUBCATEGORY):
            Product.SUBCATEGORY.append(sub_category)
        else:
            sub_category = Product.SUBCATEGORY[int(sub_category)]
        processed_food = True
        transform = input('la nourriture est-elle transformée (o/n)?, ')
        if transform == 'n':
            processed_food = False
        return product_name, product_category, sub_category, processed_food

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS product (
                        product_id serial PRIMARY KEY,
                        product_name VARCHAR(100),
                        product_category VARCHAR(100),
                        sub_category VARCHAR(100),
                        processed_food BOOLEAN)"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

    def insert(self):
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_insert = """INSERT INTO product(product_name, product_category, sub_category, processed_food)
                        VALUES(%s, %s, %s, %s)"""
        cur.execute(sql_insert, self.insert_product())
        conn.commit()
        cur.close()
        conn.close()
