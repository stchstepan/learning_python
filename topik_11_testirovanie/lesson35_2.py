from lesson35_1 import AnonymousSurvey
import unittest

print("\n#1")

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you!")
my_survey.show_results()

print("\n#2")

#class TestAnonymousSurvey(unittest.TestCase):
    #def test_store_single_response(self):
        #question = "What language did you first learn to speak?"
        #my_survey = AnonymousSurvey(question)
        #my_survey.store_response('English')
        #self.assertIn('English', my_survey.responses)

#if __name__ == '__main__':
   #unittest.main()

print("\n#3")

#class TestAnonymousSurvey(unittest.TestCase):
    #def test_store_single_response(self):
        #question = "What language did you first learn to speak?"
        #my_survey = AnonymousSurvey(question)
        #my_survey.store_response('English')
        #self.assertIn('English', my_survey.responses)

    #def test_store_three_responses(self):
        #question = "What language did you first learn to speak?"
        #my_survey = AnonymousSurvey(question)
        #responses = ['English', 'Spanish', 'Russian']
        #for response in responses:
            #my_survey.store_response(response)
        
        #for response in responses:
           #self.assertIn(response, my_survey.responses)

#if __name__ == '__main__':
    #unittest.main()

print("\n#4")

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Russian']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()