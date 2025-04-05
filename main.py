# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 17:26:50 2025

@author: asus
"""

from story import Hero, Sidekick, Villan, StoryProgress
from nlp_file import generate_story




def run_story():
    
    name = input("Enter Hero name: ")
    race = input("Enter Hero race: ")
    post = input("Enter Hero's secret title/post: ")
    skill = input("Enter Hero's special skill: ")
    chara = input("Describe Hero's personality: ")
    weapon = input("Enter the Hero's weapon: ")

    hero = Hero(name, race, post, skill, chara, weapon)

    s_name = input("Sidekick name: ")
    s_skill = input("Sidekick skill: ")
    s_chara = input("Sidekick personality: ")
    s_item = input("Important item Sidekick carries: ")

    sidekick = Sidekick(s_name, s_skill, s_chara, s_item,hero)

    v_name = input("Villan name: ")
    v_chara = input("Villan's personality: ")
    v_type = input("Villan's fighting type: ")
    v_castle = input("Villan's hideout location: ")

    villan = Villan(v_name, v_chara, v_type, v_castle)

    story = StoryProgress(
        goal="change mindest of villan", 
        fightscenenmber=3, 
        mysterynumber=2, 
        storytype="manhwa comic novel", 
        hero=hero, 
        sidekick=sidekick, 
        villan=villan
    )

    hero_back = hero.backstory()
    hero_now = hero.currenttimeline()
    sidekick_back = sidekick.backstory()
    villain_back = villan.backstory()
    villain_now = villan.currenttimeline()

    mystery_output = story.mysteryscenes()
    fights_output = story.fightiterators()
    ending_output = story.ending()
    
    context = f"""
[GENRE]: {story.storytype}
[GOAL]: {story.goal}

[HERO BACKSTORY]:
{hero_back}

[HERO CURRENT STATUS]:
{hero_now}

[SIDEKICK BACKSTORY]:
{sidekick_back}

[VILLAIN BACKSTORY]:
{villain_back}

[VILLAIN CURRENT STATUS]:
{villain_now}

[MYSTERIES]:
{mystery_output}

[FIGHTS]:
{fights_output or "No critical fight outcomes yet."}

[ENDING]:
{ending_output}

Now write a compelling, immersive fantasy story in third person using the information above. Stick to the tone of the genre: {story.storytype.capitalize()}.
Make sure the story develops progressively with character growth, drama, humor, and plot twists inspired by the events listed.
"""

    
    full_story = generate_story(context)
    print("\n===== Your Generated Story =====\n")
    print(full_story)


if __name__ == "__main__":
    run_story()