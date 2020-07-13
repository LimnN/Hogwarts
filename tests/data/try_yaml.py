import yaml

string = """
animal: pets
pets:
  - dog
  - cat
  - fish
language:
  human:
    - Chinese
    - Japenese
    - English
  computer:
    - C
    - JAVA
    - Python
"""

result = yaml.load(string)
print(result)
