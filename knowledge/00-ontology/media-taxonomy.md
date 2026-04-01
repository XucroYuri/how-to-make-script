# Media Taxonomy

- `feature_film`: feature-length narrative designed around a single sustained arc.
- `episodic`: episode-based scripted narrative with installment logic.
- `short_drama`: compact serialized storytelling optimized for fast turn and retention.
- `animation`: scripts where visual design and action readability often need extra explicitness.
- `commercial`: direct-response or brand-message driven short script.
- `branded_film`: brand-backed narrative or cinematic communication asset.
- `shortform_video`: platform-native short script for rapid viewing environments.
- `game_narrative`: authored narrative embedded in player interaction systems.
- `branching_interactive`: explicitly branching narrative with choice-state consequences.

这套媒介 taxonomy 不是为了学术归档，而是为了避免不同媒介之间的方法混用。电影长片最怕中段塌，短剧最怕钩子虚，广告最怕卖点散，互动叙事最怕伪选择。先把媒介分清，后面的协议、评分标准和失败诊断才不会乱套。

这里暂时不把 `ai_video`、`seedance`、`sora` 之类工具面另立成新媒介。对当前仓库来说，它们更像下游输出表面或交付容器，应通过 `screen_to_video_brief` 这类桥接产物承接，而不是直接改变媒介 taxonomy。

## TODOs：待回答问题

- [ ] 当前媒介 taxonomy 是否需要补进“纪录式叙事”“综艺化脚本”“短视频剧情带货”等中文语境下常见但边界模糊的类型？
- [ ] 哪些项目会在开发中跨两个以上媒介包来回切换，仓库应如何避免误路由？
- [ ] 不同媒介之间哪些判断维度是共享的，哪些必须彻底分开写，才能避免“看似通用、实际失真”？
- [ ] 当同一项目同时包含宣发短视频、正片叙事、互动支线和品牌联动时，主媒介与附属媒介该如何判定？
- [ ] 媒介 taxonomy 需要按“观看环境”“时长结构”“交互权限”“商业目标”再切一层，还是保持当前单层分类更稳？
- [ ] 哪些媒介差异其实不是创作差异，而是工业交付差异，仓库是否需要单独建模？
- [ ] AI 视频、虚拟人直播脚本、可玩广告这类新形态，应被视为既有媒介的变体还是新媒介节点？
