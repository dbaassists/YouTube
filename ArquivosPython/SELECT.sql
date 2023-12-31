-- 01.1 - SELECIONADO COLUNAS DE UMA TABELA

SELECT 
[CodVideoYouTube]
,[NomVideo]
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]

-- 01.2 - SELECIONADO VALORES DISTINTOS DE UMA TABELA

SELECT 
DISTINCT [NomCanal]
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]

SELECT 
[NomCanal]
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
GROUP BY [NomCanal]

-- 01.3 - SELECIONANDO OS N PRIMEIRO REGISTROS DE UMA TABELA

SELECT TOP 5 *
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
ORDER BY IdSeqVideoYouTube ASC

SELECT TOP 5 *
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
ORDER BY IdSeqVideoYouTube DESC

-- 01.4 - USANDO FUNÇÕES DE AGREGAÇÃO - MIN(), MAX(), COUNT(), AVG(), STDEVP() and SUM()
-- PARA REPRODUZIR A FUNÇÃO describe()

SELECT 
COUNT(NumVisualizacao) count
,AVG(NumVisualizacao) mean
,STDEVP(NumVisualizacao) std
,MIN(NumVisualizacao) min
,MAX(NumVisualizacao) max
,SUM(NumVisualizacao) sum
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]

-- 02 - FILTRANDO VALORES

SELECT 
NomCanal, 
COUNT(NumVisualizacao) QTD
INTO ##dfCanal_QtdVideos
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
GROUP BY NomCanal

SELECT * 
FROM ##dfCanal_QtdVideos
WHERE QTD = 1

SELECT * 
FROM ##dfCanal_QtdVideos
WHERE QTD >= 2 AND QTD <= 10

SELECT * 
FROM ##dfCanal_QtdVideos
WHERE QTD in ( 2 , 10 )

-- 03 - ORDENANDO UMA TABELA

SELECT *
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
ORDER BY [NumLike] ASC

SELECT *
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
ORDER BY [NumLike] DESC

-- 04 - AGRUPANDO VALORES 

SELECT NomCanal , COUNT(NumVisualizacao) QTD_VISUALIZACAO
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
GROUP BY NomCanal
ORDER BY QTD_VISUALIZACAO

SELECT NomCanal , COUNT(NumVisualizacao) QTD_VISUALIZACAO
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
GROUP BY NomCanal
ORDER BY QTD_VISUALIZACAO DESC

-- 05 - COMANDO HAVING 

SELECT NomCanal, SUM(NumVisualizacao) NumVisualizacao
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
GROUP BY NomCanal
HAVING SUM(NumVisualizacao) >= 1000000000

-- 06 - INSERINDO REGISTROS EM UMA TABELA

SELECT * 
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]

DROP TABLE IF EXISTS #DFTOTALVISUALIZACAO

SELECT NomCanal, SUM(NumVisualizacao) NumVisualizacao
INTO #DFTOTALVISUALIZACAO
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
GROUP BY NomCanal
HAVING SUM(NumVisualizacao) >= 1000000000 -- 1 bilhão

SELECT * 
FROM #DFTOTALVISUALIZACAO
ORDER BY NumVisualizacao DESC

INSERT INTO #DFTOTALVISUALIZACAO (NomCanal, NumVisualizacao)
VALUES ('Quintellão na Área',12327)

SELECT * 
FROM #DFTOTALVISUALIZACAO

-- 07 - ELIMINANDO REGISTROS DE UMA TABELA

SELECT * 
FROM #DFTOTALVISUALIZACAO
WHERE NomCanal = 'ibighit'

DELETE 
FROM #DFTOTALVISUALIZACAO
WHERE NomCanal = 'ibighit'

SELECT * 
FROM #DFTOTALVISUALIZACAO
WHERE NomCanal = 'ibighit'

-- 08 - ALTERAR UMA TABELA (INCLUINDO UMA NOVA COLUNA)

SELECT DISTINCT STATUS 
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]

