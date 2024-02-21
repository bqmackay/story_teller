#Use LangChain DallE API to generate images
## To do image generation locally, a powerful GPU/CPU is needed. 
## For mac, this means an M1 or better chip
## For windows, this means a CUDA-compatable chip
# from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
# import torch

# model_id = "stabilityai/stable-diffusion-2"

# scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
# pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)

# prompt = "a photo of an astronaut riding a horse on mars"
# image = pipe(prompt).images[0]

# image.save("image.png")

from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain.prompts import PromptTemplate
import urllib.request
from PIL import Image
import secrets

animal_descriptions={}

def generate_image(user_prompt)->str:
    # llm = OpenAI(temperature=0.0)
    # prompt = PromptTemplate(
    #     input_variables=["image_desc"],
    #     template="""
    #         List the results in the following order:
    #         1. 
    #         2. 
    #         ...

    #         List the animals found in this description: {image_desc}
    #     """
    # )
    # chain = LLMChain(llm=llm, prompt=prompt)
    # result = chain.run(user_prompt)
    # print(f'result: {result}')

    image_url = DallEAPIWrapper().run(f"""
                                      Digital painting of a distinctly male grey-eyed, yellow and orange giraffe with narrow cheeks, round eyes, a timid expression, standing on a rock; and 
                                      a distinctly female green-eyed, dark grey skin goat with clean white fur, with puffy cheeks, and hanging ears, and a happy expression, looking up at the giraffe excited in this scenario: {user_prompt}
                                      """)
    return image_url

def open_image(image_url, index):
    path = r"image-{index}-{hash}.png"
    path = path.format(index=index, hash=secrets.token_hex(6))
    urllib.request.urlretrieve(image_url, path)
    image = Image.open(path)
    image.show()

if __name__ == "__main__":
    url = generate_image("The giraffe and goat are excited to explore the jungle together")#, but they encounter a mean monkey who scares them away.")
    print(f"image_url: {url}")
    open_image(url, 0)