#!/usr/bin/env python3
"""
AI Story Teller - A simple AI-based story generation application with chat functionality
"""

import random
import re


class StoryTeller:
    """AI Story Teller that can greet users and generate stories"""
    
    def __init__(self):
        self.greetings = [
            "Hello! I'm your AI Story Teller. What kind of story would you like to hear?",
            "Hi there! Ready for an amazing story adventure?",
            "Greetings! I'm here to tell you wonderful stories!",
            "Hey! Let me craft a magical story for you!",
            "Hello friend! What story shall we create today?"
        ]
        
        self.story_templates = {
            'adventure': [
                "Once upon a time, a brave {hero} set out on a journey to {place}. "
                "Along the way, they encountered a {creature} and had to {action}. "
                "In the end, {hero} {outcome} and returned home victorious!",
                
                "In a land far away, {hero} discovered a mysterious {object}. "
                "This {object} led them to {place} where they met a wise {creature}. "
                "Together they {action} and {outcome}. The adventure changed them forever!"
            ],
            'mystery': [
                "It was a dark and stormy night when {hero} noticed something strange. "
                "A {object} was missing from {place}! They had to {action} to solve the mystery. "
                "After careful investigation, {hero} {outcome} and the truth was revealed!",
                
                "The curious case of the {object} baffled everyone in {place}. "
                "{hero} took it upon themselves to investigate. They {action} and discovered "
                "that a {creature} was behind it all. Finally, {hero} {outcome}!"
            ],
            'fantasy': [
                "In a magical realm called {place}, {hero} possessed unique powers. "
                "When a {creature} threatened the land, {hero} had to {action}. "
                "Using their magic, {hero} {outcome} and peace was restored!",
                
                "Long ago in {place}, there lived a legendary {hero}. "
                "They found an enchanted {object} guarded by a {creature}. "
                "To claim it, {hero} had to {action}. With courage, {hero} {outcome}!"
            ]
        }
        
        self.story_elements = {
            'hero': ['a young knight', 'a clever detective', 'a brave explorer', 
                     'a wise wizard', 'a skilled archer', 'a curious scientist'],
            'place': ['the Enchanted Forest', 'the Ancient Temple', 'the Mystic Mountains',
                      'the Crystal Caves', 'the Forgotten City', 'the Dragon\'s Lair'],
            'creature': ['dragon', 'giant spider', 'wise owl', 'mysterious stranger',
                        'ancient guardian', 'magical phoenix'],
            'object': ['golden crown', 'ancient scroll', 'magic sword', 'mysterious amulet',
                      'enchanted book', 'crystal orb'],
            'action': ['solve ancient riddles', 'battle fierce monsters', 'cross dangerous bridges',
                      'decipher mysterious codes', 'make difficult choices', 'overcome their fears'],
            'outcome': ['saved the kingdom', 'found the truth', 'discovered their destiny',
                       'became a legend', 'learned valuable lessons', 'united the people']
        }
    
    def greet(self, user_message=""):
        """Respond to user greetings"""
        user_message_lower = user_message.lower().strip()
        
        # Check if it's a greeting
        greet_patterns = ['hi', 'hello', 'hey', 'greetings', 'good morning', 
                         'good afternoon', 'good evening', 'howdy']
        
        if any(pattern in user_message_lower for pattern in greet_patterns):
            return random.choice(self.greetings)
        
        return None
    
    def generate_story(self, story_type='adventure'):
        """Generate a random story based on the type"""
        if story_type not in self.story_templates:
            story_type = 'adventure'
        
        template = random.choice(self.story_templates[story_type])
        
        # Fill in the template with random elements
        story = template
        for element_type, options in self.story_elements.items():
            if '{' + element_type + '}' in story:
                story = story.replace('{' + element_type + '}', random.choice(options))
        
        return story
    
    def chat(self, user_message):
        """Main chat interface"""
        # First check for greetings
        greeting_response = self.greet(user_message)
        if greeting_response:
            return greeting_response
        
        # Check for story type requests
        user_message_lower = user_message.lower()
        
        if 'adventure' in user_message_lower:
            return self.generate_story('adventure')
        elif 'mystery' in user_message_lower:
            return self.generate_story('mystery')
        elif 'fantasy' in user_message_lower:
            return self.generate_story('fantasy')
        elif 'story' in user_message_lower or 'tell' in user_message_lower:
            # Random story type
            story_type = random.choice(list(self.story_templates.keys()))
            return self.generate_story(story_type)
        else:
            return ("I'm an AI Story Teller! You can:\n"
                   "- Greet me with 'hi' or 'hello'\n"
                   "- Ask for a story (adventure, mystery, or fantasy)\n"
                   "- Type 'quit' or 'exit' to leave")


def main():
    """Main function to run the interactive story teller"""
    teller = StoryTeller()
    
    print("=" * 60)
    print("Welcome to AI Story Teller!")
    print("=" * 60)
    print(teller.chat("hello"))
    print("\nType 'quit' or 'exit' to end the conversation.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print("\nAI Story Teller: Goodbye! Come back soon for more stories!")
                break
            
            response = teller.chat(user_input)
            print(f"\nAI Story Teller: {response}\n")
            
        except (KeyboardInterrupt, EOFError):
            print("\n\nAI Story Teller: Goodbye! Come back soon for more stories!")
            break


if __name__ == "__main__":
    main()
