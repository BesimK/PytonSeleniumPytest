from _pytest.outcomes import Failed


class SoftAssertions:
    _errors = []

    @classmethod
    def assert_all(cls):
        if cls._errors:
            error_messages = "\n".join(str(error) for error in cls._errors)
            cls._errors = []  # Clear errors after asserting all
            raise Failed(f"Soft Assertions failed:\n{error_messages}")

    @classmethod
    def assert_that(cls, value, description="Non-Specified Element"):
        return SubAssertion(value, description)


class SubAssertion(SoftAssertions):

    def __init__(self, value, description):
        super().__init__()
        self.value = value
        self.description = description
        self.message = f"Assertion failed for {description} ->"

    def is_equal_to(self, other):
        if self.value != other:
            self._errors.append(Failed(f"{self.message} Expected {self.value} to be equal to {other}"))

    def is_not_equal_to(self, other):
        if self.value == other:
            self._errors.append(Failed(f"{self.message} Expected {self.value} to not be equal to {other}"))

    def is_true(self):
        if not self.value:
            self._errors.append(Failed(f"{self.message} Expected {self.value} to be True"))

    def is_false(self):
        if self.value:
            self._errors.append(Failed(f"{self.message} Expected {self.value} to be False"))

    def is_none(self):
        if self.value is not None:
            self._errors.append(Failed(f"{self.message} Expected {self.value} to be None"))

    def is_not_none(self):
        if self.value is None:
            self._errors.append(Failed(f"{self.message} Expected {self.value} to not be None"))

    def is_instance_of(self, cls):
        if not isinstance(self.value, cls):
            self._errors.append(Failed(f"{self.message} Expected {self.value} to be an instance of {cls}"))

    def is_not_instance_of(self, cls):
        if isinstance(self.value, cls):
            self._errors.append(Failed(f"{self.message} Expected {self.value} to not be an instance of {cls}"))

    def is_in(self, container):
        if self.value not in container:
            self._errors.append(Failed(f"{self.message} Expected {self.value} to be in {container}"))

    def is_not_in(self, container):
        if self.value in container:
            self._errors.append(Failed(f"{self.message} Expected {self.value} to not be in {container}"))
