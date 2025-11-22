#!/usr/bin/env python3
"""
Tests for AI Story Teller application
"""

import unittest
from story_teller import StoryTeller


class TestStoryTeller(unittest.TestCase):
    """Test cases for StoryTeller class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.teller = StoryTeller()
    
    def test_greet_with_hi(self):
        """Test greeting with 'hi'"""
        response = self.teller.greet("hi")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_greet_with_hello(self):
        """Test greeting with 'hello'"""
        response = self.teller.greet("hello")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_greet_with_hey(self):
        """Test greeting with 'hey'"""
        response = self.teller.greet("hey")
        self.assertIsNotNone(response)
    
    def test_greet_with_hey_hi(self):
        """Test greeting with 'hey hi'"""
        response = self.teller.greet("hey hi")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_greet_case_insensitive(self):
        """Test that greeting is case insensitive"""
        response1 = self.teller.greet("HI")
        response2 = self.teller.greet("Hello")
        response3 = self.teller.greet("HEY")
        
        self.assertIsNotNone(response1)
        self.assertIsNotNone(response2)
        self.assertIsNotNone(response3)
    
    def test_non_greeting_returns_none(self):
        """Test that non-greetings return None from greet method"""
        response = self.teller.greet("tell me a story")
        self.assertIsNone(response)
    
    def test_generate_adventure_story(self):
        """Test adventure story generation"""
        story = self.teller.generate_story('adventure')
        self.assertIsNotNone(story)
        self.assertIsInstance(story, str)
        self.assertTrue(len(story) > 50)
    
    def test_generate_mystery_story(self):
        """Test mystery story generation"""
        story = self.teller.generate_story('mystery')
        self.assertIsNotNone(story)
        self.assertIsInstance(story, str)
        self.assertTrue(len(story) > 50)
    
    def test_generate_fantasy_story(self):
        """Test fantasy story generation"""
        story = self.teller.generate_story('fantasy')
        self.assertIsNotNone(story)
        self.assertIsInstance(story, str)
        self.assertTrue(len(story) > 50)
    
    def test_generate_invalid_type_defaults_to_adventure(self):
        """Test that invalid story type defaults to adventure"""
        story = self.teller.generate_story('invalid_type')
        self.assertIsNotNone(story)
        self.assertIsInstance(story, str)
    
    def test_chat_with_greeting(self):
        """Test chat interface with greeting"""
        response = self.teller.chat("hello")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_chat_with_story_request(self):
        """Test chat interface with story request"""
        response = self.teller.chat("tell me a story")
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 50)
    
    def test_chat_with_adventure_request(self):
        """Test chat interface with adventure story request"""
        response = self.teller.chat("I want an adventure story")
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 50)
    
    def test_chat_with_mystery_request(self):
        """Test chat interface with mystery story request"""
        response = self.teller.chat("tell me a mystery")
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 50)
    
    def test_chat_with_fantasy_request(self):
        """Test chat interface with fantasy story request"""
        response = self.teller.chat("I want a fantasy story")
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 50)
    
    def test_chat_with_unknown_input(self):
        """Test chat interface with unknown input"""
        response = self.teller.chat("what is the weather?")
        self.assertIsNotNone(response)
        self.assertIn("Story Teller", response)


if __name__ == "__main__":
    unittest.main()
