from compressor.filters import FilterBase
from compressor.filters import CompilerFilter


class SemicolonAppender(FilterBase):

    def input(self, filename=None, basename=None, **kwargs):
        return self.content.strip() + ';'


class YUglifyFilter(CompilerFilter):
    command = "{binary} {args}"

    def __init__(self, *args, **kwargs):
        super(YUglifyFilter, self).__init__(*args, **kwargs)
        self.command += ' --type=%s' % self.type


class YUglifyCSSFilter(YUglifyFilter):
    type = 'css'
    options = (
        ("binary", 'yuglify'),
        ("args", '--terminal'),
    )


class YUglifyJSFilter(YUglifyFilter):
    type = 'js'
    options = (
        ("binary", 'yuglify'),
        ("args", '--terminal'),
    )
