#!/system/bin/sh

# grant permissions for the NetHunter app
PERMISSIONS="
android.permission.INTERNET
android.permission.ACCESS_WIFI_STATE
android.permission.CHANGE_WIFI_STATE
android.permission.READ_EXTERNAL_STORAGE
android.permission.WRITE_EXTERNAL_STORAGE
com.offsec.nhterm.permission.RUN_SCRIPT
com.offsec.nhterm.permission.RUN_SCRIPT_SU
com.offsec.nhterm.permission.RUN_SCRIPT_NH
com.offsec.nhterm.permission.RUN_SCRIPT_NH_LOGIN
android.permission.RECEIVE_BOOT_COMPLETED
android.permission.WAKE_LOCK
android.permission.VIBRATE
android.permission.FOREGROUND_SERVICE
"
echo "[ * ] Fixing NetHunter permissions for Android 12+.."
for perm in $PERMISSIONS; do pm grant -g com.offsec.nethunter $perm; done
sleep 3
echo "[ + ] Done!"

# prepare the chroot dir
echo "[ * ] Preparing chroot directory.."
chroot_dir="/data/local/nhsystem"
if [ ! -d "${chroot_dir}/kali-arm64" ]; then
    mkdir -p $chroot_dir
    mkdir "${chroot_dir}/kali-arm64"
fi
sleep 3
echo "[ + ] Done!"
