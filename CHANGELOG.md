# Changelog

## Unreleased

### Support

- Dropped support for Wagtail 6.x (Wagtail 6.3 LTS reached end of life on 2026-05-01).
- Minimum supported Wagtail version is now 7.0 LTS.
- Tested against Wagtail 7.0 LTS, 7.3, and 7.4 LTS.
- Declared support for Django 6.0 (in addition to existing 4.2, 5.1, 5.2).
- Added `python_requires=">=3.10"` to package metadata.

### Changed

- Bumped `jinja2` testing extra minimum to `>=3.0` and removed the pinned `markupsafe` testing dependency.
- Removed the legacy Jinja2 2.x compatibility shim from `wagtailschemaorg.jinja2tags`; the module now imports `pass_context` directly from Jinja2 3.x+.

### Fixed

- Removed reference to the long-removed `django.contrib.auth.middleware.SessionAuthenticationMiddleware` from the test settings.
- Removed the obsolete `bdist_wheel.universal = 1` flag from `setup.cfg` (the package is Python 3 only).
- Fixed an invalid version specifier in `docs/requirements.txt`.
