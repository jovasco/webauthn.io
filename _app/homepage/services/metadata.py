from webauthn.helpers.structs import CredentialDeviceType


class MetadataService:
    # Pulled from https://github.com/passkeydeveloper/passkey-authenticator-aaguids/ on 2024-01-03
    aaguid_json = {
        "ea9b8d66-4d01-1d21-3ce4-b6b48cb575d4": {"name": "Google Password Manager"},
        "adce0002-35bc-c60a-648b-0b25f1f05503": {"name": "Chrome on Mac"},
        "08987058-cadc-4b81-b6e1-30de50dcbe96": {"name": "Windows Hello"},
        "9ddd1817-af5a-4672-a2b9-3e3dd95000a9": {"name": "Windows Hello"},
        "6028b017-b1d4-4c02-b4b3-afcdafc96bb2": {"name": "Windows Hello"},
        "dd4ec289-e01d-41c9-bb89-70fa845d4bf2": {"name": "iCloud Keychain (Managed)"},
        "531126d6-e717-415c-9320-3d9aa6981239": {"name": "Dashlane"},
        "bada5566-a7aa-401f-bd96-45619a55120d": {"name": "1Password"},
        "b84e4048-15dc-4dd0-8640-f4f60813c8af": {"name": "NordPass"},
        "0ea242b4-43c4-4a1b-8b17-dd6d0b6baec6": {"name": "Keeper"},
        "f3809540-7f14-49c1-a8b3-8f813b225541": {"name": "Enpass"},
        "b5397666-4885-aa6b-cebf-e52262a439a2": {"name": "Chromium Browser"},
        "771b48fd-d3d4-4f74-9232-fc157ab0507a": {"name": "Edge on Mac"},
        "39a5647e-1853-446c-a1f6-a79bae9f5bc7": {"name": "IDmelon"},
        "d548826e-79b4-db40-a3d8-11116f7e8349": {"name": "Bitwarden"},
        "fbfc3007-154e-4ecc-8c0b-6e020557d7bd": {"name": "iCloud Keychain"},
        "53414d53-554e-4700-0000-000000000000": {"name": "Samsung Pass"},
        "66a0ccb3-bd6a-191f-ee06-e375c50b9846": {"name": "Thales Bio iOS SDK"},
        "8836336a-f590-0921-301d-46427531eee6": {"name": "Thales Bio Android SDK"},
        "cd69adb5-3c7a-deb9-3177-6800ea6cb72a": {"name": "Thales PIN Android SDK"},
        "17290f1e-c212-34d0-1423-365d729f09d9": {"name": "Thales PIN iOS SDK"},
    }

    # Yubico AAGUIDs from https://support.yubico.com/hc/en-us/articles/360016648959-YubiKey-Hardware-FIDO2-AAGUIDs
    aaguid_json.update(
        {
            "0bb43545-fd2c-4185-87dd-feb0b2916ace": {
                "name": "Security Key NFC by Yubico - Enterprise Edition"
            },
            "149a2021-8ef6-4133-96b8-81f8d5b7f1f5": {"name": "Security Key by Yubico with NFC"},
            "2fc0579f-8113-47ea-b116-bb5a8db9202a": {"name": "YubiKey 5 Series with NFC"},
            "6d44ba9b-f6ec-2e49-b930-0c8fe920cb73": {"name": "Security Key by Yubico with NFC"},
            "73bb0cd4-e502-49b8-9c6f-b59445bf720b": {"name": "YubiKey 5 FIPS Series"},
            "85203421-48f9-4355-9bc8-8a53846e5083": {"name": "YubiKey 5Ci FIPS"},
            "a4e9fc6d-4cbe-4758-b8ba-37598bb5bbaa": {"name": "Security Key by Yubico with NFC"},
            "b92c3f9a-c014-4056-887f-140a2501163b": {"name": "Security Key by Yubico"},
            "c1f9a0bc-1dd2-404a-b27f-8e29047a43fd": {"name": "YubiKey 5 FIPS Series with NFC"},
            "c5ef55ff-ad9a-4b9f-b580-adebafe026d0": {"name": "YubiKey 5Ci"},
            "cb69481e-8ff7-4039-93ec-0a2729a154a8": {"name": "YubiKey 5 Series"},
            "d8522d9f-575b-4866-88a9-ba99fa02f35b": {"name": "YubiKey Bio Series"},
            "ee882879-721c-4913-9775-3dfcce97072a": {"name": "YubiKey 5 Series"},
            "f8a011f3-8c0a-4d15-8006-17111f9edc7d": {"name": "Security Key by Yubico"},
            "fa2b99dc-9e39-4257-8f92-4a30d23c4118": {"name": "YubiKey 5 Series with NFC"},
        }
    )

    def get_provider_name(self, *, aaguid: str, device_type: CredentialDeviceType) -> str:
        """
        Try to map the provided AAGUID to a human-friendly provider name
        """
        default_name = ""

        if not aaguid:
            return default_name

        provider_metadata = self.aaguid_json.get(aaguid, {})
        provider_name = provider_metadata.get("name", None)

        # Return the name if we could look one up
        if provider_name is not None:
            return provider_name

        # Try to derive the provider name
        if (
            aaguid == "00000000-0000-0000-0000-000000000000"
            and device_type == CredentialDeviceType.MULTI_DEVICE
        ):
            return "iCloud Keychain"

        # When all else fails, provide a default name
        return default_name
