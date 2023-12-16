'''
Name: tarotReading.py

Purpose: Runs the tarot card reading session for the user

Last Updated: 14 Dec 2023
'''
import LCGTarot
import datetime

major_arcana = [("The Fool","Beginnings, innocence, spontaneity, a free spirit"), 
                    ("The Fool - Reversed", "Holding back, recklessness, risk-taking"), 
                    ("The Magician", "Manifestation, resourcefulness, power, inspired action"),
                     ("The Magician - Reversed","Manipulation, poor planning, untapped talents"),
                     ("The High Priestess","Intuition, sacred knowledge, divine feminine, the subconscious mind"),
                     ("The High Priestess - Reversed","Secrets, disconnected from intuition, withdrawal and silence"),
                     ("The Empress","Femininity, beauty, nature, nurturing, abundance"),
                     ("The Empress - Reversed","Creative block, dependence on others"),
                     ("The Emperor","Authority, establishment, structure, a father figure"),
                     ("The Emperor - Reversed","Domination, excessive control, lack of discipline, inflexibility"),
                     ("The Hierophant","Spiritual wisdom, religious beliefs, conformity, tradition,institutions"),
                     ("The Hierophant - Reversed","Personal beliefs, freedom, challenging the status quo"),
                     ("The Lovers","Love, harmony, relationships, values alignment, choices"),
                     ("The Lovers - Reversed","Self-love, disharmony, imbalance, misalignment of values"),
                     ("The Chariot","Control, willpower, success, action, determination"),
                     ("The Chariot - Reversed"," Self-discipline, opposition, lack of direction"),
                     ("Strength","Strength, courage, persuasion, influence, compassion"),
                     ("Strength - Reversed","Inner strength, self-doubt, low energy, raw emotion"),
                     ("The Hermit","Soul-searching, introspection, being alone, inner guidance"),
                     ("The Hermit - Reversed","Isolation, loneliness, withdrawal"),
                     ("Wheel Of Fortune","Good luck, karma, life cycles, destiny, a turning point"),
                     ("Wheel Of Fortune - Reversed","Bad luck, resistance to change, breaking cycles"),
                     ("Justice","Justice, fairness, truth, cause and effect, law"),
                     ("Justice - Reversed","Unfairness, lack of accountability, dishonesty"),
                     ("The Hanged Man","Pause, surrender, letting go, new perspectives"),
                     ("The Hanged Man - Reversed","Delays, resistance, stalling, indecision"),
                     ("Death","Endings, change, transformation, transition"),
                     ("Death - Reversed","Resistance to change, personal transformation, inner purging"),
                     ("Temperance","Balance, moderation, patience, purpose"),
                     ("Temperance - Reversed","Imbalance, excess, self-healing, re-alignment"),
                     ("The Devil","Shadow self, attachment, addiction, restriction, sexuality"),
                     ("The Devil - Reversed","Releasing limiting beliefs, exploring dark thoughts, detachment"),
                     ("The Tower","Sudden change, upheaval, chaos, revelation, awakening"),
                     ("The Tower - Reversed","Personal transformation, fear of change, averting disaster"),
                     ("The Star","Hope, faith, purpose, renewal, spirituality"),
                     ("The Star - Reversed","Lack of faith, despair, self-trust, disconnection"),
                     ("The Moon","Illusion, fear, anxiety, subconscious, intuition"),
                     ("The Moon - Reversed","Release of fear, repressed emotion, inner confusion"),
                     ("The Sun","Positivity, fun, warmth, success, vitality"),
                     ("The Sun - Reversed","Inner child, feeling down, overly optimistic"),
                     ("Judgement","Judgement, rebirth, inner calling, absolution"),
                     ("Judgement - Reversed","Self-doubt, inner critic, ignoring the call"),
                     ("The World","Completion, integration, accomplishment, travel"),
                     ("The World - Reversed","Seeking personal closure, short-cuts, delays")]

def draw_card():
    # draws card using prng from LCG algorithm where the seed number is the time in microseconds
    today = datetime.datetime.now()
    now = today.microsecond
    now = LCGTarot.LCG_tarot(now)
    return (now%44)

def past_present_future():
    # draws a card for the past, present, and future for the user as well as shares the meanings behind the cards
    past = draw_card()
    print("Here is your past: ", major_arcana[past][0])
    present = draw_card()
    print("Here is your present: ", major_arcana[present][0])
    future = draw_card()
    print("Here is your future: ", major_arcana[future][0])

def question():
    # draws a card to answer a question for the user as well as shares the meaning behind the card
    answer = draw_card()
    print("Here is the answer to your question: ", answer)

if __name__ == "__main__":
    # source: https://biddytarot.com/tarot-card-meanings/major-arcana/ 
    print("\nWelcome to your tarot reading! We will only be using the 22 major arcana cards.\n")
    print("What would you like to do?\n")
    print("1: My Past, Present, and Future\n2: Answer My Question\n")
    selection = False
    # checks input and does corresponding action
    while(selection is False):
        input_reading = input("Type in the number that correspondes to what you want to do:")
        if (int(input_reading) == 1):
            selection = True
            past_present_future()
        elif (int(input_reading) == 2):
            selection = True
            question()
        else:
            print("Please enter a valid number.\n")
     

