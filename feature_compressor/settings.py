

def refine_INSTALLED_APPS(original):
    return  ['compressor', 'feature_compressor'] + list(original)
    
    
def refine_STATICFILES_FINDERS(original):
    return list(original) + ['compressor.finders.CompressorFinder',]
    
introduce_COMPRESS_JS_FILTERS = ['feature_compressor.jsfilters.SemicolonAppender']
