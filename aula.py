#Thaynara Fumegali

class editora:
  def __init__(self, codEditora, razaoSocial, nomeContato, telefone):
    self.codEditora = codEditora
    self.razaoSocial = razaoSocial
    self.nomeContato = nomeContato
    self.telefone = telefone

  def setcodEditora(self,codEditora):
      self.codEditora = codEditora

  def setrazaoSocial(self, razaoSocial):
      self.razaoSocial = razaoSocial
    
  def setnomeContato(self, nomeContato):
      self.nomeContato = nomeContato

  def settelefone(self, telefone):
      self.telefone = telefone

  def getcodEditora(self):
      return self.codEditora
      
  def getrazaoSocial(self):
      return self.razaoSocial
    
  def getnomeContato(self):
      return self.getnomeContato

  def gettelefone(self):
      return self.gettelefone

class livro:
  def __init__(self, codLivro, descricaoLivro, codISBN):
    self.codLivro = codLivro
    self.descricaoLivro = descricaoLivro
    self.codISBN = codISBN

  def setcodLivro(self, codLivro):
      self.codLivro = codLivro

  def setdescricaoLivro(self, descricaoLivro):
      self.descricaoLivro = descricaoLivro

  def setcodISBN(self, codISBN):
      self.codISBN = codISBN

  def getcodLivro(self):
      return self.codLivro
    
  def getdescricaoLivro(self):
      return self.descricaoLivro

  def getcodISBN(self):
      return self.codISBN

editora1 = editora(89790, 'Saraiva', 'saraiva@saraiva.com', '(51) 8697-8574')
editora2 = editora(7863, 'John John', 'john@fantasia.com', '(51) 8974-5632')

livro1 = livro(5189674, 'Drama', '789-02-569-4789-1')
livro2 = livro(895743, 'Romance', '857-78-746-8942-5')

print ("\n BASE DE DADOS POO   |   Livros & Editoras   \n\t")
print ("=========================================== ")
print (" Dados das Editoras:\n\t")
print ("> Editora 1\n\tCódigo: ", editora1.getcodEditora(), "\n\tRazão Social: ",editora1.getrazaoSocial(), "\n")

print ("> Editora 2\n\tCódigo: ", editora2.getcodEditora(), "\n\tRazão Social: ",editora2.getrazaoSocial(), "\n")

print ("=========================================== ")
print (" Dados dos Livros:\n\t")
print ("> Livro 1\n\tCódigo: ", livro1.getcodLivro(),"\n\tDescrição: ", livro1.getdescricaoLivro(), "\n\tCódigo ISBN: ", livro1.getcodISBN(), "\n")
print ("> Livro 2\n\tCódigo: ", livro2.getcodLivro(),"\n\tDescrição: ", livro2.getdescricaoLivro(), "\n\tCódigo ISBN: ", livro2.getcodISBN())