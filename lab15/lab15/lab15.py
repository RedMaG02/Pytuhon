import sqlite3

try:
    connection = sqlite3.connect('data.sqlite')
    print('DB connected')
except:
    print('DB error')

cursorObj = connection.cursor()

def sql_insertDutyList(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO DutyList (ID, StoreKeeperID, SumTime, ShiftAmount) VALUES(?, ?, ?, ?)', entities)
    con.commit()
    

def sql_insertItems(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO Items (ID, ProductID, Amount, WayBillID) VALUES(?, ?, ?, ?)', entities)
    con.commit()

def sql_insertOrders(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO Orders (ID, tDate, OrderStatus, WayBillID, StoreKeeperID, SubjectRecID, SubjectSupID) VALUES(?, ?, ?, ?,?,?,?)', entities)
    con.commit()

def sql_insertProducts(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO Products (ID, ProductName, Price, ProductWeight, Amount) VALUES(?, ?, ?, ?,?)', entities)
    con.commit()

def sql_insertReceivers(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO Receivers (ID, Email, telephoneNumber) VALUES(?, ?, ?)', entities)
    con.commit()

def sql_insertSuppliers(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO Suppliers (ID, Email, telephoneNumber) VALUES(?, ?, ?)', entities)
    con.commit()

def sql_insertStoreKeepers(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO StoreKeepers (ID, FullName, telephoneNumber) VALUES(?, ?, ?)', entities)
    con.commit()

def sql_insertWayBills(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO WayBills (ID, DescriptionWB) VALUES(?, ?)', entities)
    con.commit()

cursorObj.execute('DELETE FROM Receivers')
connection.commit()
sql_insertReceivers(connection, [1, '1mail@.com', '79528119291'])
sql_insertReceivers(connection, [2, '2mail@.com', '79528119292'])
sql_insertReceivers(connection, [3, '3mail@.com', '79528119293'])
sql_insertReceivers(connection, [4, '4mail@.com', '79528119294'])
sql_insertReceivers(connection, [5, '5mail@.com', '79528119295'])
sql_insertReceivers(connection, [6, '6mail@.com', '79528119296'])
sql_insertReceivers(connection, [7, '7mail@.com', '79528119297'])
sql_insertReceivers(connection, [8, '8mail@.com', '79528119298'])
sql_insertReceivers(connection, [9, '9mail@.com', '79528119299'])
sql_insertReceivers(connection, [10, '10mail@.com', '79528119200'])


cursorObj.execute('DELETE FROM Suppliers')
connection.commit()
sql_insertSuppliers(connection, [1, '11mail@.com', '71528119291'])
sql_insertSuppliers(connection, [2, '22mail@.com', '72528119292'])
sql_insertSuppliers(connection, [3, '33mail@.com', '73528119293'])
sql_insertSuppliers(connection, [4, '44mail@.com', '74528119294'])
sql_insertSuppliers(connection, [5, '55mail@.com', '75528119295'])
sql_insertSuppliers(connection, [6, '66mail@.com', '76528119296'])
sql_insertSuppliers(connection, [7, '77mail@.com', '77528119297'])
sql_insertSuppliers(connection, [8, '88mail@.com', '78528119298'])
sql_insertSuppliers(connection, [9, '99mail@.com', '71128119299'])
sql_insertSuppliers(connection, [10, '1010mail@.com', '72228119200'])

cursorObj.execute('DELETE FROM Products')
connection.commit()
sql_insertProducts(connection, [1, 'Bolt1', 10,1,100])
sql_insertProducts(connection, [2, 'Bolt2', 11,2,101])
sql_insertProducts(connection, [3, 'Bolt3', 12,3,102])
sql_insertProducts(connection, [4, 'Bolt4', 13,4,103])
sql_insertProducts(connection, [5, 'Bolt5', 14,5,104])
sql_insertProducts(connection, [6, 'Bolt6', 15,6,105])
sql_insertProducts(connection, [7, 'Bolt7', 16,7,106])
sql_insertProducts(connection, [8, 'Bolt8', 17,8,107])
sql_insertProducts(connection, [9, 'Bolt9', 18,9,108])
sql_insertProducts(connection, [10, 'Bolt10', 19,10,109])

cursorObj.execute('DELETE FROM WayBills')
connection.commit()
sql_insertWayBills(connection, [1, 'somedesc1'])
sql_insertWayBills(connection, [2, 'somedesc2'])
sql_insertWayBills(connection, [3, 'somedesc3'])
sql_insertWayBills(connection, [4, 'somedesc4'])
sql_insertWayBills(connection, [5, 'somedesc5'])
sql_insertWayBills(connection, [6, 'somedesc6'])
sql_insertWayBills(connection, [7, 'somedesc7'])
sql_insertWayBills(connection, [8, 'somedesc8'])
sql_insertWayBills(connection, [9, 'somedesc9'])
sql_insertWayBills(connection, [10, 'somedesc10'])

cursorObj.execute('DELETE FROM StoreKeepers')
connection.commit()
sql_insertStoreKeepers(connection, [1, 'Daniil1', '71528111291'])
sql_insertStoreKeepers(connection, [2, 'Daniil2', '72528112292'])
sql_insertStoreKeepers(connection, [3, 'Daniil3', '73528113293'])
sql_insertStoreKeepers(connection, [4, 'Daniil4', '74528114294'])
sql_insertStoreKeepers(connection, [5, 'Daniil5', '75528115295'])
sql_insertStoreKeepers(connection, [6, 'Daniil6', '76528116296'])
sql_insertStoreKeepers(connection, [7, 'Daniil7', '77528117297'])
sql_insertStoreKeepers(connection, [8, 'Daniil8', '78528118298'])
sql_insertStoreKeepers(connection, [9, 'Daniil9', '71128144299'])
sql_insertStoreKeepers(connection, [10, 'Daniil10', '72228155200'])

cursorObj.execute('DELETE FROM DutyList')
connection.commit()
sql_insertDutyList(connection, [1, 1, 160, 12])
sql_insertDutyList(connection, [2, 2, 160, 11])
sql_insertDutyList(connection, [3, 3, 160, 6])
sql_insertDutyList(connection, [4, 4, 160, 7])
sql_insertDutyList(connection, [5, 5, 160, 8])
sql_insertDutyList(connection, [6, 6, 160, 9])
sql_insertDutyList(connection, [7, 7, 160, 13])
sql_insertDutyList(connection, [8, 8, 160, 11])
sql_insertDutyList(connection, [9, 9, 160, 12])
sql_insertDutyList(connection, [10, 10, 160, 16])

cursorObj.execute('DELETE FROM Items')
connection.commit()
sql_insertItems(connection, [1, 1, 15, 1])
sql_insertItems(connection, [2, 2, 43, 2])
sql_insertItems(connection, [3, 3, 65, 3])
sql_insertItems(connection, [4, 4, 23, 4])
sql_insertItems(connection, [5, 5, 43, 5])
sql_insertItems(connection, [6, 6, 14, 6])
sql_insertItems(connection, [7, 7, 75, 7])
sql_insertItems(connection, [8, 8, 23, 8])
sql_insertItems(connection, [9, 9, 56, 9])
sql_insertItems(connection, [10, 10, 13, 10])

cursorObj.execute('DELETE FROM Orders')
connection.commit()
sql_insertOrders(connection, [1, 1, 'Done', 1,1,1,0])
sql_insertOrders(connection, [2, 2, 'Done', 2,2,2,0])
sql_insertOrders(connection, [3, 3, 'Done', 3,3,0,3])
sql_insertOrders(connection, [4, 4, 'Done', 4,4,0,4])
sql_insertOrders(connection, [5, 5, 'Done', 5,5,5,0])
sql_insertOrders(connection, [6, 6, 'Done', 6,6,6,0])
sql_insertOrders(connection, [7, 7, 'Done', 7,7,0,7])
sql_insertOrders(connection, [8, 8, 'Done', 8,8,0,8])
sql_insertOrders(connection, [9, 9, 'Done', 9,9,9,0])
sql_insertOrders(connection, [10, 10, 'Done', 10,10,10,0])


def PrintSelection(rows):
    for row in rows:
        print(row)


cursorObj.execute('SELECT * FROM Orders') #1
PrintSelection(cursorObj.fetchall())

cursorObj.execute('UPDATE StoreKeepers SET FullNAME = "NeDaniil" where ID = 2') #2

cursorObj.execute('SELECT * FROM StoreKeepers') #3
PrintSelection(cursorObj.fetchall())

cursorObj.execute('SELECT * FROM StoreKeepers where ID > 3') #4
PrintSelection(cursorObj.fetchall())

cursorObj.execute('SELECT FullName FROM StoreKeepers') #5
PrintSelection(cursorObj.fetchall())

cursorObj.execute('DELETE FROM StoreKeepers where ID > 8')#6

cursorObj.execute('SELECT * FROM StoreKeepers') #7
PrintSelection(cursorObj.fetchall())

cursorObj.execute('SELECT * FROM StoreKeepers join DutyList') #8
PrintSelection(cursorObj.fetchall())

cursorObj.execute('SELECT * FROM StoreKeepers inner join DutyList') #9
PrintSelection(cursorObj.fetchall())

cursorObj.execute('SELECT * FROM Orders join Receivers join Suppliers join WayBills join StoreKeepers') #10
PrintSelection(cursorObj.fetchall())

connection.close()