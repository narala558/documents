from androguard.core.bytecodes import apk

apk = apk.APK('test.apk')

print(apk.get_androidversion_code())
