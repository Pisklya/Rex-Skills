# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import print_function

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger
from mycroft.skills.context import *

import os
import string
import re

__author__ = 'TREE'

LOGGER = getLogger(__name__)


class MathSkill(MycroftSkill):
    def __init__(self):
        super(MathSkill, self).__init__(name="MathSkill")
    
    @intent_handler(IntentBuilder("MathStartIntent").require("MathStart").build())
    @adds_context('MathContext')
    def handle_math_start(self, message):
        self.speak('Please provide the first number.',  expect_response=True)
    
    @intent_handler(IntentBuilder("FirstNumberIntent").require("Num1").require("MathContext").build())
    @adds_context('FirstNumberContext')
    def handle_first_number(self, message):
        #utterance = message.data.get('utterance')
        self.num1 = message.data.get("Num1")
        self.speak('Please provide the second number.',  expect_response=True)
        print(self.num1)


    @intent_handler(IntentBuilder("SecondNumberIntent").require("Num2").require("FirstNumberContext").build())
    @adds_context('SecondNumberContext')
    @removes_context('FirstNumberContext')
    def handle_second_number(self, message):
        #utterance = message.data.get('utterance')
        self.num2 = message.data.get("Num2")
        self.speak('What operation would you like to do',  expect_response=True)
        print(self.num2)

    @intent_handler(IntentBuilder('CalculateIntent').require('Calculate').require('SecondNumberContext').build())
    @adds_context('CalculateContext')
    @removes_context('SecondNumberContext')
    def handle_calculate(self, message):
        utterance = message.data.get('utterance')
        #print(utterance)
        if "add" in utterance:
            self.answer = float(self.num1) + float(self.num2)
            self.speak('The answer is %s.' % (self.answer))
        elif "multiply" in utterance:
            self.answer = float(self.num1) * float(self.num2)
            self.speak('The answer is %s.' % (self.answer))
        elif "divide" in utterance:
            self.answer = float(self.num1) / float(self.num2)
            self.speak('The answer is %s.' % (self.answer))
        elif "subtract" in utterance:
            self.answer = float(self.num1) - float(self.num2)
            self.speak('The answer is %s.' % (self.answer))
        self.speak('Would you like to perform another operation?',  expect_response=True)

            
    @intent_handler(IntentBuilder('NextCalculationIntent').require('Calculate').require('Num').require('CalculateContext').build())
    def handle_next_calculation(self, message):
        utterance = message.data.get('utterance')
        self.num = message.data.get("Num")
        print(utterance)
        print(self.num)
        if "add" in utterance:
            self.answer = float(self.answer) + float(self.num)
            self.speak('The answer is %s.' % (self.answer))
        elif "multiply" in utterance:
            self.answer = float(self.answer) * float(self.num)
            self.speak('The answer is %s.' % (self.answer))
        elif "x" in utterance:
            self.answer = float(self.answer) * float(self.num)
            self.speak('The answer is %s.' % (self.answer))
        elif "divide" in utterance:
            self.answer = float(self.answer) / float(self.num)
            self.speak('The answer is %s.' % (self.answer))
        elif "subtract" in utterance:
            self.answer = float(self.answer) - float(self.num)
            self.speak('The answer is %s.' % (self.answer))
        self.speak('Would you like to perform another operation?',  expect_response=True)

def create_skill():
    return MathSkill()
