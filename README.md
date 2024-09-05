Dot Context is a code-gen engine interfacing users by natural languages.

```
$ dotcontext watch .
```

## Demo

## Quick start

In your project directory, start the file watcher:

## Installation

```
$ pip3 install dotcontext
```

```
$ export OPENAI_API_KEY=...
```

Now run this in your project directory:

```
$ dotcontext watch .
```

Whenever a `*.instruct` file is saved, an LLM will automatically update the corresponding file based on the instructions. The original file will be overwritten.

**Warning:** Use this only with projects under version control (e.g., Git), as it will overwrite files.

### dot-context schema

instructs dot-context to include this file in the LLM request

```
@import examples/vite/package.json
```

# Visual Studio Code Extension

Install the extension to get proper linting for the .instruction and .context files: [Install link](https://marketplace.visualstudio.com/items?itemName=DotContext.dot-context)

This is a mono-repo. the source code for the vs-code exension can be found in `./vs-code-ext`

### Contributors

- [@kevincolemaninc](https://github.com/kevincolemaninc)
- [@Heronalps](https://github.com/Heronalps)
- [@Sharonli](https://github.com/Sharonli)
- [@foadgr](https://github.com/foadgr)

### Discord

https://discord.gg/39kKQgnV
