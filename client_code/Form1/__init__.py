from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    #self.sifterrows.items = [{'sifter':'adrian'}, {'sifter':'Roy'}]

    critical = [{'sifter':'adrian'}]
    high = [{'sifter':'Roy'}]
    normal = [{'sifter':'Mark'}]
    low = [{'sifter':'Wojtek'}]
    trivial = [{'sifter':'Naked Ape'}]

    collection = critical+high+normal

    self.sifterrows.items = collection 
    #self.sifterrows.items.extend( high )
    #self.sifterrows.items.extend( normal )
    #self.sifterrows.items.extend( low )    
    #self.sifterrows.items.extend( trivial )


