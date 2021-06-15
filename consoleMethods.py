# Developer: Mauricio    -   Date:14/06/2021    -    Start
# Description: consoleMethods.py was created to contain all methods used to construct menus as well as methods that interact with the user

from os import system, name
from consolemenu import *
from consolemenu.items import *
from vendorClass import *
from itemClass import *
from saleClass import *
#             imports-end
# -------------------------------------

# Create objects for all classes used during the program
vendorObj = vendorClass()
itemObj = itemClass()
saleObj = saleClass()

# -----------------------------------------------------

# method used to clear console
def clrConsole():
    command = 'clear'
    # check if its running on windows and, if so, change for the adequate command
    if name in ('nt', 'dos'):
        command = 'cls'
    system(command)

# Creating Main Menu
def filMenu():
    # Start the submenus constructors
    subVen = subVendor()
    subIt = subItem()
    subSale = subSales()

    # create main menu
    menu = ConsoleMenu('Welcome to Sales Menu', 'Please, select one of the options bellow:')
    # Create options for the user to select in the main menu
    submenuVen = SubmenuItem('Seller Control Panel', subVen)    #Set the Option for Seller/Vendor
    submenuItem = SubmenuItem('Item Control Panel', subIt)      #set the Option for Item/Product
    submenuSale = SubmenuItem('Sale Control Panel', subSale)    #set the Option for Sales
    # append Options to the main menu
    menu.append_item(submenuVen)
    menu.append_item(submenuItem)
    menu.append_item(submenuSale)
    # Show Main Menu
    menu.show()

# ----------------------Methods for Seller/Vendor-------------------------

# subVendor Creates the selectable options for the Seller/Vendor menu
def subVendor():
    # Create a submenu for the Vendor options
    subVendor = ConsoleMenu('Seller Control Panel', 'Please, select one of the options bellow:')
    # Create the Options selected in the Submenu
    regVendorOpt = FunctionItem('Register seller', regVendor, args=(vendorObj,))    # Call method regVendor() passing the object for the vendor Class as parameter
    editVendorOpt  = FunctionItem('Show sellers', showVendor, args=(vendorObj,))    # Call method showVendor() passing the object for the vendor Class as parameter
    delVendorOpt  = FunctionItem('Delete seller', delVendor, args=(vendorObj,))     # Call method delVendor() passing the object for the vendor Class as parameter
    # Append created options to the Seller submenu
    subVendor.append_item(regVendorOpt)
    subVendor.append_item(editVendorOpt)
    subVendor.append_item(delVendorOpt)
    # Return the submenu to be appended to the main menu
    return subVendor

# Using the vendor Object, Access the vendor Class and register a new Vendor
def regVendor(vendorObj):
    # Ask the name of the new Seller/Vendor
    selName = input("Please input the name of the Seller:\n")
    # Fill the vendor name attribute from the vendor Class with the name informed by the user
    vendorObj.vendorName = selName
    # Insert new vendor in the "data attribute" of the vendor class
    vendorObj.registerVen()
    input('Seller successfully registered')

# Show all vendors registered in the "data attribute" of the vendor object
def showVendor(vendorObj):
    vendorObj.showVen()
    input('\nThose are all the seller currently registered')

# Delete vendor registered in the "data attribute" of the vendor object
def delVendor(vendorObj):
    # Grab Vendor Id to be deleted
    selId = input("Please input the id of the seller to be deleted:\n")
    # the return of deleteVen() is a boolean with True for success and False for Failure
    if vendorObj.deleteVen(selId):
        input('\nSeller with the ID {id} successfully deleted'.format(id=selId))
    else:
        input('Selected Id not found')

# ----------------------Methods for item/Product---------------------------

# subItem Creates the selectable options for the Item/Product menu
def subItem():
    # create a sub menu for the Item options
    subItem = ConsoleMenu('Item Control Panel', 'Please, select one of the options bellow:')
    # Create the Options selected in the Submenu
    regItemOpt = FunctionItem('Register item', regItem, args=(itemObj,))    # Call method regItem() passing the object for the item Class as parameter
    editItemOpt = FunctionItem('Show item', showItem, args=(itemObj,))      # Call method showItem() passing the object for the item Class as parameter
    delItemOpt = FunctionItem('Delete item', delItem, args=(itemObj,))      # Call method delItem() passing the object for the item Class as parameter
    # Append created options to the Item/Product submenu
    subItem.append_item(regItemOpt)
    subItem.append_item(editItemOpt)
    subItem.append_item(delItemOpt)
    # Return the submenu to be appended to the main menu
    return subItem

# Using the item Object, Access the item Class and register a new product/item
def regItem(ItemObj):
    # Ask the name/description of the new product
    itemDesc = input("Please input the name of the Product to be registered:\n")
    # Fill the item description attribute from the item Class with the item informed by the user
    ItemObj.itemDesc = itemDesc
    # Does the same as above, but asking/setting the price/value of the item instead
    itemPrice = input("Please input the price of the Product to be registered:\n")
    ItemObj.itemVal = itemPrice
    # Insert new item in the "data attribute" of the vendor class
    ItemObj.registerItem()
    input('Item successfully saved')

# Show all items and the respective prices registered in the "data attribute" of the item object
def showItem(ItemObj):
    ItemObj.showItem()
    input('\nThose are all Items currently registered')

# Delete item registered in the "data attribute" of the item object
def delItem(ItemObj):
    # Grab Item Id to be deleted
    itemId = input("Please input the id of the item to be deleted:\n")
    # the return of deleteItem() is a boolean with True for success and False for Failure
    if ItemObj.deleteItem(itemId):
        input('\nItem with the ID {id} successfully deleted'.format(id=itemId))
    else:
        input('Selected Id not found')


