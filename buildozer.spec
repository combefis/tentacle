[app]

title = Tentacle
package.name = tentacle
package.domain = be.combefis

source.dir = .
source.include_exts = py,kv
source.exclude_exts = spec,md
source.exclude_patterns = LICENSE

version = 0.0.1a1

requirements = kivy

orientation = portrait
fullscreen = 1

android.api = 24
android.arch = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1

bin_dir = ./bin
