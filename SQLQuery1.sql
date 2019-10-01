INSERT INTO DisciplinaOfertada
(ID, IdCoordenador, DtInicioMatricula, DtFimMatricula, IdDisciplina, IdCurso, Ano, Semestre, Turma, IdProfessor, Metodologia, Recursos, Criterio Avaliacao, PlanoDeAula);

VALUES 
  ('1','190','2018-10-10', '2019-10-10', '1', '5', '2019','1','9','1','Agil','Computador','10','2')
, ('2','191','2018-10-10', '2019-10-10', '2', '4', '2019','1','2','1','Agil','Computador','10','2')
, ('3','192','2018-10-10', '2019-10-10', '3', '3', '2019','1','4','3','Agil','Computador','10','3')
, ('4','193','2018-10-10', '2019-10-10', '4', '2', '2019','1','6','4','Agil','Computador','10','1')
, ('5','194','2018-10-10', '2019-10-10', '5', '1', '2019','1','2','8','Agil','Computador','10','8');



INSERT INTO Curso
(ID, Nome)

VALUES 
 ('1','Jonas')
, ('2','Mario')
, ('3','Thanos')
, ('4','Vladmir')
, ('5','Alex');