#----------------------Methods for Sales-------------------------

# subItem Creates the selectable options for the Item/Product menu
def subSales():
    edSale = editSaleMenu()
    # create a sub menu for the Sales options
    subSale = ConsoleMenu('Sales Control Panel', 'Please, select one of the options bellow:')
    # Create the Options selected in the Submenu
    regSaleOpt = FunctionItem('Register sale', regSale, args=(saleObj, vendorObj, itemObj)) # Call method regSale() passing the objects for the Sale, vendor and item Classes as parameter
    showSaleOpt = FunctionItem('Show Sales', showSale, args=(saleObj,)) # Call method showSale() passing the object for the Sale Class as parameter
    delSaleOpt = FunctionItem('Delete Sale', delSale, args=(saleObj,)) # Call method delSale() passing the object for the Sale Class as parameter
    editSaleOpt = SubmenuItem('Edit Sale', edSale)  # Call method editSaleMenu() to create a submenu that will let the user choose which information to edit
    # Append created options to the Sales submenu
    subSale.append_item(regSaleOpt)
    subSale.append_item(showSaleOpt)
    subSale.append_item(delSaleOpt)
    subSale.append_item(editSaleOpt)
    return subSale

# Using the item Object, Access the item Class and register a new product/item
def regSale(saleObj, vendorObj, itemObj):
    # Ask the information necessary to register a new sale
    saleObj.venId = input('Please, inform the Id of the seller doing the sale:\n')
    saleObj.cusName = input('Please, inform the name of the customer doing the purchase:\n')
    # Since a sale can have multiple items, a list is used to store items and their quantity
    itemsReg = []
    control = ''
    # this loop is used to ask the user indefinitely if he wants to add items. The loop ends when something other than 'y' is typed
    while control != 'n':
        control = input('Would you like to Add a new item to the sale? [y/n]\n')
        # check if the user chose to add another item
        if control.lower() == 'y':
            # ask for items and their quantities
            itemId = input('What is the Id of the item to be added to the sale?\n')
            itemQtd = input('How many of the item, id {id}, would you like to add?\n'.format(id=itemId))
            # add items and quantities to the list
            itemsReg.append([itemId, itemQtd])
        else:
            control = 'n'
    try:
        # Try to register new sale, Try is used to guarantee no error in case either the quantity or the value of the items are not numbers (those are used to calculate the total)
        outcomeSale = saleObj.registerSale(vendorObj, itemObj, itemsReg)
        # Create a switcher to give accurate responses depending on the outcome of the method above
        switcher = {
            1: 'Id of the seller is not valid', # Seller not found
            2: 'One or more item(s) not found', # any of the items informed not found
            3: 'Customer name cannot be blank'  # customer name not informed
        }
        input(switcher.get(outcomeSale, 'Sale registered successfully'))
    except:
        # this error only occurs if item value or quantity informed are not numbers
        input('Error when calculating the total value of the sale. Please check the quantity and the value of the registered item')

# Show all Sales ordered by the total amount of each, the most expensive being the first
def showSale(saleObj):
    saleObj.showSale()
    input('All registered sales have been printed')

# Delete Sale registered in the "data attribute" of the Sale object
def delSale(saleObj):
    # Grab sale Id to be deleted
    delete = input('inform the id of the sale to be deleted:\n')
    # the return of delSale() is a boolean with True for success and False for Failure
    if saleObj.delSale(delete):
        input('\nSale with the ID {id} successfully deleted'.format(id=delete))
    else:
        input('Selected Id not found')

# This create the submenu for editing sale information
def editSaleMenu():
    # Create Edit Sale submenu
    subEditSale = ConsoleMenu('Sale editor', 'Please, select one of the options bellow:')
    # Create options for the submenu
    venEditOpt = FunctionItem('Edit Seller', editVendor, args=(saleObj, vendorObj,)) # option call editVendor() passing sale and vendor objects as parameters
    cusEditOpt = FunctionItem('Edit Customer', editCus, args=(saleObj,))             # option call editCus() passing sal object as parameter
    # Append created options to the submenu
    subEditSale.append_item(venEditOpt)
    subEditSale.append_item(cusEditOpt)
    # Return submenu to be appended to the previous menu 'subSale'
    return subEditSale

# Method called by the menu created above, with the goal of changing a vendor of a sale
def editVendor(salesObj, vendorObj):
    # Grab id of the sale to be changed, as well as the new vendor id to be added
    Id = input('What is the Id of the sale you wish to alter?\n')
    newVen = input('What is the Id of the new Seller?\n')
    # editVen() alter the vendor id and name from a sale. Return True for success and False for failure
    if salesObj.editVen(vendorObj, Id, newVen):
        input('Seller Altered successfully')
    else:
        input('Sale Id or Seller not found')

# Method called by the menu created above, with the goal of changing a customer of a sale
def editCus(salesObj):
    # Grab id of the sale to be changed, as well as the new customer to be added
    Id = input('What is the Id of the sale you wish to alter?\n')
    newCus = input('What is the new name of the customer?\n')
    # editCus() alter the name of the customer from a sale. Return True for success and False for failure
    if salesObj.editCus(Id, newCus):
        input('Seller Altered successfully')
    else:
        input('Sale Id or Seller not found')

# ======================================================
# Developer: Mauricio    -   Date:14/06/2021    -    End



