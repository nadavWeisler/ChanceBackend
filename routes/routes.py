from .authRoutes import SignupApi, LoginApi
from .personalSpace import CompanyPersonalSpace
from .SearchInternship import SearchEngine

def initialize_routes(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(SearchEngine, '/api/search')
    api.add_resource(CompanyPersonalSpace, '/api/personalSpace/company')

