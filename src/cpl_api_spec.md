# Consent Protocol Layer (CPL) API Specification

This document outlines the RESTful API endpoints and expected behavior for interacting with the Consent Protocol Layer (CPL) in consent-aware AI systems.

---

## 📘 Base URL

```
https://api.cpl.local/v1/
```

---

## 🔐 Authentication

All endpoints require a bearer token passed via the `Authorization` header:

```http
Authorization: Bearer YOUR_TOKEN_HERE
```

---

## 📌 Endpoints

### `GET /consent/state`

**Description:** Retrieve the current consent state and boundaries for the user session.

**Response:**

```json
{
  "consent_state": "FULL_CONSENT",
  "topics": {"family": false, "politics": true},
  "emotional_threshold": 4,
  "time_window": ["08:00", "20:00"],
  "behavioral_flags": {
    "notifications_enabled": true,
    "allow_personal_feedback": false
  }
}
```

---

### `POST /consent/update`

**Description:** Update one or more consent dimensions for the session.

**Request Body:**

```json
{
  "topics": {"trauma": false},
  "emotional_threshold": 6,
  "behavioral_flags": {"allow_personal_feedback": true}
}
```

**Response:**

```json
{
  "status": "success",
  "message": "Consent vector updated."
}
```

---

### `POST /consent/pause`

**Description:** Temporarily pauses consent for further interaction.

**Response:**

```json
{
  "consent_state": "CONSENT_PAUSED",
  "message": "Interaction paused. Awaiting explicit resume."
}
```

---

### `POST /consent/resume`

**Description:** Resumes interaction under last known consent configuration.

**Response:**

```json
{
  "consent_state": "CONDITIONAL_CONSENT",
  "message": "Interaction resumed with conditional boundaries."
}
```

---

### `POST /consent/revoke`

**Description:** Revokes consent and halts interaction.

**Response:**

```json
{
  "consent_state": "CONSENT_REVOKED",
  "message": "Consent revoked. Interaction terminated."
}
```

---

### `GET /consent/audit`

**Description:** Returns a history of consent updates and state transitions.

**Response:**

```json
[
  {
    "timestamp": "2025-06-26T14:35:12Z",
    "event": "emotional_threshold updated to 6"
  },
  {
    "timestamp": "2025-06-26T15:10:05Z",
    "event": "consent paused"
  }
]
```

---

## 🧠 Error Codes

| Code | Meaning                      |
| ---- | ---------------------------- |
| 400  | Malformed request            |
| 401  | Unauthorized                 |
| 403  | Forbidden action             |
| 409  | Conflict in state transition |
| 500  | Internal server error        |

---

## 📎 Integration Notes

* Every client session should begin with a `GET /consent/state` request.
* The CPL is stateless across sessions unless integrated with persistent identity layers.
* Sensitive domains should implement automated boundary triggers alongside manual controls.
