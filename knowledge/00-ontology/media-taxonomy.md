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
