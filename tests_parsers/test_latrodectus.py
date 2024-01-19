# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from modules.processing.parsers.CAPE.Latrodectus import extract_config


def test_bumblebee():
    with open("tests/data/malware/a547cff9991a713535e5c128a0711ca68acf9298cc2220c4ea0685d580f36811", "rb") as data:
        conf = extract_config(data.read())
        assert conf == {
            "C2": ["https://arsimonopa.com/live/", "https://lemonimonakio.com/live/"],
            "Group name": "Novik",
            "Campaign ID": 1053565364,
            "Strings": [
                "/c ipconfig /all",
                "C:\\Windows\\System32\\cmd.exe",
                "/c systeminfo",
                "C:\\Windows\\System32\\cmd.exe",
                "/c nltest /domain_trusts",
                "C:\\Windows\\System32\\cmd.exe",
                "/c nltest /domain_trusts /all_trusts",
                "C:\\Windows\\System32\\cmd.exe",
                "/c net view /all /domain",
                "C:\\Windows\\System32\\cmd.exe",
                "/c net view /all",
                "C:\\Windows\\System32\\cmd.exe",
                '/c net group "Domain Admins" /domain',
                "C:\\Windows\\System32\\cmd.exe",
                "/Node:localhost /Namespace:\\\\root\\SecurityCenter2 Path AntiVirusProduct Get * /Format:List",
                "C:\\Windows\\System32\\wbem\\wmic.exe",
                "/c net config workstation",
                "C:\\Windows\\System32\\cmd.exe",
                "/c wmic.exe /node:localhost /namespace:\\\\root\\SecurityCenter2 path AntiVirusProduct Get DisplayName | findstr /V /B /C:displayName || echo No Antivirus installed",
                "C:\\Windows\\System32\\cmd.exe",
                "/c whoami /groups",
                "C:\\Windows\\System32\\cmd.exe",
                ".dll",
                ".exe",
                '"%s"',
                "",
                "rundll32.exe",
                '"%s", %s %s',
                "runnung",
                ":wtfbbq",
                "%d",
                "%s%s",
                "%s\\%d.dll",
                "%d.dat",
                "%s\\%s",
                'init -zzzz="%s\\%s"',
                "front",
                "/files/",
                "Novik",
                ".exe",
                "Content-Type: application/x-www-form-urlencoded",
                "POST",
                "GET",
                "curl/7.88.1",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Tob 1.1)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Tob 1.1)",
                "CLEARURL",
                "URLS",
                "COMMAND",
                "ERROR",
                "12345",
                "counter=%d&type=%d&guid=%s&os=%d&arch=%d&username=%s&group=%lu&ver=%d.%d&up=%d&direction=%s",
                "counter=%d&type=%d&guid=%s&os=%d&arch=%d&username=%s&group=%lu&ver=%d.%d&up=%d&direction=%s",
                "counter=%d&type=%d&guid=%s&os=%d&arch=%d&username=%s&group=%lu&ver=%d.%d&up=%d&direction=%s",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Tob 1.1)",
                "%s%d.dll",
                "%s%d.exe",
                "LogonTrigger",
                "%x%x",
                "TimeTrigger",
                "PT1H%02dM",
                "&mac=",
                ";",
                "%04d-%02d-%02dT%02d:%02d:%02d",
                "%02x",
                ":%02x",
                "PT0S",
                "&computername=%s",
                "&domain=%s",
                "\\*.dll",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
                "%04X%04X%04X%04X%08X%04X",
                "%04X%04X%04X%04X%08X%04X",
                "\\Registry\\Machine\\",
                "AppData",
                "Desktop",
                "Startup",
                "Personal",
                "Local AppData",
                "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders",
                "C:\\WINDOWS\\SYSTEM32\\rundll32.exe %s,%s",
                "C:\\WINDOWS\\SYSTEM32\\rundll32.exe %s",
                "URLS",
                "URLS|%d|%s\r\n",
            ],
        }
