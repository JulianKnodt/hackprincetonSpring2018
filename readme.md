# Hack Princeton Spring 2018

## Problem

Devise a method that can generate music given initial music

## Approach

Recurrent neural networks and preprocessing chords
so that they're not just a series of notes.

### What we did

First, we categorized the music into groups of "phrases",
and each phrase has specific characteristics that 
made it a phrase.

Then, we created a restricted boltzmann machine to generate
some phrases of our own

## Libraries
music21 (MIT)

TensorFlow (Google)
