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
    allCount = BigIntegerField()  # общее число материалов по договору
    measure = CharField()  # ед.изм
    price = DoubleField()  # цена за ед.
    allprice = DoubleField()  # цена общая

    class Meta:
        database = db  # модель базы данных


class Facility(Model):
    owner = ForeignKeyField(Material, related_name='facilities')  # связь между таблицами
    name = CharField()  # кто взял материалы
    facility = TextField()  # объект на который ушли материалы
    reckoning = BooleanField()  # наличие счета да/нет
    waybills = BooleanField()  # наличие накладные да/нет
    count = BigIntegerField()  # текущие число взятых материалов
    measure = CharField()  # ед.изм
    class Meta:
        database = db  # модель базы данных


class Responsible(Model):
    name = CharField()  # имя
    family = CharField()  # фамилия
    patronymic = CharField()  # отчество
    position = CharField()  # должность

    class Meta:
        database = db  # модель базы данных


class ConstructionObject(Model):
    facility = CharField()  # объект
    address = CharField()  # адрес
    contract = CharField()  # договор

    class Meta:
        database = db  # модель базы данных


class Orm():
    def __init__(self):
        Material.create_table()
        Facility.create_table()
        Responsible.create_table()
        ConstructionObject.create_table()

    def getmat(self, id):
        r = Material.get(Material.id == id)
        return r

    def getfac(self, id):
        r = Facility.get(Facility.id == id)
        return r
    def getres(self, id):
        r = Responsible.get(Responsible.id == id)
        return r
    def getcons(self, id):
        r = ConstructionObject.get(ConstructionObject.id == id)
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
            allCount = mat.allCount
            measure = mat.measure
            price = mat.price
            allprice = mat.allprice

            r.append((id, name, company, store, supplier, reckoning, ndc, count, allCount,measure, price, allprice))
        return r

    def allres(self):
        r = []
        for mat in Responsible.select():
            id = mat.id
            name = mat.name
            family = mat.family
            patronymic = mat.patronymic
            position = mat.position

            r.append((id, name, family, patronymic, position))

        return r

    def allcon(self):
        r = []
        for mat in ConstructionObject.select():
            id = mat.id
            facility = mat.facility
            address = mat.address
            contract = mat.contract
            r.append((id, facility, address, contract))

        return r

    def addmater(self, name, company, store, supplier, reckoning, ndc, count,measure, price ):
        Material.create(name=name, company=company, store=store, supplier=supplier, reckoning=reckoning, ndc=ndc,
                        count=count, allCount=count,measure=measure, price=price, allprice=count * price)

    def addres(self, name, family, patronymic, position):
        Responsible.create(name=name, family=family, patronymic=patronymic, position=position)

    def addcon(self, facility, address, contract):
        ConstructionObject.create(facility=facility, address=address, contract=contract)

    def addfacil(self, owner, name, facility, reckoning, waybills, count,measure):
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
                            count=count,measure=measure)

    def delmat(self, id):
        r = Material.get(Material.id == id)
        r.delete_instance(recursive=True)

    def delfac(self, id):
        r = Facility.get(Facility.id == id)
        r.delete_instance()

    def delres(self, id):
        r = Responsible.get(Responsible.id == id)
        r.delete_instance()

    def delcon(self, id):
        r = ConstructionObject.get(ConstructionObject.id == id)
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
            measure = fac.measure

            r.append((id, name, facility, reckoning, waybills, count,measure))

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
            allCount = mat.allCount
            measure = mat.measure
            price = mat.price
            allprice = mat.allprice

            r.append((id, name, company, store, supplier, reckoning, ndc, count, allCount,measure, price, allprice))

        return r

    def search_res(self, info):
        r = []
        for mat in Responsible.select().where(Responsible.name.contains(info)):
            id = mat.id
            name = mat.name
            family = mat.family
            patronymic = mat.patronymic
            position = mat.position

            r.append((id, name, family, patronymic, position))

        return r

    def search_cons(self, info):
        r = []
        for mat in ConstructionObject.select().where(ConstructionObject.facility.contains(info)):
            id = mat.id
            facility = mat.facility
            address = mat.address
            contract = mat.contract
            r.append((id, facility, address, contract))

        return r
    def resfacil(self, fio):
        r = []
        for fac in Facility.select().where(Facility.name == fio):
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
            measure = fac.measure

            r.append((id, name, facility, reckoning, waybills, count,measure ))
        return r

    def consfacil(self, facil):
        r = []
        for fac in Facility.select().where(Facility.facility == facil):
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
            measure = fac.measure

            r.append((id, name, facility, reckoning, waybills, count,measure ))
        return r
    def allresname(self):
        r = []
        for mat in Responsible.select():
            name = mat.name
            family = mat.family
            patronymic = mat.patronymic

            fio = name + " " + family[0] + ". " + patronymic[0] + '.'
            r.append(fio)

        return r

    def allconname(self):
        r = []
        for mat in ConstructionObject.select():
            facility = mat.facility
            r.append(facility)
        return r
    def getmatwes(self, id):
        res = Material.get(Material.id == id)
        r=res.measure
        return r

bd=Orm()
bd.addmater(12,2,21,12,123,41,231,13,1335)
print(bd.allmat())
# bd.addcon("Zavod", "2", "31")
# bd.addcon("Zavod2", "2", "31")
# bd.addcon("Zavod3", "2", "31")
# bd.addres("Ivanov", "21", "12", "12")
# bd.addres("Ivanov2", "21", "12", "12")
# bd.addres("Ivanov3", "21", "12", "12")

