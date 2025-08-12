import numpy as np
def AdjacencyMatrixQuestions(ids_questions_with_concept,QAdjacencyMatrix):
    NQuestions=len(ids_questions_with_concept)
    for Locquestion_1 in np.arange(NQuestions):
        question_1=ids_questions_with_concept[Locquestion_1]
        for Locquestion_2 in np.arange(Locquestion_1+1,NQuestions):
            question_2=ids_questions_with_concept[Locquestion_2]
            QAdjacencyMatrix[question_1,question_2]+=1
            #QAdjacencyMatrix[question_2,question_1]+=1
    return QAdjacencyMatrix
