# Cookies: The Complete Guide

Cookies are one of the most important concepts in web development and authentication. They are small pieces of data stored on the client side (browser) and sent to the server with every request.

## 1. What is a Cookie?

A cookie is a small text file stored in the browser that contains data such as:

- Session identifiers
- User preferences
- Tracking information

Cookies allow the server to remember a user between requests since HTTP is stateless.

## 2. How Cookies Are Used

Server sets a cookie:

```
Set-Cookie: session_id=abc123; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=3600
```

Browser stores it and sends it automatically with every matching request:

```
GET /dashboard
Cookie: session_id=abc123
```

Server reads cookie → identifies user/session → returns response.

## 3. Cookie Properties

### 1. Sent with Every Request

Browsers automatically include cookies in requests to the domain/path that set the cookie.

This is why cookies are useful for sessions and authentication.

### 2. Cookie Scope

- **Domain**: The domain(s) that can receive the cookie.
- **Path**: URL path that can access the cookie.

Cookies outside their scope are not sent.

### 3. Expiration

- **Expires**: Sets a fixed date/time for the cookie to expire.
- **Max-Age**: Sets a lifetime in seconds (from the time of creation).

### 4. SameSite

Prevents sending cookies on cross-site requests:

- **Strict**: Cookie only sent to same-site requests.
- **Lax**: Cookie sent on top-level navigation GET requests.
- **None**: Cookie sent in all requests, must use Secure.

## 4. Cookie Types

### 1. Session Cookie

- Deleted when browser closes.
- Usually used for authentication.
- Example: `session_id=abc123; Path=/; HttpOnly; Secure`

### 2. Permanent Cookie

- Has expiration date or max-age → persists after browser closes.
- Example: `remember_me_token=xyz; Max-Age=2592000` (30 days)
- Used for “Remember Me” functionality.

### 3. HttpOnly Cookie

- Not accessible via JavaScript → protects against XSS attacks.
- Example: `session_id=abc123; HttpOnly; Secure`

### 4. Secure Cookie

- Only sent over HTTPS → prevents network sniffing.
- Example: `session_id=abc123; Secure`

### 5. Third-Party Cookie

- Set by domains other than the one in the browser address bar.
- Used for tracking or advertising.
- Example: Ads, analytics tools.

### 6. Zombie Cookie

- Resurrects itself after deletion (often via Flash or local storage backup).
- Considered malicious → used for persistent tracking.

## 5. Cookie Security Concerns

### 1. Stealing Cookies

**Attackers can steal cookies via**:

- XSS (Cross-Site Scripting) → JavaScript reads cookies.
- Network sniffing → sending cookies over HTTP.

**Prevention**:

- Use HttpOnly cookies to block JS access.
- Use Secure cookies → only over HTTPS.
- Use SameSite cookies to prevent cross-site attacks.

### 2. Cross-Site Request Forgery (CSRF)

**Exploit**: Attacker makes the browser send cookie automatically to a trusted site without the user’s intent.

**Prevention**:

- Use CSRF tokens.
- Set SameSite=Lax or Strict for sensitive cookies.

## 6. Pros & Cons of Cookies

### Pros

- Easy to implement and supported by all browsers.
- Automatically sent with requests.
- Can store session IDs, preferences, tokens.

### Cons

- Limited size (~4KB per cookie).
- Vulnerable to XSS, CSRF if not secured.
- Users can delete cookies → may break sessions.
- Not suitable for storing sensitive information directly (like passwords).

## 7. Real-World Use Cases of Cookies

| Use Case                | Cookie Type                     | Why                                                                 |
|-------------------------|---------------------------------|----------------------------------------------------------------------|
| User login session      | Session cookie + HttpOnly + Secure | Server keeps session state, not exposed to JS                         |
| “Remember Me”           | Permanent cookie + Secure       | Keeps user logged in across browser restarts                         |
| User preferences        | Permanent cookie                | Stores theme, language, settings                                     |
| Analytics / tracking     | Third-party cookie              | Track user across multiple sites (ads, analytics)                    |
| CSRF prevention         | SameSite cookie                 | Prevent cross-site requests                                          |

## 8. When & Why to Use Each Cookie Type

- **Session Cookie**: Sensitive authentication → short-lived, deleted on browser close.
- **Permanent Cookie**: Convenience features → remember login, preferences.
- **HttpOnly + Secure**: Security → always use for authentication tokens.
- **SameSite**: CSRF protection → default to Lax or Strict for security.
- **Third-Party Cookie**: Analytics or ads → optional, privacy-sensitive.
- **Zombie Cookie**: Avoid → considered malicious/tracking abuse.

## Summary

Cookies are essential for web authentication, session management, and preferences.

**Best practices**:

- Always use HTTPS.
- Use HttpOnly for sensitive cookies.
- Use Secure + SameSite to prevent CSRF and hijacking.
- Keep cookies minimal → store references, not sensitive info.
- Prefer session cookies for auth and permanent cookies for convenience.





# Everything You Need to Know About Session-Based Authentication

As a backend engineer, one of the first questions I get is: “Should I use session-based authentication or token-based authentication?” The answer depends on your application’s architecture, scalability needs, and security requirements. In this article, we’ll deep dive into session-based authentication — how it works, pros & cons, security considerations, and its application in microservices and mobile apps.

## 1. What is a Session?

A session is a temporary, server-side storage of information about a user’s interaction with your application. Each session has a unique identifier (session ID), which helps the server recognize the user across multiple requests.

Think of it as a coat check ticket: you hand over your credentials once, get a ticket (session ID), and present the ticket whenever you want to access your coat. No need to keep repeating credentials.

