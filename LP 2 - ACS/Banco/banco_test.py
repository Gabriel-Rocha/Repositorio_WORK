from banco import Cliente, Banco, Conta


def test_cria_cliente():
    try:
        c = Cliente('nome', 99999999, 'email@mail.com')
    except Exception:
        assert False, 'Erro ao criar o cliente'
    else:
        assert not hasattr(c, 'nome'), 'nome deve ser um atributo privado'
        assert not hasattr(c, 'telefone'), 'telefone deve ser um privado'
        assert not hasattr(c, 'email')


def test_nao_cria_cliente_tel():
    try:
        Cliente('nome', 'não é número', 'email@mail.com')
    except TypeError:
        assert True
    except Exception:
        assert False, 'Não lançou TypeError para telefone inválido'


def test_nao_cria_cliente_mail():
    try:
        Cliente('nome', 99999999, 'não é email')
    except ValueError:
        assert True
    except Exception:
        assert False, 'Não lançou ValueError para email inválido'


def test_get_nome():
    c = Cliente('nome', 99999999, 'email@mail.com')
    assert c.get_nome() == 'nome', 'getter de nome errado'


def test_get_telefone():
    c = Cliente('nome', 99999999, 'email@mail.com')
    assert c.get_telefone() == 99999999, 'getter de telefone errado'


def test_get_mail():
    c = Cliente('nome', 99999999, 'email@mail.com')
    assert c.get_email() == 'email@mail.com', 'getter de email errado'


def test_set_telefone():
    c = Cliente('nome', 99999999, 'email@mail.com')
    c.set_telefone(88888888)
    assert c.get_telefone() == 88888888


def test_set_telefone_erro():
    c = Cliente('nome', 99999999, 'email@mail.com')
    try:
        c.set_telefone('não é telefone')
    except TypeError:
        assert True
    except Exception:
        assert False, 'Não lançou um TypeError'
    else:
        assert c.get_telefone() == 99999999


def test_set_email():
    c = Cliente('nome', 99999999, 'email@mail.com')
    c.set_email('outro@mail.com')
    assert c.get_email() == 'outro@mail.com'


def test_set_email_erro():
    c = Cliente('nome', 99999999, 'email@mail.com')
    try:
        c.set_email('não é email')
    except ValueError:
        assert True
    except Exception:
        assert False, 'Não lançou um ValueError'
    else:
        assert c.get_email() == 'email@email.com'


def test_cria_banco():
    try:
        b = Banco('nome')
    except Exception:
        assert False, 'Erro ao criar o Banco'
    else:
        assert not hasattr(b, 'nome'), 'nome deve ser um atributo privado'


def test_get_nome_banco():
    b = Banco('nome')
    assert b.get_nome() == 'nome', 'getter de nome errado'


def lista_contas_vazio():
    b = Banco('nome')
    assert len(b.lista_contas()) == 0, 'O banco começa sem nenhuma conta'


def lista_contas_com_contas():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    b.abre_conta([c], 200)
    b.abre_conta([c], 300)
    assert len(b.lista_contas()) == 2, 'O banco deveria ter 2 contas'
    for cc in b.lista_contas():
        assert type(cc) == Conta, 'deveria retornar uma lista de contas'


def test_abre_conta():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    b.abre_conta([c], 100)
    ccs = b.lista_contas()
    assert len(ccs) == 1
    assert type(ccs[0]) == Conta
    assert ccs[0].get_numero() == 1, 'A primeira conta deve ser a numero 1'


def test_abre_conta_2():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    b.abre_conta([c], 100)
    b.abre_conta([c], 500)
    ccs = b.lista_contas()
    assert len(ccs) == 2
    assert type(ccs[1]) == Conta
    assert ccs[1].get_numero() == 2, 'A segunda conta deve ser a numero 2'


def test_n_abre_conta():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    try:
        b.abre_conta([c], -100)
    except ValueError:
        assert True
    except Exception:
        assert False, 'Não lançou um ValueError'
    ccs = b.lista_contas()
    assert len(ccs) == 0


def test_cria_conta():
    try:
        c = Cliente('nome', 99999999, 'email@mail.com')
        cc = Conta([c], 1, 0)
    except Exception:
        assert False, 'Erro ao criar conta'
    else:
        assert not hasattr(cc, 'clientes'), 'clientes deve ser privado'
        assert not hasattr(cc, 'numero'), 'numero deve ser um privado'
        assert not hasattr(cc, 'saldo'), 'saldo deve ser privado'


def test_nao_cria_conta():
    try:
        c = Cliente('nome', 99999999, 'email@mail.com')
        Conta([c], 1, -1)
    except ValueError:
        assert True
    except Exception:
        assert False, 'Não lançou ValueError para saldo inválido'


def test_get_clientes():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 0)
    lista = cc.get_clientes()
    assert len(lista) == 1
    assert lista[0].get_nome() == 'nome'
    assert lista[0].get_email() == 'email@mail.com'
    assert lista[0].get_telefone() == 99999999


def test_get_numero():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 0)
    assert cc.get_numero() == 1


def test_get_saldo():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    assert cc.get_saldo() == 100


def teste_deposito():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    cc.deposito(200)
    assert cc.get_saldo() == 300
    assert ('deposito', 200) in cc.extrato()


def teste_saque():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    cc.saque(50)
    assert cc.get_saldo() == 50
    assert ('saque', 50) in cc.extrato()


def teste_saque_err():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    try:
        cc.saque(150)
    except ValueError:
        assert cc.get_saldo() == 100, 'o saldo não deve ser alterado'
        assert ('saque', 150) not in cc.extrato()
    except Exception:
        assert False, 'Não lançou um ValueError'


def test_extrato():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    extrato = cc.extrato()
    assert type(extrato) == list
    assert len(extrato) == 1
    assert ('saldo_inicial', 100) in extrato, 'não lançou saldo no extrato'


def test_extrato_2():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 200)
    cc.saque(150)
    extrato = cc.extrato()
    assert len(extrato) == 2
    assert extrato[0] == ('saldo_inicial', 200)
    assert extrato[1] == ('saque', 150)