ALTER TABLE [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
ADD STATUS BIT NOT NULL DEFAULT(1)

ALTER TABLE [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
DROP CONSTRAINT [DF__TB_VIDEOS__STATU__3C69FB99]

ALTER TABLE [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]
DROP COLUMN STATUS

SELECT * 
FROM [PYTHON].[dbo].[TB_VIDEOS_YOUTUBE]

-- 09 - UPDATE UMA TABELA (ATUALIZANDO VALORES DE ACORDO COM UMA CONDIÇÃO)

SELECT * FROM #DFTOTALVISUALIZACAO 
ORDER BY NumVisualizacao ASC

ALTER TABLE #DFTOTALVISUALIZACAO
ADD Classificacao VARCHAR(100)

UPDATE A
SET Classificacao = 'X1'
FROM #DFTOTALVISUALIZACAO A
WHERE NumVisualizacao < 1010955663 

UPDATE A
SET Classificacao = 
CASE WHEN NumVisualizacao < 1010955663 THEN 'X1'
WHEN NumVisualizacao >= 1010955663 AND NumVisualizacao < 1300000000 THEN 'X2'
WHEN NumVisualizacao >= 1300000000 AND NumVisualizacao < 1500000000 THEN 'X3'
ELSE 'X4'
END 
FROM #DFTOTALVISUALIZACAO A

SELECT * 
FROM #DFTOTALVISUALIZACAO

-- 10 - RELACIONAMENTOS (FAMOSOS JOINS)

-- 10.1 - INNER JOIN

-- DROP TABLE IF EXISTS dbo.TB_CATEGORIA_VIDEOS_YOUTUBE; 

SELECT * 
FROM dbo.TB_VIDEOS_YOUTUBE A

SELECT * 
FROM dbo.TB_CATEGORIA_VIDEOS_YOUTUBE A


SELECT *

FROM dbo.TB_VIDEOS_YOUTUBE A -- 10000 E APENAS 9989 

INNER JOIN dbo.TB_CATEGORIA_VIDEOS_YOUTUBE B

ON A.CodCategoriaVideo = B.CodCategoriaVideo


SELECT * 
FROM dbo.TB_VIDEOS_YOUTUBE A, dbo.TB_CATEGORIA_VIDEOS_YOUTUBE B

WHERE A.CodCategoriaVideo = B.CodCategoriaVideo

SELECT 
A.NomVideo
, B.NomCategoriaVideo 
, SUM(NumVisualizacao) TOTAL_NumVisualizacao
, SUM(NumLike) TOTAL_NumLike
, SUM(NumDislike) TOTAL_NumDislike
, SUM(NumComentario) TOTAL_NumComentario

FROM dbo.TB_VIDEOS_YOUTUBE A

INNER JOIN dbo.TB_CATEGORIA_VIDEOS_YOUTUBE B

ON A.CodCategoriaVideo = B.CodCategoriaVideo

GROUP BY A.NomVideo
, B.NomCategoriaVideo 


SELECT 
B.NomCategoriaVideo 
, SUM(NumVisualizacao) TOTAL_NumVisualizacao
, SUM(NumLike) TOTAL_NumLike
, SUM(NumDislike) TOTAL_NumDislike
, SUM(NumComentario) TOTAL_NumComentario

FROM dbo.TB_VIDEOS_YOUTUBE A

INNER JOIN dbo.TB_CATEGORIA_VIDEOS_YOUTUBE B

ON A.CodCategoriaVideo = B.CodCategoriaVideo

GROUP BY B.NomCategoriaVideo 

ORDER BY TOTAL_NumVisualizacao DESC

-- 10.2 - LEFT JOIN

INSERT INTO dbo.TB_VIDEOS_YOUTUBE
(CodVideoYouTube,NomVideo ,NomCanal, NumVisualizacao)
VALUES 
('asdq7yiwq','Aprenda SQL', 'Quintellão na Área',12327)

SELECT * 
FROM dbo.TB_VIDEOS_YOUTUBE A

LEFT JOIN dbo.TB_CATEGORIA_VIDEOS_YOUTUBE B

ON A.CodCategoriaVideo = B.CodCategoriaVideo

WHERE B.NomCategoriaVideo IS NULL

-- 10.3 - RIGHT JOIN 

SELECT B.*, A.* 
FROM dbo.TB_VIDEOS_YOUTUBE A

RIGHT JOIN dbo.TB_CATEGORIA_VIDEOS_YOUTUBE B

ON A.CodCategoriaVideo = B.CodCategoriaVideo

WHERE A.CodCategoriaVideo IS NULL