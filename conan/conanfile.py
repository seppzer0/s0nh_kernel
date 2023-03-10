from conans import ConanFile


class S0nhConan(ConanFile):
    name = "s0nh"
    version = "0.1"
    author = "seppzer0"
    url = "https://gitlab.com/api/v4/projects/40803264/packages/conan"
    description = "A modified LOS kernel with Kali NetHunter functionality."
    topics = ("lineageos", "oneplus5", "oneplus5t", "nethunter")
    settings = None
    options = {
                "losversion": ["20.0"],
                "chroot": ["minimal", "full"],
                "codename": ["dumpling", "cheeseburger"]
              }

    def export_sources(self):
        self.copy("*", src="source", dst=".")

    def build(self):
        cmd = "python3 wrapper kernel local {0} {1} &&"\
              "python3 wrapper assets local {0} {1} {2} --clean"\
              .format(self.options.losversion,
                      self.options.codename,
                      self.options.chroot)
        print(f"[cmd] {cmd}")
        self.run(cmd)

    def package(self):
        # package built kernel with collected assets
        self.copy("*.zip", src="kernel", dst="kernel", keep_path=False)
        self.copy("*", src="assets", dst="assets")
