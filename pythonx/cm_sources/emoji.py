#!/usr/bin/env python

from cm import register_source, Base, getLogger
from neovim.api import Nvim

logger = getLogger(__name__)

register_source(name='ncm-emoji',
        abbreviation='emoji',
        word_pattern = r':[\w+\-]*',
        cm_refresh_length=2,
        priority=8)

class Source(Base):
    def __init__(self, nvim):
        super(Source, self).__init__(nvim)

    def cm_refresh(self,info,ctx):
        test = self.nvim.call('emoji#data#dict')
        logger.info("test: " + str(test['apple']))
        matches = []
        for name, code in test.items():
            if isinstance(code, list):
                emoji = "".join(map(chr, code))
            else:
                emoji = chr(code)
            matches += [dict(word=':'+name+':', menu=emoji)]
        self.complete(info, ctx, ctx['startcol'], matches)
