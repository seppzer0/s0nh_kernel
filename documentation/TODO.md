# TODO

## Kernel features

- [ ] add working monitor mode support for internal Wi-Fi card;
- [ ] add DM-Verity and Force Encrypt disabler.

## Build process features

- [x] add an asset downloader (ROM, Magisk, etc.);
- [x] add CI/CD pipelines;
- [x] add option to save logs to a file;
- [x] add option to build in Docker container;
- [x] add multidevice support, with appropriate manifest;
- [x] improve log level setting throughout all stages of the build;
- [x] improve file/directory cleaning mechanism in a form of a dedicated module;
- [x] improve Clang download mechanism;
- [ ] add build counter mechanism for CI/CD pipelines;
- [ ] add published Conan package validator;
- [x] add codename specific elements to final kernel zip;
- [x] add a simpler and lighter bundle creator (kernel+ROM);
- [ ] add return types to functions;
- [x] add requirements.txt for pip;
- [x] add proper OS detection for preventing local builds in unsupported systems;
- [x] add static analysis for the wrapper;
- [x] add a single-point manifest with main info on the tool;
- [ ] add a unified banner for the wrapper;
- [ ] add description when creating a release via CI/CD;
- [ ] improve CI/CD flexibility (variable-wise);
- [ ] add static analysis report to release body;
- [ ] improve documentation (visual-wise).
