import numpy as np
#This function returns a list with the ids of the interacting questions.
def NetworkList_from_Array(ids_questions_with_concept,RelatedQuestionsList):
    NQuestions=len(ids_questions_with_concept)
    for Locquestion_1 in np.arange(NQuestions):
        question_1=ids_questions_with_concept[Locquestion_1]
        for Locquestion_2 in np.arange(Locquestion_1+1,NQuestions):
            question_2=ids_questions_with_concept[Locquestion_2]
            edge=[question_1,question_2]
            RelatedQuestionsList.append(edge)
    return RelatedQuestionsList
