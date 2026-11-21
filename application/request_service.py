from domain.exceptions import DuplicateRequestIdError, RequestNotFoundError
from domain.service_request import ServiceRequest


class RequestService:
    """Application use cases for creating, viewing, searching, and resolving requests."""

    def __init__(self, repository):
        self.repository = repository
        self.requests = {}
        self._load_requests()

    def _load_requests(self):
        for data in self.repository.load():
            request = ServiceRequest.from_dict(data)
            self.requests[request.request_id.upper()] = request

    def _save_requests(self):
        self.repository.save([request.to_dict() for request in self.requests.values()])

    def create_request(self, request_id, employee_name, issue, priority):
        request_id = request_id.strip().upper()
        if request_id in self.requests:
            raise DuplicateRequestIdError(
                f"Request ID {request_id} already exists"
            )

        request = ServiceRequest(request_id, employee_name, issue, priority)
        self.requests[request.request_id.upper()] = request
        self._save_requests()
        return request

    def view_requests(self):
        return list(self.requests.values())

    def search_request(self, request_id):
        key = request_id.strip().upper()
        request = self.requests.get(key)
        if request is None:
            raise RequestNotFoundError(f"Request {key} not found")
        return request

    def resolve_request(self, request_id):
        request = self.search_request(request_id)
        request.resolve()  # OPEN -> RESOLVED belongs in the domain model
        self._save_requests()
        return request
