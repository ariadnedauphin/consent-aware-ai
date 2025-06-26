# boundary_model.py
# Consent Vector Representation and Update Logic

from datetime import datetime, time

class ConsentVector:
    def __init__(self):
        self.topics = {}
        self.emotional_threshold = 5  # default: 1 (low) to 10 (high)
        self.time_window = (time(8, 0), time(22, 0))  # default 8 AM to 10 PM
        self.behavioral_flags = {
            "notifications_enabled": True,
            "allow_personal_feedback": True
        }

    def set_topic_boundary(self, topic, allowed):
        self.topics[topic.lower()] = allowed

    def is_topic_allowed(self, topic):
        return self.topics.get(topic.lower(), True)

    def set_emotional_threshold(self, level):
        if 1 <= level <= 10:
            self.emotional_threshold = level

    def set_time_window(self, start: time, end: time):
        self.time_window = (start, end)

    def is_within_time_window(self):
        now = datetime.now().time()
        return self.time_window[0] <= now <= self.time_window[1]

    def toggle_behavior(self, flag):
        if flag in self.behavioral_flags:
            self.behavioral_flags[flag] = not self.behavioral_flags[flag]

    def get_status(self):
        return {
            "topics": self.topics,
            "emotional_threshold": self.emotional_threshold,
            "time_window": self.time_window,
            "behavioral_flags": self.behavioral_flags
        }

# Example usage
if __name__ == "__main__":
    cv = ConsentVector()
    cv.set_topic_boundary("family", False)
    cv.set_emotional_threshold(3)
    cv.set_time_window(time(9, 0), time(17, 0))
    cv.toggle_behavior("notifications_enabled")
    print(cv.get_status())
    print("Is 'politics' allowed?", cv.is_topic_allowed("politics"))
    print("Within time window?", cv.is_within_time_window())
