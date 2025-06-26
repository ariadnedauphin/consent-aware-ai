# streamlit_app_demo.py
# Streamlit interface for testing Consent Protocol Layer (CPL)

import streamlit as st
from datetime import time
from boundary_model import ConsentVector
from csm_state_machine import ConsentStateMachine, ConsentEvent

# Initialize state
if 'consent_vector' not in st.session_state:
    st.session_state.consent_vector = ConsentVector()

if 'csm' not in st.session_state:
    st.session_state.csm = ConsentStateMachine()

st.title("🧠 Consent-Aware AI: CPL Demo")
st.markdown("This interface simulates boundary-setting and consent flow for a fictional AI assistant.")

# Consent State Display
st.subheader("Consent State")
st.write(f"**Current State:** {st.session_state.csm.state.name}")

# Topical Boundaries
st.subheader("Topical Boundaries")
for topic in ["family", "politics", "trauma"]:
    allow = st.checkbox(f"Allow topic: {topic.title()}", value=st.session_state.consent_vector.is_topic_allowed(topic))
    st.session_state.consent_vector.set_topic_boundary(topic, allow)

# Emotional Threshold
st.subheader("Emotional Intensity")
emotion = st.slider("Max intensity (1-10)", 1, 10, st.session_state.consent_vector.emotional_threshold)
st.session_state.consent_vector.set_emotional_threshold(emotion)

# Time Window
st.subheader("Active Time Window")
start = st.time_input("Start", value=st.session_state.consent_vector.time_window[0])
end = st.time_input("End", value=st.session_state.consent_vector.time_window[1])
st.session_state.consent_vector.set_time_window(start, end)

# Behavioral Flags
st.subheader("Behavioral Flags")
notif = st.checkbox("Enable Notifications", value=st.session_state.consent_vector.behavioral_flags["notifications_enabled"])
feedback = st.checkbox("Allow Personal Feedback", value=st.session_state.consent_vector.behavioral_flags["allow_personal_feedback"])

st.session_state.consent_vector.behavioral_flags["notifications_enabled"] = notif
st.session_state.consent_vector.behavioral_flags["allow_personal_feedback"] = feedback

# Event Simulation
st.subheader("Simulate Consent Event")
event = st.selectbox("Trigger Event", ["BoundaryApproach", "ViolationDetected", "UserPause", "UserRevoke", "RepairComplete", "UserResume"])

if st.button("Apply Event"):
    evt = getattr(ConsentEvent, event.upper())
    st.session_state.csm.handle_event(evt)
    st.success(f"Event '{event}' processed.")

# Current Consent Vector
st.subheader("Consent Vector Snapshot")
st.json(st.session_state.consent_vector.get_status())
