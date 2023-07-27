import pysbd

from deeppavlov.core.models.component import Component
from deeppavlov.core.common.registry import register


@register('sentence_delimiter')
def SentenceDelimiter(x_long):
    seg = pysbd.Segmenter(clean=False)
    xs = seg.segment(x_long[0])
    return tuple(xs)
    

