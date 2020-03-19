import weakref
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


rxn_pot = []

class Element(object):
    """docstring for element."""
    _instances = set()

    def __init__(self, Symbol,Number,Group,Name, Mass):
        super(Element, self).__init__()
        #print(type(Number))
        self.symbol = Symbol
        self.number = int(Number)
        if Group != '':
            self.group = int(Group)
        else:
            self.group = ''
        self.name = Name
        m = list(Mass)
        if '[' in m:
            m.remove('[')
        if ']' in m:
            m.remove(']')
        mass = ''
        for i in m:
            mass+=i

        self.mass = mass
        self.type = ''
        self._instances.add(weakref.ref(self))




    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead


dat = []
with open('PTdata.csv','r') as f:
    lines = f.readlines()



for i in range(len(lines)//2):
    symbol = lines[i*2].split(',')
    letter = symbol[1].split(': ')[1]


    number = symbol[2].split(': ')[1]


    gr = lines[i*2+1].split(',')[0]
    gr = gr.split(': ')[1]

    mass = lines[i*2].split(',')[3].split(':')[1].split(' ')[1]

    name = lines[i*2].split(',')[0].split(': ')[1]

    dat.append([name,letter,number,gr,mass])

for i in dat:
    i[0] = Element(i[1],i[2],i[3],i[0],i[4])



#GUI Below



m = Tk(className='PTGUI')
i=0
metal = []
nonmetal = []
transition = []
semimetal = []

def compile():
    pass ####################################what do it do######################################## pair this with the button at the bottom
    #add up all the masses for molar mass
    #for bonds between metals and non metals apply ionic rule
    #display results in popup
    #clear entrys
    #have a dorp down option be unknown
        #cancles adding protocoll
        #only for ionic componds
        #figures out hown many are needed to have a properly bonded molecule
            #wholl program only works for 'ideal ' molecules
    for i in range(0,len(rxn_pot)):
        for obj in Element.getinstances():
            if obj.symbol == rxn_pot[i][0]:
                rxn_pot[i] = (obj, rxn_pot[i][1])

    mm = sum([float(y[0].mass) * y[1] for y in rxn_pot])
    popup = Tk()
    popup.wm_title("Molar Mass")
    molecule = ''
    #print(molecule)
    for i in rxn_pot:
        molecule += ' '
        molecule += str(i[1])
        molecule += ' '
        molecule += i[0].name





    l1 = Label(popup, text = 'Molecule:' + molecule)
    l1.grid(row = 0)
    l2 = Label(popup, text = str(mm) + ' amu')
    l2.grid(row = 1)

def add():
    le = len(rxn_pot)

    #logic for meatls
    if m_cb.get() != '' and m_cb.get() not in [x[0] for x in rxn_pot] and m_cb.get() != 'None':
        rxn_pot.insert(0, (m_cb.get(),1))

    elif m_cb.get() in [x[0] for x in rxn_pot] and m_cb.get() != 'None':

        ind = [x[0] for x in rxn_pot].index(m_cb.get())
        rxn_pot[ind] = (m_cb.get(),rxn_pot[ind][1]+1)
        update = Label(m, text = str(rxn_pot[ind][1]) + ' ' + rxn_pot[ind][0])
        update.grid(row = ind+1, column = 4)

#logic for nonmetals
    if nm_cb.get() != '' and nm_cb.get() not in [x[0] for x in rxn_pot] and nm_cb.get() != 'None':
        rxn_pot.insert(0,(nm_cb.get(),1))
        #print((m_cb in [x[0] for x in rxn_pot]))
    elif nm_cb.get() in [x[0] for x in rxn_pot] and nm_cb.get() != 'None' :

        ind = [x[0] for x in rxn_pot].index(nm_cb.get())
        rxn_pot[ind] = (nm_cb.get(),rxn_pot[ind][1]+1)
        update = Label(m, text = str(rxn_pot[ind][1]) + ' ' + rxn_pot[ind][0])
        update.grid(row = ind+1, column = 4)

#logic for transition metals
    if tm_cb.get() != '' and tm_cb.get() not in [x[0] for x in rxn_pot] and tm_cb.get() != 'None':
        rxn_pot.insert(0,(tm_cb.get(),1))
    elif tm_cb.get() in [x[0] for x in rxn_pot] and tm_cb.get() != 'None':
        ind = [x[0] for x in rxn_pot].index(tm_cb.get())
        rxn_pot[ind] = (tm_cb.get(),rxn_pot[ind][1]+1)
        update = Label(m, text = str(rxn_pot[ind][1]) + ' ' + rxn_pot[ind][0])
        update.grid(row = ind+1, column = 4)

    n_add = len(rxn_pot)-le

    for i in range(n_add):

        rx = Label(m,text= str(rxn_pot[i][1]) + ' ' + rxn_pot[i][0])

        rx.grid(row = 1+le+i, column= 4)


for obj in Element.getinstances():
    if obj.group == '':
        obj.type = 'other'

    elif obj.group == 1 and obj.symbol != 'H':
        obj.type = 'metal'
    elif obj.symbol == 'H':
        obj.type = 'nonmetal'
    elif obj.group == 2:
        obj.type = 'metal'

    elif obj.group <= 12:
        obj.type = 'transition metal'
    elif obj.group == 13:
        if obj.number != 5:
            obj.type = 'metal'
        else:
            obj.type = 'semimetal'

    elif obj.group == 14:
        if obj.number == 6:
            obj.type = 'nonmetal'
        elif obj.number <= 32:
            obj.type = 'semimetal'
        else:
            obj.type = 'metal'
    elif obj.group == 15:
        if obj.number <= 15:
            obj.type = 'nonmetal'
        elif obj.number <= 51:
            obj.type = 'semimetal'
        else:
            obj.type = 'metal'
    elif obj.group == 16:
        if obj.number <= 34:
            obj.type = 'nonmetal'
        elif obj.number <= 84:
            obj.type = 'semimetal'
        else:
            obj.type = 'metal'

    elif obj.group == 17:
        if obj.number <= 53:
            obj.type = 'nonmetal'
        else:
            obj.type = 'semimetal'

    elif obj.group == 18:
        obj.type = 'nonmetal'


    if obj.type == 'metal':
        metal.append(obj)
    elif obj.type == 'nonmetal':
        nonmetal.append(obj)
    elif obj.type == 'semimetal':
        semimetal.append(obj)
    else:
        transition.append(obj)

none1 = Element('None','0','0','None','0')
none1.type = 'metal'
metal.append(none1)
none2 = Element('None','0','0','None','0')
none2.type = 'nonmetal'
nonmetal.append(none2)

none3 = Element('None','0','0','None','0')
none3.type = 'transition metal'
transition.append(none3)

none4 = Element('None','0','0','None','0')
none4.type = 'semimetal'
semimetal.append(none4)

label1 = Label(m, text='Metals', width = 30)
label1.config(anchor=CENTER)
label1.grid(row=0, column=0)


label2 = Label(m, text = 'Nonmetals', width = 30)
label2.config(anchor=CENTER)
label2.grid(row=0, column=1)


label3 = Label(m, text='Transition Metals', width = 30)
label3.config(anchor=CENTER)
label3.grid(row = 0, column = 2)

label4 = Label(m,text = 'Semimetals', width = 30)
label4.config(anchor=CENTER)
label4.grid(row = 0, column = 3)



m_cb = Combobox(m, values =  [obj.symbol for obj in metal] , textvariable = 'Metals')
m_cb.grid(row=1,column=0)

nm_cb = Combobox(m, values =  [obj.symbol for obj in nonmetal] , textvariable = 'Nonmetals')
nm_cb.grid(row=1,column=1)

tm_cb = Combobox(m, values =  [obj.symbol for obj in transition] , textvariable = 'Transition Metals')
tm_cb.grid(row=1,column=2)

sm_cb = Combobox(m, values = [obj.symbol for obj in semimetal], textvariable = 'Semimetals')
sm_cb.grid(row = 1, column = 3)

add = Button(m, text='Add Elements to RXN', command=add, width = 30)
add.grid(row=2, column = 1)

submit = Button(m, text = 'Done', command = compile, width = 30)
submit.grid(row=3, column=1)

l4 = Label(m, text = 'Reactants', width =30)
l4.config(anchor=CENTER)
l4.grid(row = 0, column = 4)




m.mainloop()
