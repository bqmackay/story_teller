from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
import image_generator as image_generator

llm = OpenAI()

# template = """
#     As an expert writer, write an outline for a children's book. The book must have a clever ending that is a play on words. 

#     Base the story on the following description: {user_story}

#     The story should use simple words that a child can understand. The length of the story should be succinct, ultimately contianing less than 500 words. 

#     Assume the reader already knows the characters.
# """

template = """
    The output format must be a numbered outline:
    1. 
    2. 
    3. 
    ...

    As an expert children's writer, write a brief outline for a children's book with three or four points. The story's main problem should be presented in the first outline point. The story constantly builds towards a climax that is quickly resolved with a lighthearted ending. 

    Base the story on the following description: {user_story}

    Introductions for characters are not needed. Assume the reader already knows the characters.
"""

prompt = PromptTemplate.from_template(template=template)

llm_chain = LLMChain(prompt=prompt, llm=llm)

user_story = "A story about making new friends with the main characters being a giraffe and a goat. The giraffe personality is friendly, loyal, and timid. The goat's personality is sympathetic and brave. A third animal is a new friend and should be presented early in the story."

results = llm_chain.run(user_story)

plot_points=results.split("\n")
print(plot_points)

should_continue = input("Here is the outline. Do you wish to proceed? y/n (n)")



if should_continue.lower() != "y":
    print("Ending program")
    exit()

pages_completed = 0
for (i, plot) in enumerate(plot_points):
    if plot and pages_completed < 2:
        image_url = image_generator.generate_image(plot)
        image_generator.open_image(index=i, image_url=image_url)
        pages_completed = pages_completed + 1
