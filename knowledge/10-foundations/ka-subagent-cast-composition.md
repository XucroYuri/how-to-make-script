---
{
  "id": "ka.subagent-cast-composition",
  "type": "knowledge_atom",
  "title": "Subagent 阵容编排",
  "kind": "heuristic",
  "summary": "多智能体创作不是把所有专家都拉进场，而是用最小可用阵容覆盖真实决策压力，并给每个 subagent 清楚的职责、上下文包和退出条件。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "多智能体系统容易因为“专家越多越强”而失控，导致职责重叠、上下文泛滥、收敛速度下降，最后还不如一个清醒的 orchestrator。",
  "decision_rules": [
    "先选必须在场的核心功能角色，再补过程节点，最后才决定是否需要 persona lens。",
    "常规任务默认只配 3-7 个核心 subagent；只有当 artifact chain、risk profile 或 medium 明显增压时再扩容。",
    "每个 subagent 必须写清 mandate、输入包、输出包、merge 关系和 deactivate 条件。"
  ],
  "anti_patterns": [
    "每个环节都拉一堆名家 persona 进场",
    "多个 subagent 都声称拥有 final say",
    "阵容扩张了，但没有任何 lane trimming 规则"
  ],
  "prompt_primitives": [
    "这次任务最小可运行阵容应该由哪几类 subagent 组成",
    "哪些角色是核心决策者，哪些只是压力测试者",
    "如果阵容太大，哪几个 subagent 应该先被裁掉而不伤主判断"
  ],
  "evaluation_checks": [
    "阵容是否真的覆盖了当前项目的主要决策压力",
    "角色间是否存在清晰的 authority 和 merge 关系",
    "persona lens 是否被限制在辅助校准而非主导创作"
  ],
  "links": ["ka.team-topology-selection", "ka.process-node-specialization", "ka.convergence-owner-discipline", "ka.subagent-context-budgeting"],
  "source_status": "synthesized"
}
---
# Subagent 阵容编排

最强的多智能体系统，往往不是“人数最多”的那个，而是“阵容刚刚好”的那个。真正高质量的 subagent cast 必须像真实创作团队一样，知道谁负责发散、谁负责挑错、谁负责收束、谁有资格把事情拍板推进。

如果一个阵容里所有人都像“创作总监”，那它其实没有阵容，只有多份冲突中的总控。如果一个阵容里既有很多专家，又没有退场机制，那系统会自然滑向上下文拥堵和意见堆积。

这个 atom 的重点不是教系统“怎么多找人”，而是教系统“什么时候不该再加人”。越高水平的创作，越要克制阵容膨胀。

## TODOs：待回答问题

- [ ] 不同 team mode 下，最小可运行阵容是否应该有不同的上限和下限？
- [ ] 当用户要求“尽可能多专家同时参与”时，仓库应该如何保留丰富度但避免劣化？
- [ ] 哪些 persona lens 最适合只在 review 阶段出现，而不是提前参与 ideation？
- [ ] subagent 的 deactivate 条件是否应该成为 output contract 的固定字段？
- [ ] 阵容设计是否需要把 token / context cost 作为一等约束写进协议？
