from .authRoutes import SignupApi, LoginApi
from .personalSpace import CompanyPersonalSpace
from .SearchInternship import SearchEngine
from .internshipRoute import ApproveCandidate, OfferCandidate, FinishInternship

def initialize_routes(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(SearchEngine, '/api/search')
    api.add_resource(CompanyPersonalSpace, '/api/personalSpace/company')
    api.add_resource(ApproveCandidate, '/api/personalSpace/approveRequest')
    api.add_resource(OfferCandidate, '/api/personalSpace/setRequest')
    api.add_resource(FinishInternship, '/api/personalSpace/finishProject')


