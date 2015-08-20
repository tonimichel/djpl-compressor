

def refine_INSTALLED_APPS(original):
    return  ['compressor', 'feature_compressor'] + list(original)


def refine_STATICFILES_FINDERS(original):
    return list(original) + ['compressor.finders.CompressorFinder',]

introduce_COMPRESS_ENABLED = True
introduce_COMPRESS_OUTPUT_DIR = ''
introduce_COMPRESS_JS_FILTERS = ['feature_compressor.filters.SemicolonAppender', 'feature_compressor.filters.YUglifyJSFilter']
introduce_COMPRESS_CSS_FILTERS = ['feature_compressor.filters.YUglifyCSSFilter']

introduce_COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
