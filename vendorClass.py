# Developer: Mauricio    -   Date:14/06/2021    -    Start
# Description: consoleMethods.py was created to contain all methods used to construct menus as well as methods that interact with the user
class vendorClass():
    # All Vendor related attributes
    vendorId = '0'
    vendorName = ''
    # This attribute is used to record all data for this class, since no database is being used
    allVendors = []

    # registerVen() will register a vendor
    def registerVen(self):
        # append to the data attribute. If the Data attribute is empty, insert the first line with the vendorId = 1
        if len(self.allVendors) == 0:
            self.allVendors.append(['1', self.vendorName])
        else:
            # if its not the first record, sort existing records to guarantee the id inserted is the biggest id +1
            self.sortVen()
            self.allVendors.append([str(int(self.allVendors[len(self.allVendors)-1][0])+1), self.vendorName])

    # delete a vendor according to an id informed by the user
    def deleteVen(self, idSel):
        # loops through all vendors looking for the id in 'idSel'
        for i in range(0, len(self.allVendors)):
            if idSel == self.allVendors[i-1][0]:
                del(self.allVendors[i-1])
                return True
        # return false if nothing was found
        return False

    # Print all vendors in the allVendors attribute
    def showVen(self):
        print('\nRegistered Vendor:\n')
        self.sortVen()
        # loop through all vendors
        for i in range(0, len(self.allVendors)):
            # condition used to guarantee the loop will not go over the size of the list
            # if len(self.allVendors) -1 was used in the loop, nothing would occur case allVendors had only 1 record
            if i == len(self.allVendors):
                break
            # print the vendor info
            print('Seller id: ' + str(self.allVendors[i][0]) + '\nSeller Name: ' + str(self.allVendors[i][1]) + '\n')

    # sort allVendors attribute
    def sortVen(self):
        self.allVendors.sort()

# ========================================================
# Developer: Mauricio    -   Date:14/06/2021    -    End