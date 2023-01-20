import os
import sys
import json
import shutil
import argparse
import itertools
import subprocess
import tools.customcmd as ccmd
import tools.fileoperations as fo
import tools.messagedecorator as msg


def parse_args():
    """Parse the script arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("losversion",
                        help="select LineageOS version")
    parser.add_argument("codename",
                        help="select device codename")
    global args
    args = parser.parse_args()


def build_kernel(losver, clean_only=False):
    """Build the kernel."""
    cmd = f"python3 {os.path.join(workdir, 'wrapper', 'modules', 'kernel.py')} {args.codename} {losver}"
    if clean_only:
        cmd += " -c"
    if not os.path.isdir("release") or clean_only is True:
        ccmd.launch(cmd)


def collect_assets(losver, chroot):
    """Collect assets."""
    ccmd.launch(f"python3 {os.path.join(workdir, 'wrapper', 'modules', 'assets.py')} {args.codename} {losver} {chroot} --clean")


def conan_sources():
    """Prepare sources for rebuildable Conan packages."""
    sourcedir = os.path.join(workdir, "source")
    print("\n", end="")
    msg.note("Copying sources for Conan packaging..")
    shutil.rmtree(sourcedir, ignore_errors=True)
    fo.ucopy(workdir, sourcedir, ["__pycache__",
                                  ".vscode",
                                  "source",
                                  "release",
                                  "localversion",
                                  "Dockerfile",
                                  ".dockerignore",
                                  "assets",
                                  "conanfile.py",
                                  "manifest.json"])
    msg.done("Done!")


def conan_options(json_file):
    """Read Conan options from a JSON."""
    with open(json_file) as f:
        json_data = json.load(f)
    return json_data


def conan_package(options, reference):
    """Create the Conan package."""
    cmd = f"conan export-pkg . {reference}"
    for option_value in options:
        # not the best solution, but will work temporarily for 'losversion' and 'chroot' options
        option_name = "losversion" if not any(c.isalpha() for c in option_value) else "chroot"
        cmd += f" -o {option_name}={option_value}"
    # add codename as an option separately
    cmd += f" -o codename={args.codename}"
    ccmd.launch(cmd)


def conan_upload(reference):
    """Upload Conan component to the remote."""
    url = "https://gitlab.com/api/v4/projects/40803264/packages/conan"
    alias = "s0nhconan"
    cmd = f"conan upload -f {reference} -r {alias}"


# parse arguments
parse_args()
# form Conan reference
workdir = os.getenv("ROOTPATH")
name = "s0nh"
version = "0.1"
user = args.codename
channel = "stable" if subprocess.check_output("git branch --show-current", shell=True).decode("utf-8") == "main" else "testing"
reference = f"{name}/{version}@{user}/{channel}"
# form option sets
losversion = [args.losversion]
chroot = ["minimal", "full"]
option_sets = list(itertools.product(losversion, chroot))
# build and upload Conan packages
fo.ucopy(os.path.join(workdir, "conan"), workdir)
for opset in option_sets:
    build_kernel(opset[0])
    build_kernel(opset[0], True)
    conan_sources()
    collect_assets(opset[0], opset[1])
    conan_package(opset, reference)
os.chdir(workdir)
# upload package
if os.getenv("CONAN_UPLOAD_CUSTOM") == "1":
    conan_upload(reference)