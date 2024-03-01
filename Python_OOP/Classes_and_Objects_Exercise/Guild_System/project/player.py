class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = self.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"{skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills_result = '\n'.join(f"=== {skill} - {mana}" for skill, mana in self.skills.items())
        return (f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\n"
                f"MP: {self.mp}\nSkills: {self.skills}\n"
                f"{skills_result}")