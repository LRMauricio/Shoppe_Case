# Developer: Mauricio    -   Date:14/06/2021    -    Start
# Description: consoleMethods.py was created to contain all methods used to construct menus as well as methods that interact with the user
class itemClass():
    # All Items related attributes
    itemId = ''
    itemDesc = ''
    itemVal = 0.0
    # This attribute is used to record all data for this class, since no database is being used
    itemData = []

    # registerItem() will register a item
    def registerItem(self):
        # append to the data attribute. If the Data attribute is empty, insert the first line with the vendorId = 1
        if len(self.itemData) == 0:
            self.itemData.append(['1', self.itemDesc, self.itemVal])
        else:
            # if its not the first record, sort existing records to guarantee the id inserted is the biggest id +1
            self.sortItem()
            self.itemData.append([str(int(self.itemData[len(self.itemData)-1][0])+1), self.itemDesc, self.itemVal])

    # delete an item according to an id informed by the user
    def deleteItem(self, idItem):
        # loops through all vendors looking for the id in 'idItem'
        for i in range(0, len(self.itemData)):
            if idItem == self.itemData[i-1][0]:
                del(self.itemData[i-1])
                return True
        # return false if nothing was found
        return False

    # Print all items in the itemData attribute
    def showItem(self):
        print('\nRegistered Items:\n')
        self.sortItem()
        # loop through all items
        for i in range(0, len(self.itemData)):
            # condition used to guarantee the loop will not go over the size of the list
            # if len(self.allVendors) -1 was used in the loop, nothing would occur case allVendors had only 1 record
            if i == len(self.itemData):
                break
            # print the item info
            print('Item Id: {id} \nItem Name: {name} \nItem Price: {price}\n'.format(id=str(self.itemData[i][0]),
                                                                                     name=str(self.itemData[i][1]),
                                                                                     price=str(self.itemData[i][2])))

    # sort allVendors attribute
    def sortItem(self):
        self.itemData.sort()

# ========================================================
# Developer: Mauricio    -   Date:14/06/2021    -    End