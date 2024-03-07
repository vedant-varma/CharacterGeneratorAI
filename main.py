from openai import OpenAI
import webbrowser

client = OpenAI(api_key='MY_KEY')


class Entity:
    def __init__(self, name, age, height, strength, gender):
        self.name = name
        self.age = age
        self.height = height
        self.strength = strength
        self.gender = gender
        self.metadata = f"My name is {name}. My age is {age}. My height is {height}. I am {strength}. I am a {gender}."


class Human(Entity):
    def __init__(self, ethnicity, culture, skin_color, mood, name, age, height, strength, gender):
        super().__init__(name, age, height, strength, gender)
        self.ethnicity = ethnicity
        self.culture = culture
        self.skin_color = skin_color
        self.mood = mood
        self.metadata += f" My ethnicity is {ethnicity}. My culture is {culture}. My skin color is {skin_color}. I am usually in a {mood} mood."

    def intro(self):
        print(self.metadata)


bot = Human("Scandinavian", "American", "FOB8A0", "Patriotic", "Jason", "30", "6'2", "decently strong", "male")
bot.intro()

response = client.images.generate(
    model="dall-e-3",
    prompt= bot.metadata,
    size="1024x1024",
    quality="standard",
    n=1
)

image_url = response.data[0].url
webbrowser.open(image_url)
