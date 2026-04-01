---
{
  "id": "wp.visual-language-pack",
  "type": "workflow_protocol",
  "title": "多语种视觉语言包协议",
  "goal": "输出一份 task-specific 的 visual_language_pack，帮助剧本 Agent 或人类协作者在目标语言里更准确地表达镜头、灯光、动作、音频和文化美学锚点。",
  "input_contract": ["scene goal", "medium and stage", "target collaboration language", "aesthetic target", "production or model context"],
  "output_contract": ["visual_language_pack"],
  "preconditions": [
    "知道当前视觉语言包服务的任务类型",
    "知道目标语种、协作语境或至少知道需要 hybrid wording",
    "知道这次最需要控制的是镜头、光线、动作、音频还是文化气质"
  ],
  "steps": [
    "识别当前包主要服务的是跨团队沟通、模型提示、风格校准，还是 adaptation translation。",
    "在中文、日语、韩语、俄语、西语或 hybrid 模式中选择最合适的工作语言。",
    "只挑当前任务真正需要的词类：景别、运镜、镜头光学、构图、灯光、音频、动作、文化美学锚点。",
    "补一层 prompt delegation level，说明当前是气质级、动作级、时间切分级，还是编排级控制。",
    "如果这份语言包会直接服务 screen_to_video_brief 或 previz handoff，补一层 bridge-facing phrasing 和误读控制。",
    "输出 pack：包含精选术语、英文对照或 hybrid 锚点、prompt-ready phrases、使用禁忌与误读提醒。"
  ],
  "fallbacks": [
    "若用户没有指定语种，默认输出中文或当前工作语为主、英文技术锚点为辅的 hybrid 包。",
    "若用户真正要的是可执行视频生成 brief，而不是语言包，切到 screen-to-video-bridge。",
    "若用户最终还是要 screenplay 产物，只把 language pack 当附加参考，不替代主路由。"
  ],
  "stop_conditions": [
    "pack 已经足够支持当前任务，而不是退化成词典全文",
    "术语选择能明确改变下游镜头或表达决策",
    "输出包含误用警报和适用边界，而不是只有好看的词"
  ],
  "rubrics": ["rb.visual-language-pack"],
  "linked_atoms": ["ka.multilingual-visual-vocabulary", "ka.cultural-aesthetic-registers", "ka.prompt-delegation-levels", "ka.register-adaptation"]
}
---
# 多语种视觉语言包协议

这个协议不是为了炫多语种能力，而是为了让 Agent 和协作者在“视觉沟通”这件事上少失真。

很多任务并不需要完整剧本重写，只需要把某场戏、某个短片、某个广告段落翻成目标语言里更专业、更易执行的镜头话语。这个时候，最差的做法是全文翻译；更差的做法是扔一大堆术语表。真正有用的，是一份按任务精选的语言包。

所以 `visual_language_pack` 的核心不是全，而是准。它只保留当前任务真正有用的词类，并告诉你这些词是为了锁什么：镜头调度、气质锚点、动作密度，还是音频感受。这样它才能作为上游剧本和下游执行之间的一层轻接口，而不是新的一大坨上下文噪音。
如果它还要继续服务 bridge 层，它就必须进一步说明哪些词是给人类团队看的，哪些词是给模型或执行 brief 做精度锚定的。

## TODOs：待回答问题

- [ ] `visual_language_pack` 是否应该进一步拆成 crew-facing 和 model-facing 两种输出变体？
- [ ] 当用户既要语种迁移，又要品牌语体或 IP 声纹连续性时，这份包应该如何与 `voice_style_guide` 配合？
- [ ] 如果项目本身不是视频生成而是传统拍摄，这份包是否应输出更偏人类协作的版本？
- [ ] 哪些任务需要按语种提供不同的“禁忌词”清单，以避免误导生成模型或协作方？
