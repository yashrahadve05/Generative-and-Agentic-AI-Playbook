# 03_Python_Code_Splitter.py

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade is a float (like 8.5 or 9.2)

    def get_details(self):
        return self.name"

    def is_passing(self):
        return self.grade >= 6.0


# Example usage
student1 = Student("Yash", 20, 8.2)
print(student1.get_details())

if student1.is_passing():
    print("The student is passing.")
else:
    print("The student is not passing.")

"""

# Initialise the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    # It supports multiple different languages for code splittig
    language = Language.PYTHON,
    chunk_size = 300,
    chunk_overlap = 0
)
# For more info Refer: https://docs.langchain.com/oss/python/integrations/splitters/code_splitter

# Split the text
text = splitter.split_text(text)

print(len(text))

print(text[1])