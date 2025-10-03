"""Cryptographic configuration and security constants.

This module centralizes all security-critical constants following OWASP, NIST,
and ISO 27001 recommendations. Keeping constants separate from implementation
improves auditability and configuration management.

References:
    - OWASP Password Storage Cheat Sheet (2023)
    - NIST SP 800-132: PBKDF2 Recommendations
    - NIST SP 800-175B: Key Derivation Methods
    - RFC 7539: ChaCha20-Poly1305
    - RFC 5116: AEAD Interface
"""

from dataclasses import dataclass
from typing import ClassVar

__all__ = [
    "CryptoConfig",
    "crypto_config",
    "validate_config",
]


@dataclass(frozen=True)
class CryptoConfig:
    """Immutable security constants for cryptographic operations.

    Security Rationale:
        - All values follow industry best practices as of 2025
        - Conservative parameters chosen to withstand future attacks
        - Memory/time trade-offs optimized for server-side use

    Compliance:
        - ISO 27001:2022 A.8.24 (Use of cryptographic keys)
        - GDPR Article 32 (Security of processing)
        - BSI TR-02102-1 (Cryptographic Mechanisms)
    """

    # Key sizes (bits → bytes)
    SALT_SIZE: ClassVar[int] = 32  # 256 bits - prevents rainbow tables
    AES_KEY_SIZE: ClassVar[int] = 32  # 256 bits - post-quantum recommended
    CHACHA_KEY_SIZE: ClassVar[int] = 32  # 256 bits - ChaCha20 standard

    # Nonce/IV sizes
    AES_NONCE_SIZE: ClassVar[int] = 12  # 96 bits - GCM standard (RFC 5116)
    CHACHA_NONCE_SIZE: ClassVar[int] = 12  # 96 bits - ChaCha20 standard

    # PBKDF2 parameters (backward compatibility only)
    PBKDF2_ITERATIONS: ClassVar[int] = 600_000  # OWASP 2023 minimum for SHA-256

    # Argon2id parameters (recommended for new implementations)
    ARGON2_TIME_COST: ClassVar[int] = 3  # Iterations
    ARGON2_MEMORY_COST: ClassVar[int] = 65536  # 64 MiB (OWASP recommendation)
    ARGON2_PARALLELISM: ClassVar[int] = 4  # Threads (CPU cores)

    # Security metadata
    CRYPTO_VERSION: ClassVar[str] = "1.0.0"
    MIN_PASSWORD_LENGTH: ClassVar[int] = 12  # NIST SP 800-63B recommendation


# Singleton instance for easy import
crypto_config: CryptoConfig = CryptoConfig()


# Validation function for runtime checks
def validate_config() -> None:
    """Validate security parameters meet minimum requirements.

    Raises:
        ValueError: If security parameters are too weak
    """
    if crypto_config.PBKDF2_ITERATIONS < 600_000:
        raise ValueError(
            f"PBKDF2 iterations too low: {crypto_config.PBKDF2_ITERATIONS} "
            "(OWASP 2023 minimum: 600,000)"
        )

    if crypto_config.ARGON2_MEMORY_COST < 65536:  # 64 MiB
        raise ValueError(
            f"Argon2 memory cost too low: {crypto_config.ARGON2_MEMORY_COST} KiB "
            "(OWASP 2023 minimum: 65536 KiB / 64 MiB)"
        )

    if crypto_config.ARGON2_TIME_COST < 2:
        raise ValueError(
            f"Argon2 time cost too low: {crypto_config.ARGON2_TIME_COST} (minimum: 2)"
        )


validate_config()

if __name__ == "__main__":
    # Self-test
    validate_config()
    print("✓ Crypto configuration validated")
    print(f"  PBKDF2 iterations: {crypto_config.PBKDF2_ITERATIONS:,}")
    print(f"  Argon2 memory: {crypto_config.ARGON2_MEMORY_COST / 1024:.1f} MiB")
