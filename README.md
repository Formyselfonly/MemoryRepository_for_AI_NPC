# Paper

[MemoryRepository for AI NPC](https://ieeexplore.ieee.org/document/10508558)

# MemoryRepository for AI NPC

## Architecture of MemoryRepository

- 介绍了MemoryRepository的结构组成
- 分别介绍了Memory Room,Memory Interaction,Memory Renewal Mechanism
- 包含图片
  - FIGURE 1. MemoryRepository Structure
- 包含表
  - TABLE 1. Notation used for modeling and scheduling

## Scheduling policy of MemoryRepository

- 介绍了MemoryRepository的执行流程
- 介绍了MemoryRepository的调度策略,即MemoryRepository的三个大模块之间是如何联系和运作的
- 包含图片
  - FIGURE 2. MemoryRepository Processing
- 包含算法流程
  - Algorithm 1 Memory Repository Processing

## Example:An AI NPC game powered by MemoryRepository

- 介绍了基于MemoryRepository搭建的虚拟小镇Example:StarUniverse的搭建过程
  - 对LLM使用开源游戏NPC相关数据进行微调
  - 嵌入MemoryRepository
- 介绍了在虚拟小镇上进行的实验
  - 用嵌入了MemoryRepository的LLM代理对话的NPC与
    没有嵌入MemoryRepository的LLM代理的对话的NPC
    进行对比
  - Human-Like对比结果(CaseStudy,一张对比
  - 图定性分析,无定量数据)
  - Long-Term Interaction对比结果(CaseStudy,一张对比图定性分析,无定向数据)
- 包含图片
  - FIGURE 3. StarUniverse
  - FIGURE 4. StarUniverse
  - FIGURE 5. Prompt Structure of NPC in MemoryRepository
  - FIGURE 6. Long-Term Comparable
  - FIGURE 7. Human-Like Comparable

## Experiments and Analysis

- 介绍了实验环境的搭建

  - 实验平台
  - 数据集
    - 训练集
    - 验证集
    - 测试集
  - 评估矩阵
    - Memory retrieval accuracy
    - Response Correctness
    - Contextual Coherence
    - Human-Like

- 介绍了实验

  - 实验步骤

    - 数据集的生成
    - 实验结果评估办法

  - 包含图

    - FIGURE 8. StreamLit-Constructed Local Website for Experimental
    - FIGURE 9. A segment of these historical records

  - 包含表

    - TABLE 2. Platform Specifications

  - 实验结果

    - **1.MemoryRepository Performance and Comparison**

      - 包含图
        - Figure 10(a) (b) (c) (d) 
      - 图片解析
        - a展示了
          - MemoryRepository使得Retrieval 甚至略微下降了
        - b展示了
          - MemoryRepository没有显著提升Correctness
        - c展示了
          - 没有MemoryRepository时,GPT3.5和GPT4已经有不错的表现啊
          - 嵌入MemoryRepository后对于GPT3.5和GPT4没有Coherence的显著提升
          - 没有MemoryRepository时,ChatGLM的性能表现很差
          - 嵌入MemoryRepository后对于ChatGLM有显著的Coherence提升
        - d展示了
          - MemoryRepository对于所有模型的Human-Like都能提供显著提升
        - 原因和说明
          - MemoryRepository的长期记忆会通过总结机制和遗忘机制保存在Long-term MemoryRoom,会遗忘掉相关性不强的信息,Long-term MemoryRoom是对更久远的记忆保存下来的长期记忆,更加总结性而不是十分细节,这导致检索时的精确性略微下降,从而Retrieval性能略微下降.   
          - 但是这对我们专注于Human-Like和Long-Term Interaction的目标没有影响
          - 当模型本身存在Coherence缺陷时,MemoryRepository可以给他带来显著提升. 
          - 而模型本身存在Coherence性能不错时,MemoryRepository无法给它带来显著提升. 
          - 这说明MemoryRepository通过这套记忆系统机制,使得不具备记忆机制的模型具备了长短期记忆的记忆机制,从而使得模型的连贯性Coherence能够得到显著提升.
          - MemoryRepository对于所有模型的Human-Like都能提供显著提升
          - 这是因为大部分模型都没有Human-Like的记忆设计,而MemoryRepository通过长短期记忆系统,以及总结和遗忘机制,使得模型的对话更加的Human-Like,从而显著提升了模型的Human-Like性能

    - **2.Performance comparison of MemoryRepository and**
      **MemGPT**

      - 对比了MemoryRepository and
        MemGPT
        依然是评估矩阵的四个指标
        Retrieval,Correctness,Coherence,Human Like

        MemGPT的Retrieval稍微高于MemoryRepository
        MemoryRepository的Human Like显著高于MemGPT
        Correctness和Coherence两者差不多
        说明MemoryRepository的记忆机制在提升了模型的长期交互能力外,还显著提升了模型的Human-Like能力

      - 包含表

        - TABLE 3. Comparison of MemGPT and MemoryRepository-embedded GPT-3.5 Performance in the 100th Round of Dialogue

    - **3.Performance Comparison of MemoryRepository-Enhanced LLMs Across Diverse Inference Parameters**

      - 包含图
        - Figure 11(a) (b) (c) (d)
      - 展示了MemoryRepository具有很好的多样性和鲁棒性,当模型参数调整时,MemoryRepository的功能依然存在.
        能够提升模型的Long-Term Interaction和Human-Like性能

# Code-MemoryRepository_ChatGPT

Some code and data related to MemoryRepository
