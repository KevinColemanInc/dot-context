Dot Context is a code-gen engine interfacing users by natural languages.

```
$ python -m main 'example/vite/src/components/Footer.tsx.instruct'
```

### Demo

### Quick start

In your project directory, start the file watcher:

# Installation

```
$ pip3 install dotcontext
```

```
$ export OPENAI_API_KEY=...
```

Now run this in your project directory:

```
$ dotcontext watch
```

Now every time a `*.instruct` file is updated, an LLM will be called to update the `*` file based on those instructions

Now whenever the .instruct file is saved, the corresponding file will overwritten

**Warning:** Please only use this on projects with git enabled, because it will overwrite files

## doctInstruction schema

instructs dot-context to include this file in the LLM request

```
@import examples/vite/package.json
```

# Visual Studio Code Extension

Install the extension to get proper linting for the .instruction and .context files: [Install link](https://marketplace.visualstudio.com/items?itemName=DotContext.dot-context)

This is a mono-repo. the source code for the vs-code exension can be found in `./vs-code-ext`

### Contribution

### Contributors

- [@kevincolemaninc](https://github.com/kevincolemaninc)
- [@Heronalps](https://github.com/Heronalps)
- [@Sharonli](https://github.com/Sharonli)
- [@foadgr](https://github.com/foadgr)

### Discord

https://discord.gg/39kKQgnV
