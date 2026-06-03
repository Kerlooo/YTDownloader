# YTDownloader
YTDownloader is my simple way to download mp3 audio from YT. There are many tools online to do it but they're full of ads and they're very slow so I decided to create my own tool that use `ytdlp` for downloading the audio and `customtinker` for the GUI.

## How to use:
> Only tested on Linux!

Clone the repo from github:
```bash
git clone https://github.com/Kerlooo/YTDownloader
cd YTDownloader
```

Create and activate the venv:
```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

Run the script:
`python app.py` or `python3 app.py`

## Features
| Feature | Description | Status |
|---------|-------------|--------|
| Download MP3 | Download audio from YouTube video/playlist | ✅ |
| Quality selection | Choose audio quality (128,192,256,320) | ✅ |
| Settings UI | Choose output folder and default quality | ✅ |
| Threaded download | Downloads run in background thread | ✅ |
| CustomTkinter UI | Simple GUI with dark theme | ✅ |

## TODO
- [ ] Better UI
- [ ] Reset button for settings
- [ ] Add support for video download
- [ ] Progress bar
- [ ] Add batch download

## License
This guide is distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

**You are free to:**
- **Share** — copy and redistribute the material in any medium or format.
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

**Under the following terms:**
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

For more details, see the [LICENSE](LICENSE) file or visit [creativecommons.org](https://creativecommons.org/licenses/by/4.0/).