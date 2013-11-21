from compressor.filters import FilterBase

class SemicolonAppender(FilterBase):

    def input(self, filename=None, basename=None, **kwargs):
        return self.content.strip() + ';'
