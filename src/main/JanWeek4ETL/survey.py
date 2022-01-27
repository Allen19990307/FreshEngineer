# from survey import AnonymousSurvey
class AnonymousServey:
    """收集匿名调查问卷的答案"""
    def __init__(self,question):
        """存储问题，并且为答案做准备"""
        self.question = question
        self.responses = []
    def show_question(self):
        """展现调查问卷"""
        print(self.question)
    def store_response(self,new_response):
        """存储单份的调查问卷"""
        self.responses.append(new_response)
    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results: ")
        for response in self.responses:
            print(f"-{response}")

