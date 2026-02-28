"""小说下载器 - 启动入口"""

from novel_downloader.app import NovelDownloaderApp


def main():
    app = NovelDownloaderApp()
    app.run()


if __name__ == "__main__":
    main()
