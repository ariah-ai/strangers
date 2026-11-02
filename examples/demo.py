"""Print what the model would see for the example feed: `python examples/demo.py`. The feed is fictional: Bramble is the
bot of a neighbourhood seed library, Ines Okafor is its human, and every handle is on the reserved .example domain."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import strangers  # noqa: E402

feed = json.load(open(os.path.join(HERE, "feed.json"), encoding="utf-8"))
print(strangers.block(feed, owner="Ines Okafor", agent="Bramble"))
