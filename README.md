kzg-special-contribution
========================

This is the code and details for the special contribution I made to the Ethereum KZG Summoning Ceremony (https://ceremony.ethereum.org/).

The contribution was based on entropy generated with CAN bus data from my car (a 2023 Hyundai Elantra Hybrid Limited), captured with a comma.ai panda attached to a comma three (https://comma.ai/shop/comma-three), running sunnypilot (https://github.com/sunnyhaibin/sunnypilot).

Anyone should be able to reproduce the entropy generation process for this contribution, assuming you have a comma three attached to a compatible car, by following the instructions below.

Reproducing the process
-----------------------

1. **Preparation**: The comma three has an on-board cellular modem for use with the comma connect service. Make sure the SIM card slot is empty, so that no entropy is leaked to comma's servers. Also, make sure there is no important data saved on the comma three's NVMe drive, as it will be removed and destroyed at the end of the process.

2. **Capture the entropy**: With the comma three attached and turned on, drive around. The goal is to maximize "interesting" CAN bus data, which includes steering wheel angle, gas/brake pedal angles, and camera/radar measurements, so try to make many interactions with the car's controls and drive on roads with many other cars around.

3. **Retrieve the entropy**:
    1. Turn the car off and disconnect the comma three.
    2. Follow the instructions here: https://enjoi.dev/posts/2021-12-20-comma-3-teardown to open the comma three, remove the NVMe drive, and put it in a USB enclosure. It's also a good time to replace it with a new drive and re-assemble, as the old drive will be destroyed later. (*Note: The comma three doesn't have an easy way to retrieve files via USB, the "official" options are SSH or using the comma connect service, neither of which are suitable for keeping the entropy secret. It's possible to live-stream the CAN bus data via USB-serial, but this is somewhat more complicated, and the logs will be written to the NVMe drive anyway, so it has to be replaced regardless.*)
    3. On an air-gapped computer, transfer `get-entropy.py` from this repo.
    4. Connect the NVMe drive and mount it.
    5. Run `python3 get-entropy.py <path to mounted drive>`. If everything went well, you should get an output `Entropy: xxxx`.

4. **Make your contribution**: Follow the instructions with one of the KZG ceremony clients to make a contribution using the entropy value output from the script (eg. https://github.com/jsign/go-kzg-ceremony-client#offline-contributions, https://github.com/PatriceVignola/cpp-kzg-ceremony-client#dual-computer-setup).

5. **Destroy the entropy**: Destroy the old NVMe drive.

My contribution
---------------

My specific contribution is #83337 from the sequencer (look it up here: https://ceremony.ethereum.org/#/record), with the following parameters:

ETH public key: 0x192ccacdd6da99463e1e8a76223ea07a6cde3479

Powers of Tau pubkeys:
- (2^12): 0x932a946bad415d52f5df4a33400343f234207ac228356e31402d7dc59fa8d070a40fec9845f227473308b928e47d15e50554eb9d98784099ae9918a4c6c69402e1f5123a78a97d4d054fee94d817ea043b3f3eaf9af259ddd209d5e0b7d01ca3
- (2^13): 0xb3a1d9379b96cdb29aa8f381555efcda1273e9ea8168e9d43e7bf62d461100ec905da84251799e6201c808e670da42d90784856ff819e797ca39ad7510152c048374df8f748327b9a2d5c8f10e220046cb83b71e6eb516bfa627af5e367436e3
- (2^14): 0x9642b7ea0df52d7c4e0a35b385659551887d6e5fab5458d89cd898b382f6dd2aa82ce49d8db4921ad85741fb347b1a93057b8e1e84687a40fb659550fb1db4afe6924fec2ae1d73efd628f7dc0f9e343319971b7397baa6e24949c1cc243461a
- (2^15): 0xa5fb2e8b94cc38941e392902875ea3d8d2e2de9a848184ea06a5fe38ba3021b243e52f26019cf849ac624ca20fae5fbd14b7657c4f66922d59412cd7cfb436946f40c0f96e3c7d7a2344336888f6ab905fca9c66717edc69887f227ef09be141

The front-camera video from the drive used for entropy capture is available on YouTube: https://youtu.be/ZR6vUlRlWf8. The drive occurred in central Austin, Texas on April 12 2023, during peak afternoon traffic hours (around 4-5PM CST) on a mix of highway and city roads. This was done to maximize the number of other cars on the road and vary the driving environment, which in turn should maximize the entropy captured.

Below are some photos from the contribution:

<p align="center">
    <img src="https://raw.githubusercontent.com/stephensolis/kzg-special-contribution/master/images/img1.jpg">
    <i>The NVMe drive before destruction.</i>
</p>
<p align="center">
    <img src="https://raw.githubusercontent.com/stephensolis/kzg-special-contribution/master/images/img3.jpg">
    <i>The comma three with NVMe drive installed, before entropy capture.</i>
</p>
<p align="center">
    <img src="https://raw.githubusercontent.com/stephensolis/kzg-special-contribution/master/images/img2.jpg">
    <i>The NVMe drive after destruction, accomplished by drilling a total of 5 holes through each chip on the board.</i>
</p>
<p align="center">
    <img src="https://raw.githubusercontent.com/stephensolis/kzg-special-contribution/master/images/img4.jpg">
    <i>The comma three powered on, showing the firmware used during the drive.</i><br/>
    <i>The release string was "sunnypilot 2022.11.13 / test-c3 / a0e6bb9 / Mar 26", which is available here: https://github.com/sunnyhaibin/sunnypilot/tree/a0e6bb94da3aea655d815574f999927d257df865.</i>
</p>
<p align="center">
    <img src="https://raw.githubusercontent.com/stephensolis/kzg-special-contribution/master/images/img5.jpg">
    <i>The interior of the car, showing the comma three mounted to the front windshield.</i>
</p>

License ![License](http://img.shields.io/:license-mit-blue.svg)
-------

    The MIT License (MIT)

    Copyright (c) 2023 Stephen

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.