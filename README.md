# 1.Paper

[MemoryRepository for AI NPC](https://ieeexplore.ieee.org/document/10508558)

# 2.Guide for read-MemoryRepository for AI NPC

This guide describes the content of each chapter.

## Architecture of MemoryRepository

- Introduces the structure of the MemoryRepository,which include three part:Memory Room, Memory Interaction, and Memory Renewal Mechanism.
- Provides a detailed explanation of the Memory Room, Memory Interaction, and Memory Renewal Mechanism.
- Includes figures:
  - FIGURE 1. MemoryRepository Structure.
- Includes tables:
  - TABLE 1. Notation used for modeling and scheduling.

## Scheduling Policy of MemoryRepository

- Describes the execution process of the MemoryRepository.
- Explains the scheduling policy of the MemoryRepository, detailing how its three major modules are interconnected and operate.
- Includes figures:
  - FIGURE 2. MemoryRepository Processing.
- Includes algorithm flow:
  - Algorithm 1: Memory Repository Processing.

## Example: An AI NPC Game Powered by MemoryRepository

- Details the process of building the virtual town, Example: StarUniverse, using MemoryRepository.
  - Fine-tuned an LLM using open-source NPC-related game data.
  - Integrated the MemoryRepository.
- Describes the experiments conducted in the virtual town:
  - Comparison of NPC dialogues powered by an LLM with and without the MemoryRepository.
  - Human-Like comparison results (Case Study, a qualitative comparison image, no quantitative data).
  - Long-Term Interaction comparison results (Case Study, a qualitative comparison image, no quantitative data).
- Includes figures:
  - FIGURE 3. StarUniverse.
  - FIGURE 4. StarUniverse.
  - FIGURE 5. Prompt Structure of NPC in MemoryRepository.
  - FIGURE 6. Long-Term Comparable.
  - FIGURE 7. Human-Like Comparable.

## Experiments and Analysis

- Describes the experimental setup:
  - Platform used.
  - Datasets:
    - Training set.
    - Validation set.
    - Test set.
  - Evaluation metrics:
    - Memory retrieval accuracy.
    - Response correctness.
    - Contextual coherence.
    - Human-Like.
- Explains the experiment:
  - Experimental steps:
    - Data generation.
    - Evaluation methods for experimental results.
  - Includes figures:
    - FIGURE 8. StreamLit-Constructed Local Website for Experimental.
    - FIGURE 9. A segment of these historical records.
  - Includes tables:
    - TABLE 2. Platform Specifications.
  - Experimental results:
    - **1. MemoryRepository Performance and Comparison**
      - Includes figures:
        - Figure 10(a) (b) (c) (d).
      - Analysis of figures:
        - (a) shows that retrieval performance slightly decreased with the MemoryRepository.
        - (b) shows that the MemoryRepository did not significantly improve correctness.
        - (c) shows that GPT-3.5 and GPT-4 performed well even without the MemoryRepository.
          - The integration of the MemoryRepository did not significantly enhance coherence for GPT-3.5 and GPT-4.
          - Without the MemoryRepository, ChatGLM performed poorly.
          - With the MemoryRepository, there was a significant improvement in coherence for ChatGLM.
        - (d) shows that the MemoryRepository significantly improved Human-Like performance across all models.
        - Explanation:
          - The MemoryRepository's long-term memory mechanism stores information in the Long-term MemoryRoom through summarization and forgetting processes, discarding less relevant information. This slightly decreases retrieval accuracy but aligns with the goal of focusing on Human-Like and Long-Term Interaction.
          - When a model has coherence issues, the MemoryRepository can provide a significant improvement.
          - If a model already has strong coherence performance, the MemoryRepository cannot offer much improvement.
          - This indicates that the MemoryRepository's memory system endows models without inherent memory mechanisms with both short-term and long-term memory, significantly enhancing coherence.
          - The MemoryRepository provides a notable improvement in Human-Like performance for all models.
          - This is because most models lack a Human-Like memory design, but the MemoryRepository, through its short-term and long-term memory system along with summarization and forgetting mechanisms, makes model dialogues more human-like, thereby significantly enhancing Human-Like performance.
    - **2. Performance Comparison of MemoryRepository and MemGPT**
      - Comparison between MemoryRepository and MemGPT using the four evaluation metrics: Retrieval, Correctness, Coherence, and Human-Like.
        - MemGPT slightly outperforms MemoryRepository in Retrieval.
        - MemoryRepository significantly outperforms MemGPT in Human-Like.
        - Correctness and Coherence are similar for both.
        - This shows that the MemoryRepository’s memory mechanism not only enhances long-term interaction but also significantly improves Human-Like capabilities.
      - Includes tables:
        - TABLE 3. Comparison of MemGPT and MemoryRepository-embedded GPT-3.5 Performance in the 100th Round of Dialogue.
    - **3. Performance Comparison of MemoryRepository-Enhanced LLMs Across Diverse Inference Parameters**
      - Includes figures:
        - Figure 11(a) (b) (c) (d).
      - Shows that the MemoryRepository exhibits good diversity and robustness, maintaining its functionality even when model parameters are adjusted.
        - It can improve Long-Term Interaction and Human-Like performance.

# 3.Code - MemoryRepository_ChatGPT

Some code and data related to MemoryRepository are available, but a full codebase is not provided. 
Only partial implementation and key snippets necessary for understanding and experimenting with the MemoryRepository framework are included.