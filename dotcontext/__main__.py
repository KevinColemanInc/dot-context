def main():
    try:
        import sys

        if len(sys.argv) < 3:
            print("Usage: python main.py [watch|run] <path_to_file|directory>")
        else:
            from dotcontext.run.main import run

            cmd = sys.argv[1]
            inst_file_path = sys.argv[2]
            if cmd == "run":
                run(inst_file_path)
            elif cmd == "watch":
                from dotcontext.watch.main import Watcher

                watcher = Watcher(".")
                watcher.run()
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":  # pragma: nocover
    import sys

    sys.exit(main())
