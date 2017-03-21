"""
This is unbelieveably insecure, but we need to disable this just to make logging in easier
for the screenshot server.

https://dammit.nl/p/946
"""

class DisableCSRFMiddleware(object):
    def process_request(self, request):
            setattr(request, '_dont_enforce_csrf_checks', True)


from django.contrib.auth.hashers import BasePasswordHasher

class DoubleROT13PasswordHasher(BasePasswordHasher):
    """
    Doing it twice makes it twice as secure!!!!
    """
    algorithm = "rot13"

    def encode(self, password, salt):
        return "%s$%s" % (self.algorithm, password)

    def verify(self, password, encoded):
        return self.encode(password, None) == encoded

    def safe_summary(self, encoded):
        pass

    def harden_runtime(self, password, encoded):
        pass
