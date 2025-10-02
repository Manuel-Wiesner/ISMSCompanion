"""Security-specific exceptions for ISMSCompanion.

Custom exceptions improve error handling and security logging by providing
structured error information for audit trails and monitoring.
"""

__all__ = [
    "CryptoError",
    "InvalidKeyError",
    "DecryptionError",
    "NonceReuseError",
    "WeakPasswordError",
    "KeyDerivationError",
]


class CryptoError(Exception):
    """Base exception for cryptographic errors.

    All crypto-specific exceptions inherit from this base class,
    allowing centralized exception handling for security operations.
    """

    pass


class InvalidKeyError(CryptoError):
    """Raised when key size or format is invalid.

    Example:
        Attempting to use a 128-bit key with AES-256
    """

    pass


class DecryptionError(CryptoError):
    """Raised when decryption fails.

    Possible causes:
        - Wrong password/key
        - Tampered ciphertext (authentication tag mismatch)
        - Corrupted data

    Security:
        Do not expose specific failure reason to prevent oracle attacks
    """

    pass


class NonceReuseError(CryptoError):
    """Raised when nonce reuse is detected (CRITICAL security issue).

    Nonce reuse with the same key breaks confidentiality in GCM and ChaCha20-Poly1305.
    This should trigger immediate security incident response.
    """

    pass


class WeakPasswordError(CryptoError):
    """Raised when password does not meet security policy requirements.

    Example policy violations:
        - Password too short (< 12 characters)
        - Password contains only lowercase letters
        - Password is in common password database
    """

    pass


class KeyDerivationError(CryptoError):
    """Raised when key derivation fails (PBKDF2/Argon2).

    Possible causes:
        - Invalid salt format
        - Unsupported KDF algorithm
        - System resource constraints (Argon2 memory allocation)
    """

    pass
