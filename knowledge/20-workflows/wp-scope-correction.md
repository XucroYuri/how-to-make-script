---
{
  "id": "wp.scope-correction",
  "type": "workflow_protocol",
  "title": "范围修正协议",
  "goal": "当一条规则、路由、rubric 或知识说法被挑战时，输出一份 scope_correction，而不是只做二元否定或教条防守。",
  "input_contract": ["challenged claim", "counterexample", "failure context", "current file or route", "none"],
  "output_contract": ["scope_correction"],
  "preconditions": [
    "用户已经指出一个可定位的 claim、route、rubric 或规则",
    "至少存在一个失败上下文、反例或适用范围争议"
  ],
  "steps": [
    "锁定被挑战的原始说法，避免把真正的问题改写掉。",
    "找出原说法中仍然成立的最小核心，而不是直接把它整体抹掉。",
    "写出至少一个失效条件、反例上下文或边界触发点，说明原说法为什么过宽。",
    "把原说法改写成带适用边界的 scope_correction，并标注是否需要保留并行路径。",
    "说明这次范围修正会影响哪些 route、rubric、fixture 或 docs。"
  ],
  "fallbacks": [
    "若反例仍然模糊，先要求最小失败案例，再暂缓正式修正。",
    "若原说法根本没有任何可保留核心，明确标记为 total replacement 而不是伪 scope correction。"
  ],
  "stop_conditions": [
    "修正后的说法保留了一个清楚的 surviving core",
    "至少写明一个失效条件和一个适用边界",
    "明确说明后续哪些资产需要跟进更新"
  ],
  "rubrics": ["rb.scope-correction"],
  "linked_atoms": ["ka.scope-correction", "ka.false-universal-warning", "ka.creative-pluralism", "ka.boundary-first-guidance"]
}
---
# 范围修正协议

这个协议的作用，不是给维护者一个更体面的“打圆场”方式，而是让仓库在面对反驳时有第三种动作：既不把所有规则都护成神谕，也不把所有规则都一脚踢翻。

真正有价值的 scope correction，必须保留仍然成立的核心判断，同时诚实写出它为什么不能再冒充普遍规律。这样一来，仓库吸收反例后会变得更窄、更准，而不是更飘。

如果这个协议执行得好，社区提出的强反驳就不会总落成“谁赢谁输”的争论，而会更频繁地变成“原规则留下什么、删掉什么、缩到哪里”的建设性修正。

## TODOs：待回答问题

- [ ] 哪些 challenge 最适合走 scope correction，而不是 total replacement？
- [ ] scope correction 是否应该默认要求一个 fixture，还是只在 route/rubric 受影响时要求？
- [ ] 当 surviving core 很弱时，什么程度还值得保留？
- [ ] 是否需要一个标准段落格式来表达“原说法 / 失效条件 / 修正版 / 影响面”？
- [ ] 如果 scope correction 连续发生多次，何时该把原规则拆成多个独立资产？
