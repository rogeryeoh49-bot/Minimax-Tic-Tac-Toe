# Minimax Tic-Tac-Toe

> An unbeatable Tic-Tac-Toe AI built from scratch using the Minimax algorithm.

This project was built during an AI summer school as a hands-on project.

At the time, I only had a basic understanding of programming and algorithms, and the project had to be completed within a limited amount of time. Rather than following a finished implementation, I built the game and AI from scratch and worked out how Minimax could be applied to the game as I went.

## What I Built

- A fully playable Tic-Tac-Toe game
- An AI opponent powered by the Minimax algorithm
- Game-tree search for evaluating possible moves
- An AI that cannot be beaten when played correctly
- A graphical interface for playing against the AI

## The Core Idea

The AI explores possible future game states and assigns each outcome a score:

```text
Win  → +1
Draw →  0
Loss → -1
