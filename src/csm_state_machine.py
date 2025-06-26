# csm_state_machine.py
# Consent State Manager (CSM) for Consent-Aware AI

from enum import Enum, auto

class ConsentState(Enum):
    FULL_CONSENT = auto()
    CONDITIONAL_CONSENT = auto()
    CONSENT_PAUSED = auto()
    CONSENT_REVOKED = auto()

class ConsentEvent(Enum):
    BOUNDARY_APPROACH = auto()
    USER_PAUSE = auto()
    VIOLATION_DETECTED = auto()
    REPAIR_COMPLETE = auto()
    USER_RESUME = auto()
    USER_REVOKE = auto()

class ConsentStateMachine:
    def __init__(self):
        self.state = ConsentState.FULL_CONSENT

    def handle_event(self, event):
        print(f"Current state: {self.state.name}, Event received: {event.name}")

        if self.state == ConsentState.FULL_CONSENT:
            if event == ConsentEvent.BOUNDARY_APPROACH:
                self.state = ConsentState.CONDITIONAL_CONSENT
            elif event == ConsentEvent.USER_REVOKE:
                self.state = ConsentState.CONSENT_REVOKED

        elif self.state == ConsentState.CONDITIONAL_CONSENT:
            if event == ConsentEvent.VIOLATION_DETECTED:
                self.state = ConsentState.CONSENT_PAUSED
            elif event == ConsentEvent.USER_REVOKE:
                self.state = ConsentState.CONSENT_REVOKED
            elif event == ConsentEvent.USER_RESUME:
                self.state = ConsentState.FULL_CONSENT

        elif self.state == ConsentState.CONSENT_PAUSED:
            if event == ConsentEvent.REPAIR_COMPLETE:
                self.state = ConsentState.CONDITIONAL_CONSENT
            elif event == ConsentEvent.USER_REVOKE:
                self.state = ConsentState.CONSENT_REVOKED

        elif self.state == ConsentState.CONSENT_REVOKED:
            if event == ConsentEvent.USER_RESUME:
                self.state = ConsentState.CONDITIONAL_CONSENT

        print(f"New state: {self.state.name}\n")
        return self.state

# Example usage
if __name__ == "__main__":
    csm = ConsentStateMachine()
    csm.handle_event(ConsentEvent.BOUNDARY_APPROACH)
    csm.handle_event(ConsentEvent.VIOLATION_DETECTED)
    csm.handle_event(ConsentEvent.REPAIR_COMPLETE)
    csm.handle_event(ConsentEvent.USER_REVOKE)
    csm.handle_event(ConsentEvent.USER_RESUME)
