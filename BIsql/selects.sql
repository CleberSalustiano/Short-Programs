-- Questão 1
SELECT sum(t.qtdAlunos) AS "número de alunos", 
d.nmDisciplina AS "nome da disciplina",
p.nmProfessor AS "nome do professor",
pe.semestre,
pe.ano 
FROM Turma AS t 
INNER JOIN Professor AS p ON p.id = t.idProfessor
INNER JOIN Disciplina AS d ON d.id = t.idDisciplina
INNER JOIN Periodo AS pe ON pe.id = t.idPeriodo
GROUP BY d.nmDisciplina, p.nmProfessor, pe.semestre, pe.ano;


-- Questão 2
SELECT sum(t.qtdAlunosAprovados) / sum(t.qtdAlunos) AS "percentual de aprovação",
d.nmDisciplina AS "nome da disciplina",
p.semestre, 
p.ano 
FROM Turma t
INNER JOIN Disciplina d on d.id  = t.idDisciplina 
INNER JOIN Periodo p on p.id = t.idPeriodo 
GROUP BY d.nmDisciplina, p.semestre, p.ano;


-- Questão 3
SELECT sum(t.qtdAlunosAprovados) AS "alunos aprovados por nota", p.nmProfessor  
FROM Turma t 
INNER JOIN Professor p on p.id = t.idProfessor 
GROUP BY p.nmProfessor ;


-- Questão 4
SELECT sum(t.qtdAlunosAprovados), p.nmProfessor, d.Curso, p2.semestre, p2.ano FROM Turma t 
INNER JOIN Professor p on p.id = t.idProfessor 
INNER JOIN Disciplina d on d.id = t.idDisciplina 
INNER JOIN Periodo p2  on p2.id = t.idPeriodo
GROUP BY p.nmProfessor, d.Curso, p2.semestre, p2.ano 
ORDER BY t.id DESC;


-- Questão 5
SELECT sum(t.qtdAlunosReprovados) / sum(t.qtdAlunos), d.nmDisciplina, p.semestre, p.ano  FROM Turma t 
INNER JOIN Disciplina d on d.id = t.idDisciplina 
INNER JOIN Periodo p  on p.id = t.idPeriodo
GROUP BY d.nmDisciplina, p.semestre, p.ano
HAVING sum(t.qtdAlunosReprovados) / sum(t.qtdAlunos) > 0.5;


-- Questão 6
SELECT sum(t.qtdAlunosReprovados), d.tipoDisciplina FROM Turma t 
INNER JOIN Disciplina d on d.id = t.idDisciplina 
GROUP BY d.tipoDisciplina;
