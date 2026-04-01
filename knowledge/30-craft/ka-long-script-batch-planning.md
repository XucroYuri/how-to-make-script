---
{
  "id": "ka.long-script-batch-planning",
  "type": "knowledge_atom",
  "title": "长文本分批规划",
  "kind": "technique",
  "summary": "长剧本不是先粗暴切批再理解结构，而应先识别 scene / beat 组织，再决定批次边界，这样批处理改变的是窗口，不是真相。",
  "mediums": ["feature_film", "episodic", "animation", "short_drama", "commercial", "branded_film"],
  "stages": ["outline", "scene", "adaptation"],
  "problem": "长文本处理中，批次切分先于结构理解，导致语义断裂、节奏错判和桥接漂移。",
  "decision_rules": [
    "先看 scene 和 beat 的真实边界，再决定批处理边界。",
    "批次应该服务处理稳定性，而不是替代结构判断。",
    "如果批次切分让因果链、动作线或关系线断掉，就说明切法有问题。"
  ],
  "anti_patterns": [
    "按行数机械切批，不看结构单元",
    "先生成 processing plan，再反向猜结构",
    "每个批次都像独立片段，合起来却不是原场景"
  ],
  "prompt_primitives": [
    "当前文本的最小稳定结构单元是什么",
    "哪些地方绝不能被批次切断",
    "批次合并回去后，原场景关系和动作线是否仍完整"
  ],
  "evaluation_checks": [
    "批次边界是否尊重 scene / beat 结构",
    "合并后是否能恢复原有连续性",
    "批处理是否只是窗口优化，而非事实改写"
  ],
  "links": ["ka.source-span-traceability", "ka.video-generation-shot-economy", "ka.bounded-context-loading"],
  "source_status": "derived"
}
---
# 长文本分批规划

长文本处理最大的错觉是：先切批，后理解，也能“差不多还原”结构。实际通常不是。

只要批次边界先于结构边界，scene 的动作线、关系线、信息线就会被切坏。后面再怎么“汇总”，也只是在补一个已经被破坏的上游对象。

所以分批规划的前提，不是 token 压力，而是结构识别。结构先，批次后。

## TODOs：待回答问题

- [ ] scene 边界不稳、beat 本身松散的文本，应该先做什么级别的稳定化处理？
- [ ] 长剧本在 scene 内部又极度复杂时，beat 级和 shot 级切分的界线该如何定？
- [ ] 仓库未来是否需要把 batch planning 独立成更明确的 bridge 子协议？
