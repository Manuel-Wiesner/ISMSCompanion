# Security Policy

## Supported Versions

Currently supported versions for security updates:

| Version | Supported |
| ------- | --------- |
| main    | ✅        |

## Reporting a Vulnerability

**⚠️ DO NOT** create public GitHub issues for security vulnerabilities.
**Language Support**: Reports can be submitted in English or German.
We take security vulnerabilities seriously. Please use one of the following methods:

### Preferred: GitHub Security Advisories (Private)

1. Navigate to the [Security tab](https://github.com/Manuel-Wiesner/ISMSCompanion/security/advisories)
2. Click "Report a vulnerability"
3. Fill out the private advisory form

### Alternative: Encrypted Email

For highly sensitive vulnerabilities, use PGP encryption:

- Email: manuelwiesner@mailbox.org
- PGP Key: [Download Public Key](https://github.com/Manuel-Wiesner.gpg)
- Fingerprint: 0BDA BC45 8954 3EF0 F7F7 BF2D F6EF A1E8 532F 7372

To import and verify the key:

```
curl https://github.com/Manuel-Wiesner.gpg | gpg --import
gpg --fingerprint manuelwiesner@mailbox.org
```

### Response Timeline

- Initial response: 48 hours
- Status update: 7 days
- Resolution target: 30 days

## Disclosure Policy

We follow coordinated disclosure principles:

- Vulnerabilities will be disclosed publicly only after a fix is available
- Standard disclosure timeline: 90 days from initial report
- We will credit reporters unless anonymity is requested
- Early disclosure may occur for actively exploited vulnerabilities

## Security Best Practices for Contributors

- Enable 2FA on your GitHub account
- Sign commits with GPG keys
- Follow secure coding guidelines in CONTRIBUTING.md
- Run pre-commit hooks before submitting PRs

## Safe Harbor

We support security research conducted in good faith and will not pursue legal action against researchers who:

- Make a good faith effort to avoid privacy violations, service disruptions, and data destruction
- Only interact with test accounts they own or have explicit permission to access
- Do not exploit vulnerabilities beyond proof-of-concept verification
- Report findings privately according to this policy before any public disclosure
- Do not engage in extortion or similar demands

This Safe Harbor applies to security research performed under this policy.
