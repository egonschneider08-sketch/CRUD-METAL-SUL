from database import conectar

conectar()

from setor import (
    cadastrar_setor, 
    listar_setores, 
    atualizar_setor, 
    deletar_setor
)

from funcionario import (
    cadastrar_funcionario, 
    listar_funcionarios, 
    atualizar_cargo_salario, 
    deletar_funcionario
)

from categoria_produto import (
    cadastrar_categoria, 
    listar_categorias, 
    atualizar_categoria, 
    deletar_categoria
)

from fornecedor import (
    cadastrar_fornecedor, 
    listar_fornecedores, 
    atualizar_fornecedor, 
    deletar_fornecedor
)

from produto import (
    cadastrar_produto, 
    listar_produtos, 
    atualizar_estoque_preco, 
    deletar_produto
)

from ordem_producao import (
    cadastrar_ordem_producao, 
    listar_ordens_producao, 
    atualizar_status_ordem, 
    deletar_ordem_producao
)

from controle_qualidade import (
    cadastrar_inspecao, 
    listar_inspecoes, 
    atualizar_resultado_inspecao, 
    deletar_inspecao
)