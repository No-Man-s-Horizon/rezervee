from rest_framework.throttling import AnonRateThrottle, SimpleRateThrottle, UserRateThrottle


class RegisterThrottle(SimpleRateThrottle):
    scope = 'registerthrottle'

    def get_cache_key(self, request, view):
        if request.user.is_authenticated or request.method == "GET":
            return None  # Only throttle unauthenticated requests.

        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request)
        }


"""class RegisterThrottle(AnonRateThrottle):
    scope = 'registerthrottle' # Get authenticated user and block via IP"""


class ArticleListUserThrottle(UserRateThrottle):
    scope = 'postlistuserthrottle'
