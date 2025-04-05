
# 🧙‍♂️ AI Generative Fantasy Story Creator

A generative storytelling engine where you build your own characters — a Hero, Sidekick, and Villain — and feed their backstories, quirks, and goals into an LLM (Gemini) to create an immersive fantasy tale.

---

## 📝 Required Inputs

You'll be prompted to enter the following story elements:

### 🦸‍♂️ Hero Inputs:
| Prompt                     | Description |
|---------------------------|-------------|
| `Hero name`               | Name of the main protagonist |
| `Hero race`               | Elf, human, beastman, etc. |
| `Secret title/post`       | Hidden identity or noble post (e.g. "Duke", "Lost Prince") |
| `Special skill`           | Magic, combat talent, healing, etc. |
| `Personality`             | Introvert, stoic, brave, funny, etc. |
| `Weapon`                  | Magical staff, sword, etc. |

---

### 🧝 Sidekick Inputs:
| Prompt                         | Description |
|--------------------------------|-------------|
| `Sidekick name`                | Loyal companion's name |
| `Sidekick skill`               | Their special power or ability |
| `Sidekick personality`         | Supportive, bubbly, sharp, mysterious, etc. |
| `Important item they carry`    | Emotional item (e.g., "Pendant", "Old photo") |

---

### 😈 Villain Inputs:
| Prompt                         | Description |
|--------------------------------|-------------|
| `Villain name`                 | Antagonist's name |
| `Villain personality`          | Dark, tragic, power-hungry, etc. |
| `Fighting style/type`          | Swordsmanship, fire magic, manipulation |
| `Villain's hideout location`   | Dark tower, demon castle, desert tomb, etc. |

---

## 🧩 Narrative Control Inputs (StoryProgress Class)

These values let you customize the plot structure and tone:

| Parameter             | Description |
|-----------------------|-------------|
| `Goal`                | The Hero's final goal (e.g., "Revenge", "Justice", "Redemption") |
| `fightscenenmber`     | Number of intense fight scenes |
| `mysterynumber`       | Number of mysterious or emotional story reveals |
| `storytype`           | Story genre/type: `"Tragedy"`, `"Adventure"`, `"Comedy"`, etc. |

These shape the middle arc and emotional pull of the generated tale.

---

## 🌌 Prompt Generation Process

Once you enter your characters and story elements:

1. A **backstory** is generated for each character based on input.
2. A **dynamic story context** is constructed including:
   - Hero's journey
   - Sidekick's emotional arc
   - Villain's motive and tragedy
3. The plot is guided using:
   - Your selected `goal`
   - `number of mysteries`
   - `number of fight scenes`
   - `story type` (tone)
4. This `context` is passed to **Gemini LLM**, generating a deeply imaginative story.

---

## 🧪 Example Story Input & Generation

```text
Hero: Sam, Elf, Legendary Duke, Mage, Quiet but kind, Magical circles
Sidekick: Rony, Sword fighting, Bubbly and loyal, Pendant
Villain: Scar, Sarcastic and tragic, Dragon blade master, Demon Castle
Goal: Revenge
Mysteries: 2
Fights: 3
Story Type: Tragedy

