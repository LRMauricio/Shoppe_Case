# Developer: Mauricio    -   Date:14/06/2021    -    Start
# Description: saleClass.py was created to contain all methods used to manipulate sales
from datetime import date
#             imports-end
# -------------------------------------
class saleClass():
    # All sale related attributes
    saleId = ''
    dtSale = date.today()
    items = []
    venId = ''
    venName = ''
    cusName = ''
    salVal = 0.0
    # This attribute is used to record all data for this class, since no database is being used
    dataSale = []

    # RegisterSale() will register a sale and return errors according to the outcome
    def registerSale(self, vendObj, itemObj, itemReg):
        # error = 0 means success
        error = 0
        # try to search for the Vendor of this sale. Error = 1 means Vendor not found in the vendor object
        if not self.searchVen(vendObj):
            error = 1
            return error
        # try to search for all items listed in the sale. Error = 2 means one or more items were not found in the item object
        if not self.searchItems(itemObj, itemReg):
            error = 2
            return error
        # return error if the customer name was not filled
        if self.cusName == '':
            error = 3
            return error
        # append to the data attribute. If the Data attribute is empty, insert the first line with the saleId = 1
        if len(self.dataSale) == 0:
            self.dataSale.append(['1', self.dtSale, self.items, self.venId, self.venName, self.cusName, self.salVal])
        else:
            # if its not the first record, sort existing records to guarantee the id inserted is the biggest id +1
            self.sortSale()
            self.dataSale.append([str(int(self.dataSale[len(self.dataSale)-1][0])+1), self.dtSale, self.items, self.venId, self.venName, self.cusName, self.salVal])
            # if none of the previous errors were activated, the value of 'error' should be 0 at this point (which means success)
            return error

    # Print all sales in the dataSale attribute
    def showSale(self):
        # sort all sales by salVal (Sales total Value or the 6th column, hence x[6]). reverse is used to have the biggest value first
        sorted_Sales = sorted(self.dataSale, key=lambda x: x[6], reverse=True)
        # loop through all sales
        for i in range(0, len(sorted_Sales)):
            # condition used to guarantee the loop will not go over the size of the list
            # if len(sorted_Sales) -1 was used in the loop, nothing would occur case sales had only 1 record
            if i == len(sorted_Sales):
                break
            # grab all information from the sorted list
            idSal = sorted_Sales[i][0]
            dtSal = sorted_Sales[i][1]
            idVen = sorted_Sales[i][3]
            nmVen = sorted_Sales[i][4]
            nmCus = sorted_Sales[i][5]
            slVal = sorted_Sales[i][6]
            #print the sales info
            print('===================================')
            print('\nId Sale: {idSale} \nDate of sale: {dtSale} \nSeller id and name: {venId} - {venName} '
                  '\nCustomer name: {cusName} \nTotal value: {salVal}'.format(idSale=idSal,
                                                                            dtSale=dtSal.strftime('%d/%m/%Y'),
                                                                              venId=idVen,
                                                                              venName=nmVen,
                                                                              cusName=nmCus,
                                                                              salVal=slVal))
            # this loop is used to print all items listed in a specific sale
            print('\nItems in the sale:')
            for j in range(0, len(sorted_Sales[i][2])):
                # same checking as above
                if j == len(sorted_Sales[i][2]):
                    break
                # grab information about items of the sale and print them
                id = sorted_Sales[i][2][j][0]
                name = sorted_Sales[i][2][j][1]
                val = sorted_Sales[i][2][j][2]
                qtd = sorted_Sales[i][2][j][3]
                print('Item: {Id} - {name} - {value}'
                      ' - Quantity sold: {qtd}'. format(Id=id,
                                                        name=name,
                                                        value=val,
                                                        qtd=qtd))
            print('===================================')

    # Search for vendor in the vendor object to grab name and guarantee the Id exists
    def searchVen(self, vendObj):
        for i in range(0, len(vendObj.allVendors)):
            if self.venId == vendObj.allVendors[i-1][0]:
                self.venName = vendObj.allVendors[i-1][1]
                return True
        # return false case the vendor was not found (error 1)
        return False

    # Search for items in the item object to grab description, price and guarantee the Id exists
    def searchItems(self, itemObj, itemReg):
        # empty items and total value attributes to guarantee a new sale do not grab old values
        self.items = []
        self.salVal = 0.0
        # loops through the list of objects informed by the user
        for i in range(0, len(itemReg)):
            # loops through all items in the item object and check if the items above exist, also grabbing their description and values
            for j in range(0, len(itemObj.itemData)):
                if itemReg[i-1][0] == itemObj.itemData[j-1][0]:
                    self.items.append([itemReg[i-1][0], itemObj.itemData[j-1][1], itemObj.itemData[j-1][2], itemReg[i-1][1]])
                    # calculate the total value of the sale
                    self.salVal = self.salVal + (float(itemObj.itemData[j-1][2]) * float(itemReg[i-1][1]))
        # if the items were not found or the number of items found is not equal to all items informed, return False (error 2)
        if len(self.items) == 0 or len(self.items) != len(itemReg):
            return False
        else:
            return True

    # delete a sale according to a id informed by the user
    def delSale(self, delete):
        # loops through all sales looking for the id in 'delete'
        for i in range(0, len(self.dataSale)):
            if self.dataSale[i-1][0] == delete:
                del(self.dataSale[i-1])
                return True
        # return false if nothing was found
        return False

    # edit vendor in the sale
    def editVen(self, vendorObj, Id, newId):
        # loop through sale looking for the id informed in 'Id'
        for i in range(0, len(self.dataSale)):
            if Id == self.dataSale[i-1][0]:
                # if the id was found, loop through all vendors to check if the newId exists and grabbing the name of the vendor
                for j in range(0, len(vendorObj.allVendors)):
                    if newId == vendorObj.allVendors[j-1][0]:
                        self.dataSale[i-1][3] = newId
                        self.dataSale[i-1][4] = vendorObj.allVendors[j-1][1]
                        return True
        # return false for Id or newId not found
        return False

    # Edit customer name in the sale
    def editCus(self, Id, Cus):
        # loop through all sales looking for Id
        for i in range(0, len(self.dataSale)):
            # If Id found, change the customer name for the one informed
            if Id == self.dataSale[i-1][0]:
                self.dataSale[i-1][5] = Cus
                return True
        # return false for Sale Id not found
        return False

    # sort dataSale attribute
    def sortSale(self):
        self.dataSale.sort()

# ========================================================
# Developer: Mauricio    -   Date:14/06/2021    -    End