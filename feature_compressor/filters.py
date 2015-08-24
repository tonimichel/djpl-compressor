from compressor.filters import FilterBase
from compressor.filters import CompilerFilter


class SemicolonAppender(FilterBase):

    def input(self, filename=None, basename=None, **kwargs):
        return self.content.strip() + ';'


class UglifyFilter(CompilerFilter):
    command = "{binary} {args}"


class UglifyCSSFilter(UglifyFilter):
    options = (
        ("binary", 'uglifycss'),
        ("args", ''),
    )

class UglifyJSFilter(UglifyFilter):
    options = (
        ("binary", 'uglifyjs'),
        ("args", '-c --mangle'),
    )