- **Lifetime**: Starts on login, ends on logout or expiration.
- **Storage**: Can be in memory, database, or in-memory cache (Redis, Memcached).

## 2. What is Session-Based Authentication?

Session-based authentication is a method where the server keeps track of logged-in users by storing session information. The workflow:

1. User logs in with username/password.
2. Server validates credentials.
3. Server creates a session, stores it, and returns a session ID to the client.
4. Client sends the session ID with every request (usually in a cookie).
5. Server looks up the session and authenticates the user.

## 3. How Session-Based Authentication Works

Here’s a typical flow:

**Step 1: Login**

```
POST /login
Body: { "username": "rabbi", "password": "secret" }
```

**Step 2: Server Validates**

- Creates session in server store (Redis, DB, memory)
- Generates session ID (e.g., abc123)

**Step 3: Send Session ID**

```
Set-Cookie: session_id=abc123; HttpOnly; Secure; SameSite=Strict
```

**Step 4: Subsequent Requests**

```
GET /dashboard
Cookie: session_id=abc123
```

Server fetches session ID from store → authenticates user.

**Step 5: Logout / Expiration**

Session removed from server → user must log in again.

## 4. Pros & Cons of Session-Based Authentication

### Pros

- **Secure by default**: Sensitive data stored on server, not client.
- **Server-side control**: Easy to invalidate sessions (logout everywhere).
- **Supports stateful data**: Can store user roles, cart info, preferences.
- **Mature ecosystem**: Frameworks like Django, Rails, Laravel have built-in support.

### Cons

- **Server-side storage overhead**: Every session consumes memory.
- **Scaling complexity**: Multi-server setups need shared session stores or sticky sessions.
- **Stateful nature**: Breaks REST statelessness principle.
- **CSRF risk**: Because cookies are sent automatically by browsers.

## 5. Security Issues & Prevention

1. **Session Hijacking**

   - **Threat**: Attacker steals session ID.
   - **Prevention**: HTTPS, Secure + HttpOnly cookies, SameSite cookies, IP/device monitoring.

2. **Session Fixation**

   - **Threat**: Attacker sets victim’s session ID before login.
   - **Prevention**: Regenerate session ID after login, use cryptographically secure IDs.

3. **CSRF (Cross-Site Request Forgery)**

   - **Threat**: Browser sends session automatically on attacker’s request.
   - **Prevention**: CSRF tokens, SameSite cookies.

4. **XSS (Cross-Site Scripting)**

   - **Threat**: JavaScript steals session cookie.
   - **Prevention**: HttpOnly cookies, input sanitization, Content Security Policy.

5. **Long Session Lifetimes**

   - **Threat**: Stolen sessions stay valid longer.
   - **Prevention**: Idle timeout, absolute expiration, logout everywhere.

6. **Server-Side Storage Risks**

   - **Threat**: Sessions stored insecurely.
   - **Prevention**: Encrypt session store, use secure Redis/DB, store minimal sensitive data.

## 6. Session Authentication in Microservices

In a microservice architecture, session authentication requires special care:

- **Challenge**: Multiple services handle requests → session store must be shared.
- **Solution**: Use Redis or Memcached as a central session store.

**Flow**:

1. Auth service creates session.
2. Session ID returned to client.
3. API Gateway or microservices validate session by querying shared store.

**Pros**: Centralized control, server-side revocation.

**Cons**: Stateful, performance overhead, scaling complexity.

**Best Practices**:

- Use a centralized session store (Redis).
- Minimal data in sessions (user ID only, fetch roles/permissions separately).
- Use API Gateway to validate sessions → reduces load on individual services.
- Short session lifetimes, regenerate session ID after login.

## 7. Session Authentication for Mobile Apps

Mobile apps don’t automatically send cookies, so the session flow changes slightly:

- **Login**: App sends credentials → server creates session → returns session ID.
- **Storage**: Secure storage on device (iOS Keychain, Android EncryptedSharedPreferences).
- **Subsequent requests**: App sends session ID in headers (Authorization: Session abc123) or manually in cookies.
- **Security**: HTTPS, short session expiry, optional device binding.

**Pros**: Server controls session expiration, easy invalidation.

**Cons**: Centralized store required, mobile app must handle session management manually.

## 8. When to Use Session-Based Authentication

✅ **Suitable for**:

- Traditional web apps.
- Internal enterprise portals.
- E-commerce sites with carts stored server-side.
- Banking/admin systems requiring full control over sessions.

❌ **Avoid for**:

- Stateless APIs at scale (JWT is better).
- Highly distributed microservices across regions without shared session stores.
- Offline-first mobile apps needing offline validation.

## 9. Conclusion

Session-based authentication is robust, secure, and mature. For monolithic apps or controlled enterprise systems, it’s often the best choice.

However, in microservices and mobile apps, you must use a centralized session store (Redis, Memcached) and enforce best security practices: HTTPS, HttpOnly/SameSite cookies, short-lived sessions, and session ID regeneration.

When designed properly, session authentication gives you full server-side control, enabling features like logout everywhere, role updates, and fine-grained session monitoring — which are hard to implement with purely stateless tokens like JWT.







JWT:

Json Web Token
Completely Stateless
3 Parts Header, Data, Signature
Signature ecryption can be symmetrical or asymmetrical
symmetrical require same key to create JWT and validate
Asymmetrical private key create JWT, public key validates

pros:
stateless
great of apis
Secure
Carry useful info
Can store info that derive UX
No need for centelized database

Cons:
Sharing secrets in Microservices
Key management
Very tricky to consume correctly
Storage of Refresh tokens
Token Revocation and Control
Insecure implementation