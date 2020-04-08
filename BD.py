from peewee import *
from PyQt5.QtWidgets import *

db = SqliteDatabase('bd.db')


class Material(Model):
    name = CharField()  # название материала
    company = TextField()  # фирма
    store = TextField()  # магазин
    supplier = TextField()  # поставщик
    reckoning = BooleanField()  # наличие счета да/нет
    ndc = BooleanField()  # наличие ндс да/нет
    count = BigIntegerField()  # количество взятых материалов
    price = DoubleField()  # цена общая

    class Meta:
        database = db  # модель базы данных


class Facility(Model):
    owner = ForeignKeyField(Material, related_name='facilities')  # связь между таблицами
    name = CharField()  # кто взял материалы
    facility = TextField()  # объект на который ушли материалы
    reckoning = BooleanField()  # наличие счета да/нет
    waybills = BooleanField()  # наличие накладные да/нет
    count = BigIntegerField()  # количество взятых материалов

    class Meta:
        database = db  # модель базы данных


class Orm():
    def __init__(self):
        Material.create_table()
        Facility.create_table()

    def getmat(self, id):
        r = Material.get(Material.id == id)
        return r

    def getfac(self, id):
        r = Facility.get(Facility.id == id)
        return r

    def allmat(self):
        r = []
        for mat in Material.select():
            id = mat.id
            name = mat.name
            company = mat.company
            store = mat.store
            supplier = mat.supplier
            if mat.reckoning:
                reckoning = "Да"
            else:
                reckoning = "Нет"
            if mat.ndc:
                ndc = "Да"
            else:
                ndc = "Нет"
            count = mat.count
            price = mat.price

            r.append((id, name, company, store, supplier, reckoning, ndc, count, price))
            # print(mat.id, mat.name, mat.company, mat.store, mat.supplier, mat.reckoning, mat.ndc, mat.count, mat.price)
        return r

    def addmater(self, name, company, store, supplier, reckoning, ndc, count, price):
        Material.create(name=name, company=company, store=store, supplier=supplier, reckoning=reckoning, ndc=ndc,
                        count=count, price=price)

    def addfacil(self, owner, name, facility, reckoning, waybills, count):
        r = Material.get(Material.id == owner)
        if r.count < count:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("на складе меньше чем вы берете")
            msg.addButton('Ок', QMessageBox.RejectRole)
            msg.exec()
            # print("на складе меньше чем вы берете")
        else:
            r.count = r.count - count
            r.save()
            Facility.create(owner=owner, name=name, facility=facility, reckoning=reckoning, waybills=waybills,
                            count=count)

    def delmat(self, id):
        r = Material.get(Material.id == id)
        r.delete_instance(recursive=True)

    def delfac(self, id):
        r = Facility.get(Facility.id == id)
        r.delete_instance()

    def allfac(self, id):
        r = []
        for fac in Facility.select().where(Facility.owner == id):
            id = fac.id

            name = fac.name
            facility = fac.facility
            if fac.reckoning:
                reckoning = "Да"
            else:
                reckoning = "Нет"
            if fac.waybills:
                waybills = "Да"
            else:
                waybills = "Нет"
            count = fac.count

            r.append((id, name, facility, reckoning, waybills, count))

        return r

    def search_mater(self, info):
        r = []
        for mat in Material.select().where(Material.name.contains(info)):
            id = mat.id
            name = mat.name
            company = mat.company
            store = mat.store
            supplier = mat.supplier
            if mat.reckoning:
                reckoning = "Да"
            else:
                reckoning = "Нет"
            if mat.ndc:
                ndc = "Да"
            else:
                ndc = "Нет"
            count = mat.count
            price = mat.price

            r.append((id, name, company, store, supplier, reckoning, ndc, count, price))
            # print(mat.id, mat.name, mat.company, mat.store, mat.supplier, mat.reckoning, mat.ndc, mat.count, mat.price)
        return r

