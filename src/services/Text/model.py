# Use a pipeline as a high-level helper
from transformers import pipeline
class TextModelService():
    PIPE =  pipe = pipeline("text-generation", model="Vikhrmodels/Vikhr-Nemo-12B-Instruct-R-21-09-24")
    def __init__(self):
        self.PIPE = pipeline("text-generation", model="Vikhrmodels/Vikhr-Nemo-12B-Instruct-R-21-09-24")
    def summarize(self):
        messages = [
            {"role": "system", "content": ""},
        ]
        pipe = pipeline("text-generation", model="Vikhrmodels/Vikhr-Nemo-12B-Instruct-R-21-09-24")
        return pipe(messages)