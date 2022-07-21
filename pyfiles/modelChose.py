from pyexpat import model
import pyfiles.models
# from pyfiles.w2vModel import result
class case:
    def __init__(self,case) -> None:
        self.case = case
    
    def choose(self,DOCUMENT,rat):
        if self.case==1:
            model1=pyfiles.models.model1()
            reslt= model1.result(DOCUMENT,int(rat))
            return reslt

        elif self.case==2:
            model=pyfiles.models.model2()
            DOCUMENT = model.cleanText(DOCUMENT)

            similarity_matrix = model.getSimmat(DOCUMENT)

            scores = model.run_page_rank(similarity_matrix)

            ret_sent = model.get_top_sentences(scores, DOCUMENT, int(rat))
            return ret_sent

        elif self.case==3:
            return result(DOCUMENT)
        # elif self.case==4:
        #     return 
        else:
            model=pyfiles.models.model2()
            DOCUMENT = model.cleanText(DOCUMENT)

            similarity_matrix = model.getSimmat(DOCUMENT)

            scores = model.run_page_rank(similarity_matrix)

            ret_sent = model.get_top_sentences(scores, DOCUMENT, int(rat))
            return ret_sent
    