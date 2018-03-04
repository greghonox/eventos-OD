 def eventos(self):
        self.cadastrar_produto.triggered.connect(self.cadastrar_p)
        self.consultar_produto.triggered.connect(self.consulta_p)
        self.cadastrar_fornecedor.triggered.connect(self.cadastrar_f)
        self.consultar_fornecedor.triggered.connect(self.consultar_f)
        self.relatorio.triggered.connect(self.relat)
        self.gerenciar_usuario.triggered.connect(self.gerenciar_u)
        self.bancodados.triggered.connect(self.bancod)
        self.backup.triggered.connect(self.backupp)

    def cadastrar_p(self):
        print("cadastrar produto")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_Form_produto()
        self.ui.setupUi(self.janela)
        self.janela.show()

    def consulta_p(self):
        print("consulta produto")

    def cadastrar_f(self):
        print("cdastrar fornecedor")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_Form_fornecedor()
        self.ui.setupUi(self.janela)
        self.janela.show()

    def consultar_f(self):
        print("consulta fornecedor")
    def relat(self):
        print("relatorio")

    def gerenciar_u(self):
        print("gerenciar usuario")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_Form_usuario()
        self.ui.setupUi(self.janela)
        self.janela.show()
        
    def bancod(self):
        print("banco de dados")
    def backupp(self):
        print("backup")
